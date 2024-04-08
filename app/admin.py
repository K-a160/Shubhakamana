# admin.py
from django.contrib import admin # type: ignore
from .models import BannerImage, HomeImage, Description, Photo,BannerSlider
from .models import *
from ckeditor.widgets import CKEditorWidget # type: ignore
from django import forms # type: ignore



# home 
class BannerSliderAdmin(admin.ModelAdmin):
    filter_horizontal = ('images',)

admin.site.register(BannerImage)
admin.site.register(BannerSlider, BannerSliderAdmin)



@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Check if an image is provided and not empty
        if 'image' in form.cleaned_data:
            new_image = form.cleaned_data['image']
            if new_image:
                # Delete previous image if it exists
                existing_image = HomeImage.objects.first()
                if existing_image:
                    existing_image.image.delete()
                # Save the new image
                obj.image = new_image
        super().save_model(request, obj, form, change)

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Check if description is provided and not empty
        if 'text' in form.cleaned_data:
            new_text = form.cleaned_data['text']
            if new_text:
                # Delete previous description if it exists
                existing_description = Description.objects.first()
                if existing_description:
                    existing_description.delete()
                # Save the new description
                obj.text = new_text
        super().save_model(request, obj, form, change)



# about/gallery
admin.site.register(Photo)

# governance/management_teams
admin.site.register(ManagementTeam)

# Governance/corporate_teams
admin.site.register(CorporateTeams)

# Governance/Committee
admin.site.register(Committee)
admin.site.register(CommitteeMember)

# Governance/BoardMember
admin.site.register(BoardMember)

# services 
from django import forms # type: ignore
from django.contrib import admin # type: ignore
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # type: ignore # Changed import
from .models import Service, SubService

class ServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())  # Changed widget
    
    class Meta:
        model = Service
        fields = '__all__'

class SubServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())  # Changed widget
    
    class Meta:
        model = SubService
        fields = '__all__'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm

@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    form = SubServiceAdminForm
   
   
# # Financial Highlights 
admin.site.register(AnnualReport)
admin.site.register(QuarterlyReport)
admin.site.register(AGMMinutes)
admin.site.register(BaseRate)


# Contact
admin.site.register(ContactInfo)


# FAQS
admin.site.register(FAQ)


# Notices
admin.site.register(Notice)

