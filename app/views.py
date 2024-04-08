from django.shortcuts import render # type: ignore
from .models import BannerSlider, HomeImage, Description
from .models import *

def home(request):
    sliders = BannerSlider.objects.all()
    latest_image = HomeImage.objects.last()
    latest_description = Description.objects.last()
    return render(request, 'app/home.html', {'sliders': sliders, 'latest_image': latest_image, 'latest_description': latest_description})



# about

def About_background(request):
    return render(request, 'app/about_background.html')

def About_philosophy(request):
    return render(request, 'app/about_philosophy.html')

def About_source(request):
    return render(request, 'app/about_source.html')


def Gallery(request):
    photos = Photo.objects.all()
    return render(request, 'app/gallery.html', {'photos': photos})


# governance 
# management_teams
def Management_teams(request):
    teams = ManagementTeam.objects.all()
    return render(request, 'app/management_teams.html', {'teams': teams})


# Governance/corporate_teams
def Corporate_teams(request):
    c_teams = CorporateTeams.objects.all()
    return render(request, 'app/corporate_teams.html' ,{'c_teams':c_teams})

# Governance/Committee
def Committees(request):
    committees = Committee.objects.all()
    return render(request, 'app/committees.html', {'committees': committees})

# Governance/board_of_directors
def Board_of_directors(request):
    board_members = BoardMember.objects.all()
    return render(request, 'app/board_of_directors.html', {'board_members': board_members})


# services 

from django.shortcuts import render # type: ignore
from .models import Service, SubService
from django.shortcuts import render, get_object_or_404  # type: ignore # Import get_object_or_404

def financial_services(request):
    services = Service.objects.all()
    return render(request, 'app/financial_services.html', {'services': services})

def service_detail(request, service_id):
    service = Service.objects.get(pk=service_id)
    sub_services = SubService.objects.filter(service=service)
    return render(request, 'app/service_detail.html', {'service': service, 'sub_services': sub_services})

def sub_service_detail(request, sub_service_id):
    sub_service = SubService.objects.get(pk=sub_service_id)
    return render(request, 'app/sub_service_detail.html', {'sub_service': sub_service})

def financial_services(request):
    services = Service.objects.all()
    return render(request, 'app/financial_services.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)  # Use get_object_or_404 to handle object not found
    sub_services = SubService.objects.filter(service=service)
    return render(request, 'app/service_detail.html', {'service': service, 'sub_services': sub_services})

def sub_service_detail(request, sub_service_id):
    sub_service = get_object_or_404(SubService, pk=sub_service_id)  # Use get_object_or_404 to handle object not found
    return render(request, 'app/sub_service_detail.html', {'sub_service': sub_service})


# Financial Highlights

def Annual_Report(request):
    reports = AnnualReport.objects.all()
    return render(request, 'app/annual_report.html', {'reports': reports})


def Quarterly_report(request):
    reports = QuarterlyReport.objects.all()
    return render(request, 'app/quarterly_report.html', {'reports': reports})

def Agm_minutes(request):
    minutes = AGMMinutes.objects.all()
    return render(request, 'app/agm_minutes.html', {'minutes': minutes})

def Base_rate(request):
    base_rates = BaseRate.objects.all()
    return render(request, 'app/base_rate.html', {'base_rates': base_rates})


# Contact
def Contact(request):
    contact_info = ContactInfo.objects.first()  # Assuming there's only one contact info instance
    return render(request, 'app/contact.html', {'contact_info': contact_info})


# FAQS
def FAQS(request):
    faqs = FAQ.objects.all()
    return render(request, 'app/faqs.html',{'faqs': faqs})

# Notices
def Notices(request):
    notices = Notice.objects.all()
    return render(request, 'app/notices.html', {'notices': notices})