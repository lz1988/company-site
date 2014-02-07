# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response,RequestContext
from mysiteapp.models import loftk_articles
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from mysiteapp.models import Book,Person,user,userrole
from mysiteapp import pub
from django.core.mail import send_mail,BadHeaderError


def index(request):
		item_list = loftk_articles.objects.order_by("-id")[:6]
		return render_to_response('index.html',{'item_list':item_list})

#def company(request):
		#return render_to_response('company.html')
		
def news(request):
		#articles = loftk_articles.objects.order_by('-id')
		#after_range_num = 5
		#before_range_num = 4
		#try:
                   # page = request.GET.get('page',1)
                    #if page < 1:
                    #    page = 1
		#except ValueError:
                   # page = 1
		#p = Paginator(articles,2)
		
		#try:
               #     articles = p.page(page)
		#except (EmptyPage,InvalidPage,PageNotAnInteger):
        #            contacts = p.page(p.num_pages)
		#if page <= after_range_num:
          #          page_range = p.page_range[page-after_range_num:page+before_range_num]
		#else:
                   # page_range = p.page_range[0:int(page)+before_range_num]
		item_list = loftk_articles.objects.order_by("-id")
		paginator = Paginator(item_list,2)
		p = request.GET.get('page','')
	 
		try:
			items = paginator.page(p)
		except PageNotAnInteger:
			items = paginator.page(1)
		except EmptyPage:
			items = paginator.page(paginator.num_pages)
				
		return render_to_response('news.html',{'record_list':items})
		
def business(request):
		return render_to_response('business.html')
		
def hire(request):
		return render_to_response('hire.html')
		
def culture(request):
		return render_to_response('culture.html')
	
def contact(request):
		return render_to_response('contact.html')

def news_detail(request, id):
		news_detail = loftk_articles.objects.get(id=int(id))
		return render_to_response('news_detail.html',{'news_detail':news_detail})
		
def test(request):
		return render_to_response('test.html')
		
def item(request):
		return render_to_response('test.html');
		
def vars(request):
		person = user.objects.filter(username='666')
		book = person[0].userrole_set.all()
		return render_to_response('vars.html',{'book':book})
		
def sendmail_list(request):
	return render_to_response('send_mail.html',dict,context_instance=RequestContext(request))

def send_email(request):
	if request.method == "POST":
		mailto_list = request.POST.get('shipto','')
		content = request.POST.get('content')
		content = list(content)
	#mailto_list=["513245459@qq.com","zhi.li@manshijian.com"]
	res = pub.send_emails(request,mailto_list,"subject",content)

	if res is True:
		mes = '发送成功'
	else:
		mes ='发送失败'
	return HttpResponse(mes)
	######################

""" @title dango发送邮件	
	@author lizhi
	@create on 2013-07-11 
"""
def django_email(request):
	msg = ''
	if request.method == "POST":
		if request.POST.get('submit',''):
			subject = request.POST.get('subject','')
			shipto = request.POST.get('shipto','')
			content = request.POST.get('content','')
			try:
					flag = send_mail(subject,content,'lz19881123@163.com',[shipto])
					if flag > 0:
						return HttpResponse('发送成功!')
					else:
						return HttpResonse('发送失败！')
			except:
				return HttpResponse('Invalid server error')
	
	return render_to_response('send_mail.html')
