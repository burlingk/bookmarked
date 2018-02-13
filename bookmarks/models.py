from django.db import models
from django.conf import settings

# Create your models here.
class Bookmark(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Who owns the object
	url = models.SlugField(max_length=100, unique=True)                             # 
	slug = models.SlugField(max_length=100)
	site = models.CharField(max_length=2000)
	
	
	def save(self, *args, **kwargs):
		self.slug = self.url.lower();
		super().save(*args, **kwargs)
	
	def __str__(self):
		return '%s: %s' % (self.url, self.site)
	
	def get_absolute_url(self):
		return '/%s' % self.url
	
	#@property
	#def slug(self):
	#	return '%s' % self.url
	
	
	
	
	
	
	