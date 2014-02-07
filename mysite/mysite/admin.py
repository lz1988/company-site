#filename admin.py
from django.contrib import admin
from mysite.models import author

class authorAdmin(admin.ModelAdmin):
	list_display  = ('name', 'address')
	search_fields = ('name', 'address')
	fields = ('name', 'address')

admin.site.register(author,authorAdmin)