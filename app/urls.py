# myapp/urls.py
from django.urls import path # type: ignore
from .views import home 
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from . import views

urlpatterns = [
    path('', home, name='home'), 
    # about 
    path('About/Background/', views.About_background, name='About_background'),
    path('About/Philosophy/', views.About_philosophy, name='About_philosophy'),
    path('About/Pource/', views.About_source, name='About_source'),
    path('About/Gallery/', views.Gallery, name='Gallery'),

    # Governance
    path('Governance/Management Teams', views.Management_teams, name='Management_teams'),
    path('Governance/Corporate Teams', views.Corporate_teams, name='Corporate_teams'),
    path('Governance/Committees/', views.Committees, name='Committees'),
    path('Governance/Board Of Directors/', views.Board_of_directors, name='Board_of_directors'),

    # services 
    path('Financial Services/', views.financial_services, name='financial_services'),
    path('Service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('Subservice/<int:sub_service_id>/', views.sub_service_detail, name='sub_service_detail'),


    # Financial Highlights
    path('Financial Highlights/Annual_Report/', views.Annual_Report, name='annual_report'),
    path('Financial Highlights/Quarterly_Report/', views.Quarterly_report, name='quarterly_reports'),
    path('Financial Highlights/Agm_Minutes/', views.Agm_minutes, name='agm_minutes'),
    path('Financial Highlights/Base_Rate/', views.Base_rate, name='base_rate'),

    # Contact
    path('Contact/', views.Contact, name='contact'),

    # FAQS
    path('FAQS/', views.FAQS, name='FAQS'),


    # Notices
    path('Notices/', views.Notices, name='notices'),
    
    # Add more URLs as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
