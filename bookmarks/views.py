from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound

from django.http.response import HttpResponseRedirect


from .models import Bookmark


# Create your views here.

def go_to_site(request, site_slug):
		if Bookmark.objects.filter(slug=site_slug.lower()).exists():
			site = Bookmark.objects.get(slug=site_slug.lower())
			return HttpResponseRedirect(site.site)
			#return redirect(site.site)
		else:
			return  HttpResponseNotFound('<h1>The site ('+site_slug+') is not in our database!</h1>')

def index_view(request):
	bookmarks = Bookmark.objects.all()
	return render(request, 'core/index.html', {'bookmarks':bookmarks})





