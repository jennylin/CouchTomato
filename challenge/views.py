# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core import serializers
from CouchTomato.craigSearch import CraigsSearch

def search(request, location, term):
    cs = CraigsSearch(term, location)
    results = cs.search()
    #return render_to_response('index.htm', serializers.serialize("json",results))
    return HttpResponse(serializers.serialize("json",results), mimetype="application/json")
def search_category(request, category, location, term):
    cs = CraigSearch(term, location)
    results = cs.searchCategory(category)
    #return render_to_response('index.htm', serializers.serialize("json",results))
    return HttpResponse(serializers.serialize("json",results), mimetype="application/json")