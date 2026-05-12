from django.contrib import admin
from model.models import watchesdata1 

class watchesdata(admin.ModelAdmin):
    list_display = ('image' , 'title' , 'company' , 'model' , 'machine' , 'price')

admin.site.register(watchesdata1 , watchesdata)