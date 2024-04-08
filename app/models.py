from django.db import models # type: ignore
from django.db.models.signals import pre_delete, pre_save # type: ignore
from django.dispatch import receiver # type: ignore
from PIL import Image # type: ignore
import os

# Define a common function to handle image deletion
def delete_image(instance, **kwargs):
    instance.image.delete(False)

# Define a common function to handle image updating
def update_image(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False

    if not old_instance.image == instance.image:
        old_instance.image.delete(False)

# home banner 
class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        desired_width = 1200
        desired_height = 600
        
        img_resized = img.resize((desired_width, desired_height), Image.LANCZOS)
        img_resized.save(self.image.path)

@receiver(pre_delete, sender=BannerImage)
def banner_image_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

@receiver(pre_save, sender=BannerImage)
def banner_image_update(sender, instance, **kwargs):
    update_image(sender, instance, **kwargs)
    
class BannerSlider(models.Model):
    images = models.ManyToManyField(BannerImage)

# home middle
class HomeImage(models.Model):
    image = models.ImageField(upload_to='home_images')

@receiver(pre_delete, sender=HomeImage)
def home_image_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

@receiver(pre_save, sender=HomeImage)
def home_image_update(sender, instance, **kwargs):
    update_image(sender, instance, **kwargs)

class Description(models.Model):
    text = models.TextField()

# about/gallery
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

@receiver(pre_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

@receiver(pre_save, sender=Photo)
def photo_update(sender, instance, **kwargs):
    update_image(sender, instance, **kwargs)


# Governance/management_teams
class ManagementTeam(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='management_team_images')
    position = models.CharField(max_length=100)

@receiver(pre_delete, sender=ManagementTeam)
def management_team_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

@receiver(pre_save, sender=ManagementTeam)
def management_team_update(sender, instance, **kwargs):
    update_image(sender, instance, **kwargs)

    def __str__(self):
        return self.name

# Governance/corporate_teams
class CorporateTeams(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='corporate_teams_image')
    position = models.CharField(max_length=100)
    
@receiver(pre_delete, sender=CorporateTeams)
def corporate_teams_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

@receiver(pre_save, sender=CorporateTeams)
def corporate_teams_update(sender, instance, **kwargs):
    update_image(sender, instance, **kwargs)

    def __str__(self):
        return self.name

# Committee
class Committee(models.Model):
    name = models.CharField(max_length=200)

@receiver(pre_delete, sender=Committee)
def committee_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

    def __str__(self):
        return self.name

# CommitteeMember
class CommitteeMember(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='committee_member_images')
    position = models.CharField(max_length=100)

@receiver(pre_delete, sender=CommitteeMember)
def committee_member_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

@receiver(pre_save, sender=CommitteeMember)
def committee_member_update(sender, instance, **kwargs):
    update_image(sender, instance, **kwargs)

    def __str__(self):
        return self.name

# BoardMember
class BoardMember(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='board_member_images')
    position = models.CharField(max_length=100)

@receiver(pre_delete, sender=BoardMember)
def board_member_delete(sender, instance, **kwargs):
    delete_image(instance, **kwargs)

@receiver(pre_save, sender=BoardMember)
def board_member_update(sender, instance, **kwargs):
    update_image(sender, instance, **kwargs)

    def __str__(self):
        return self.name




# services 

from django.db import models # type: ignore
from ckeditor.fields import RichTextField # type: ignore

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title
    
    
# Financial Highlights
class AnnualReport(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='annual_reports/')

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=AnnualReport)
def delete_annual_report(sender, instance, **kwargs):
    # Delete the file when the model instance is deleted
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
            

class QuarterlyReport(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='quarterly_reports/')

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=QuarterlyReport)
def delete_quarterly_report(sender, instance, **kwargs):
    # Delete the file when the model instance is deleted
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
            
class AGMMinutes(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='agm_minutes/')

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=AGMMinutes)
def delete_agm_minutes(sender, instance, **kwargs):
    # Delete the file when the model instance is deleted
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
            

class BaseRate(models.Model):
    month = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.month} {self.year}: {self.rate}%"

# Contact
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.address


# FAQS



# Notices
class Notice(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notices/')

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Notice)
def delete_notice(sender, instance, **kwargs):
    # Delete the file when the model instance is deleted
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question