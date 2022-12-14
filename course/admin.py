from django.contrib import admin
from .models import Course,Students,Instractor
# Register your models here.
admin.site.site_header='Course Registration'
admin.site.site_title='Course Registration'
admin.site.index_title='Course Registration'
class ModelAdmin(admin.ModelAdmin):
    list_display=['course_title','instractor_name','capacity','open_seats']
    list_filter=['course_title','instractor_name']
    search_fields=['course_title','instractor_name']
    list_per_page=10
    
admin.site.register(Course,ModelAdmin)
admin.site.register(Students)
admin.site.register(Instractor)
