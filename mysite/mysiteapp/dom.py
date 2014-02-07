#filename dom.py
# -*- coding:utf-8 -*-
from  xml.dom import  minidom
from django.http import HttpResponse, Http404

def xml_to_data(request, filename='F:/Django-1.5.1/mysite/mysiteapp/static/xml/demo.xml'):
	doc = minidom.parse(filename)
	return HttpResponse(filename)