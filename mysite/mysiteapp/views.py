# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime
from mysite.models import author
from mysite.forms import ContactForm
from urllib

def weatherinfo(request):
	page = urllib.urlopen("http://www.webxml.com.cn/webservices/weatherwebservice.asmx/getWeatherbyCityName?theCityName=青岛")
	body = page.readlines()
	page.close()
	for line in body:
		print line
