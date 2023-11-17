# Installs phonenumbers minimal metadata
# pip install "django-phonenumber-field[phonenumberslite]"

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .models import Post, Comment
from cloudinary.models import CloudinaryField

BUSINESS_SECTOR_CHOICES = (
    ('other', 'Other...'),
    ('accounting', 'Accounting'),
    ('analytics', 'Analytics & Market Research'),
    ('construction', 'Construction'),
    ('education', 'Education'),
    ('energy', 'Oil, Gas & Electricity'),
    ('energy_renewable', 'Renewable Energy'),
    ('engineering', 'Engineering'),
    ('estate_agent', 'Estate Agency'),
    ('entrepreneur', 'Entrepreneur'),
    ('finance', 'Finance'),
    ('food', 'Food Production'),
    ('health_care', 'Health Care'),
    ('hospitality', 'Hospitality'),
    ('insurance', 'Insurance'),
    ('law', 'Law'),
    ('logistics', 'Transport & Logistics'),
    ('management', 'Management'),
    ('manufacturing', 'Manufacturing'),
    ('marketing', 'Marketing'),
    ('management_consulting', 'Management Consulting'),
    ('recruitment', 'Recruitment Agency'),
    ('retail', 'Retail'),
    ('technology', 'Technology'),
    ('telecomms', 'IT & Telecommunication'),
    ('warehouse', 'Warehousing & Operations'),
)


class CustomUser(AbstractUser):
    contact_number = PhoneNumberField(unique=True, region='GB')

# Settings.py
# AUTH_USER_MODEL = 'accounts.CustomUser'

# https://www.youtube.com/watch?v=Pz1IedwX06E sets national GB
# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models


class UserProfile(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, related_name="users_details")
    slug = models.SlugField(max_length=200, unique=True)
    business_sector = models.CharField(max_length=50, choices=BUSINESS_SECTOR_CHOICES, default='other')
    company_name = models.CharField(max_length=100)
    comapny_website = models.URLField(max_length=200)
    company_contact_number = PhoneNumberField(unique=True, region='GB')
    company_contact_email = models.EmailField(unique=True)
    company_bio = models.TextField()
    # cloudinary is image only, what should i use here or is this stored in DB?
    company_brochure_upload = CloudinaryField('image', default='placeholder')
    company_services_post = models.TextField()
    company_hero_picture = CloudinaryField('image', default='placeholder')
    user_contact_number = models.ForeignKey(CustomUser.contact_number, on_delete=models.CASCADE, related_name="users_contact_number")
    display_user_email = models.BooleanField(default=True)
    user_about = models.TextField()
    user_avatar = CloudinaryField('image', default='placeholder')
    users_posts = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="users_posts"
    )


    def __str__(self):
        # just unsure what the string is needed for at the moment
        return f'{ self.user.username }: { self.company_name }'
