from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
# Create your views here.
def index(request):
  template = loader.get_template('compselector/index.html')
  context = RequestContext(request, {
#    'path' : request.path.split('/')[-2],
  })
  return HttpResponse(template.render(context))