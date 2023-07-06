from django.contrib import admin
from .models import Images

# Register your models here.
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("id","image")
    
admin.site.register(Images, ImagesAdmin)
