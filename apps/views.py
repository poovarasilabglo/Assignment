from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from apps.models import student
from apps.form import studentform
import datetime
from apps.models import mark
from apps.form import markform
import random

def student_add(request):
    form = studentform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    else:
     	print("its not valid")
    return render(request,'form.html',{'form':form})
    

def student_update(request,id):
    item =student.objects.get(id = id)
    form = studentform(request.POST or None, request.FILES or None , instance = item)
    if form.is_valid():
       form.save()
    return render(request,'studentupdate.html',{'form':form})
               

def student_delete(request,id):
    item =student.objects.get(id = id)
    item.delete()
    return render(request,'del.html')
        
    
def list_view(request):
    item = student.objects.all()
    return render(request,'stable.html',{'item':item})


def detail_view(request,id):
    item =mark.objects.filter(student1_id = id).values()
    return render(request,'markview.html',{'item':item})
    
    
    
def mark_add(request):
    form = markform(request.POST or None, request.FILES or None)
    if form.is_valid():
       form.save()
    return render(request,'markadd.html',{'form':form})
    
    
def mark_update(request,id):
    item =mark.objects.get(id = id)
    form = markform(request.POST or None, request.FILES or None , instance = item)
    if form.is_valid():
       form.save()
    return render(request,'markupdate.html',{'form':form})
        
def mark_delete(request,id):
    item =mark.objects.get(id = id)
    item.delete()
    return render(request,'markview.html')
    
   
    
# Create your views here.
