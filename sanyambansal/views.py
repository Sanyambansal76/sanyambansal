from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home_page(request):
    context = {}
    return render_to_response("home.html", context ,context_instance=RequestContext(request))
