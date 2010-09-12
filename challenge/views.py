# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from CouchTomato.craigSearch import CraigsSearch
from django.views.decorators.cache import never_cache

def search(request, location):
    cs = CraigsSearch(request.POST['term'], location)
    results = cs.search()
    return HttpResponseRedirect(reverse('/', args=(results)))

def search_category(request, location, category):
    cs = CraigSearch(request.POST['term'], location)
    results = cs.searchCategory(category)
    return HttpResponseRedirect(reverse('/', args=(results)))
