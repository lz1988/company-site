#filename admin.py
from django.contrib import admin
from mysiteapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'address','enname')
	search_fields = ('name', 'address')
	fields = ('name', 'address','enname')

admin.site.register(Author, AuthorAdmin)