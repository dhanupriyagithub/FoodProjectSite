from django.contrib import admin

from django.utils.html import format_html
from productapp.models import DemoModel

from django.contrib.admin.views.main import ChangeList

class CustomChangeList(ChangeList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Food Products"

class DemoModelCustomAdmin(admin.ModelAdmin):
    list_display=("Title","image1","Price","Description","Availability")
    search_fields = ("Title","image1","Price","Description","Availability")
    
    def image1(self, obj):
        return format_html('<img src="{0}" width="auto" height="150px">'.format(obj.Image.url))

    def formatted_price(self, obj):
         return format_html("${:.2f}".format(obj.Price))
    
    def get_changelist(self, request, **kwargs):
        return CustomChangeList
    

admin.site.register(DemoModel,DemoModelCustomAdmin)
