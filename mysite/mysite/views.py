#filename views.py
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime
from mysite.models import author
from mysite.forms import ContactForm


def index(request):
	return render_to_response('index.html')
	
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    #html = "<html><body> It is now %s.</body></html>" % now
    html = t.render(Context({'current_datetime': now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
	raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
	
def search_form(request):
	return render_to_response('search_form.html')
	
def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		authors = author.objects.filter(name__icontains=q)
		return render_to_response('search_results.html',{'mysite':authors, 'query':q})
		
		#message = 'You searched for:%s' % request.GET['q']
	else:
		#message = 'You submitted an empty form.'
		return render_to_response('search_form.html', {'error':True})

def searchs(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 8:
			errors.append('Please enter at most 8 characters.')
		else:
			authors = author.objects.filter(name__icontains=q)
			return render_to_response('search_results.html',{'mysite':authors, 'query':q})
	return render_to_response('search_form.html',{'errors':errors})
	
def current_url(request):
	return HttpResponse("welcome to page %s" % request.path)
	
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
	else:
		form = ContactForm(
			initial = {'name':'I LOVE YOU'}
		)
	return render_to_response('contact_form.html', {'form':form})
	
def foobar(request, template_name):
	m_list = author.objects.filter(name=True)
	m_list = [1,2]
	return render_to_response(template_name,{'m_list':m_list})
	
def my_view(request, month, day):
	myvar = 'wel come %s %s' % (month, day)
	#return render_to_response('my_view.html',{'myvar':myvar})
	return HttpResponse(myvar)
	
def archive(request, year, month, day):
	date = datetime.date(int(year), int(month), int(day))
	return HttpResponse(date)
	
def show(request):
	return HttpResponse('ssssssssss')
