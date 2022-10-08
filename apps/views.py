from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from apps.models import student
from apps.form import studentform
from apps.models import mark
from apps.form import markform




def user_login(request): 
    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('listview')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login')
    else:     
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
        
def user_logout(request):
    logout(request)
    return redirect('/apps')



def jsondata(request):
    import json
    data = student.objects.all().values()
    l = []
    for i in data:
        l.append(i)
    res = json.dumps(l, default = str, indent = 4)
    print(res)
    print(type(res))
    return HttpResponse(res,content_type='application/json')



def json(request):
    data = list(mark.objects.values())
    return JsonResponse(data,safe = False)



@login_required(redirect_field_name='/apps/markadd', login_url='/apps')
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
        
@login_required(redirect_field_name='/apps/listview', login_url='/apps')    
def list_view(request):
    item = student.objects.all()
    return render(request,'stable.html',{'item':item})


def detail_view(request,id):
    item =mark.objects.filter(student1_id = id).values()
    return render(request,'markview.html',{'item':item})
    
    
    
def mark_add(request):
    form = markform(request.POST or None, request.FILES or None)
    if form.is_valid():
       f = form.save(commit = False)
       f.create_name = (request.user).username
       form.save()
    return render(request,'markadd.html',{'form':form})
    
    
def mark_update(request,id):
    item =mark.objects.get(id = id)
    form = markform(request.POST or None, request.FILES or None , instance = item)
    if form.is_valid():
       f = form.save(commit = False)
       f.modify_name = (request.user).username
       form.save()
    return render(request,'markupdate.html',{'form':form})
        
def mark_delete(request,id):
    item =mark.objects.get(id = id)
    item.delete()
    return render(request,'markview.html')
    
   
    
# Create your views here.
