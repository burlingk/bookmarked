from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import PermissionsMixin




# Create your models here.
class CustomUserManager(BaseUserManager):
	
	def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_user(self, email, password=None, **extra_fields):
		return self._create_user(email, password, False, False, **extra_fields)
	
	def create_superuser(self, email, password, **extra_fields):
		return self._create_user(email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
	#class CustomUser(AbstractBaseUser):
	"""
	A User Model that uses the email address as the login.
	"""
	
	#TODO: Consider adding help_text=_('...') options to some of the fields.
	email = models.EmailField(_('email address'), max_length=160, unique=True)
	is_staff = models.BooleanField(_('staff status'), default=False)
	is_admin = models.BooleanField(_('Admin status'), default=False)
	is_active = models.BooleanField(_('active'), default=True)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	is_verified = models.BooleanField(_('verified'),default=False)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	objects = CustomUserManager()
		
	#get_full_name and get_short_name are here because they are required by the auth system.
	#I'm not collecting information that means anything in that context in the user object,
	#so, they are just returning the "username," which is the email address.
	def get_full_name(self):
		return email
	
	def get_short_name(self):
		return self.email
	
	def __str__(self):
		return self.email
	
	def email_user(self, subject, message, from_email=None):
		"""
		Send an email to this user.
		"""
		send_mail(subject, message, from_email, [self.email])
	
	def natural_key(self):
		return self.email;


	
	
		
		
	
