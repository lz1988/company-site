#filename show.py
#coding:utf-8
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime
from django.utils.translation import ugettext
import urllib
from xml.dom import minidom


def index(request):
	return HttpResponse('this is show')
	
def my_image(request):
	image_data = open("F:/Django-1.5.1/mysite/mysite/2000.jpg","rb").read()
	return HttpResponse(image_data,mimetype="image/jpg")
	
def my_tran(request):
	output = ugettext("Welcome to my site.")
	return HttpResponse(output)

def current_time(request):
	now = datetime.datetime.now()
	t = get_template('current_time.html')
	html = t.render(Context({'currxent_time':now}))
	#return HttpResponse(html)
	return render_to_response('current_time.html',{'current_time':now})

def showbase(request):
	return render_to_response('show.html',{'current_time':datetime.datetime.now()})

def weatherinfo(request):
	page = urllib.urlopen("http://www.webxml.com.cn/webservices/weatherwebservice.asmx/getWeatherbyCityName?theCityName=武汉")
	body = page.readlines()
	page.close()
	return HttpResponse(body)
	#return render_to_response('weather.html',{'data': body})

def javaplayer(request):
	return render_to_response('javaplayer.html')