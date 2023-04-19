from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
admin.site.register(myLoginDetials)
admin.site.register(myUserDetials)
admin.site.register(myscreenshot)