from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.constraints import Deferrable
from django.db.models.fields.related import ForeignKey
from .managers import UserManager
from django.utils import timezone, tree
from django.core.validators import RegexValidator


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        "Email Address",
        max_length=255,
        unique=True,
        error_messages={'unique': ("A user with that Email address already exists")})

    phone_regex = RegexValidator(regex=r"^(?:[0-9]●?){6,14}[0-9]$", message=(
        "Enter a valid international mobile phone number "))

    mob_number = models.CharField(
        "Phone Number ",
        validators=[phone_regex],
        max_length=20,
        unique=True,
        error_messages={'unique': (
            "A user with that phone number address already exists")},
        null=True, blank=True)
    first_name = models.CharField("First Name", max_length=300, )
    last_name = models.CharField("Last Name", max_length=300, )
    is_active = models.BooleanField(default=True)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)  # a superuser
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mob_number']

    class Meta:
        ordering = ['email']
        verbose_name = ('User Profile')
        verbose_name_plural = ('Users Profile')

    #if we want send a mail to user when user is create 
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        send email to this user
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
