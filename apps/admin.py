from django.contrib import admin
from .models import student
from .models import mark

class studentadmin(admin.ModelAdmin):
    list_display = ('id','name','img','dob',)
    
admin.site.register(student,studentadmin)

class markadmin(admin.ModelAdmin):
    list_display = ('id','subject','mark','student1')

admin.site.register(mark,markadmin)   
# Register your models here.
