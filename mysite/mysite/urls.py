from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, search_form, searchs, current_url, index, contact, foobar, my_view, archive, show
from django.contrib import admin
from mysite import show
from mysiteapp import dom,home
from django.conf import settings
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
	#('^$',index),
	('^hello/$',hello),
	('^time/$',current_datetime),
	('^another-time-page/$',current_datetime),
	(r'^time/plus/(\d{1,2})/$',hours_ahead),
	(r'^admin/', include(admin.site.urls)),
	(r'^search-form/$', search_form),
	(r'^search/$', searchs),
	(r'^current_url/$', current_url),
	#(r'^contact/$', contact),
	(r'^foo/$', foobar,{'template_name':'tem1.html'}),
	(r'^bar/$',foobar,{'template_name':'tem2.html'}),
	(r'^mydata/(?P<month>\w{3})/(?P<day>\d{1,2})/$', my_view),
	(r'^articles/(\d{4})/(\d{2})/(\d{2})/$', archive),
	#(r'^show/$', include(mysite.show.urls)),
	(r'^show/$',show.index),
	(r'^my_image/$',show.my_image),
	(r'^my_tran/$', show.my_tran),
	(r'^current_time/$', show.current_time),
	(r'^showbase/$', show.showbase),
	(r'^weatherinfo/$',show.weatherinfo),
	(r'^javaplayer/$', show.javaplayer),
	(r'^static/(?P<path>.*)$','django.views.static.serve',
	{'document_root':settings.STATIC_ROOT}),
	#(r'^img/(?P<path>.*)$','django.views.static.serve',
	#{'document_root':settings.IMG_ROOT}),
	#(r'^css/(?P<path>.*)$','django.views.static.serve',
	#{'document_root':settings.CSS_ROOT}),
	(r'^load_xml/$',dom.xml_to_data),
	(r'^$',home.index),
	#(r'^company/$',home.company),
	(r'^company/$',TemplateView.as_view(template_name="company.html")),
	(r'^news/$',home.news),
	(r'^business/$',home.business),
	(r'^hire/$',home.hire),
	(r'^culture/$',home.culture),
	(r'^contact/$',home.contact),
	(r'^news_detail/(\d+)/$',home.news_detail),
	(r'^item/$',home.item),
	(r'^vars/$',home.vars),
	(r'^sendmail_list/$',home.sendmail_list),
	(r'^send_email/$',home.send_email),
	(r'^django_email/$',home.django_email),
	#(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':mysiteapp.settings.STATICFILES_DIRS,'show_indexes':True}),

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
