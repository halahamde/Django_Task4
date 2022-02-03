from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.template import context
from .models import myuser, students , Track
from .forms import Loginform, insertstudentForm , updatestudentForm , updatestudentForm2
from django.views import View
from django.views.generic import ListView,CreateView
from django.views.decorators.http import  require_http_methods,require_POST,require_GET
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def loginusertoadmin(request):
    context={}
    if(request.method=='GET'):
        return render(request, 'loginusertoadmin.html')
    else:
        username = request.POST['name']
        password = request.POST['password']
        #check cred in User
        authuser= authenticate(username=username,password=password)
        #check cred in myuser
        user=myuser.objects.filter(name=username,password=password)

        if(authuser is not None and user is not  None):
            request.session['username']=username
            login(request,authuser)
            return render(request,'home.html',context)
        else:
            context['errormsg'] = 'invlaid cred.'
            return render(request, 'loginusertoadmin.html', context)


def mylogout(request):
    request.session['username']=None
    return redirect('/affairs/loginusertoadmin')
        
def addusertoadmin(request):
    context={}
    if(request.method=='GET'):
        return render(request,'addusertoadmin.html',context)
    else:
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # add myuser
        myuser.objects.create(name=username,password=password)
        # add user
        User.objects.create_user(username=username,email=email,password=password)
        return render(request, 'loginusertoadmin.html', context)
    

class myuserList(ListView):
    model=myuser
    
class trackList(ListView):
    model=Track

    
def home(request):
    return render(request,'home.html')

def addStudent(request):
    context={}
    form=insertstudentForm()
    if (request.method == 'GET'):
        context['form']=form
        return render(request, 'addStudent.html',context)
    else:
        students.objects.create(name=request.POST['name'], track= request.POST['track'])
        student = students.objects.all()
        return redirect('/affairs/add', {'student': student})


class updateStudent(View):
    def get(self,request):
        context={}
        form=updatestudentForm2()
        #print('get class based')
        context['form']=form
        return render(request, 'updateStudent.html',context)
    def post(self,request):
        context={}
        form=updatestudentForm2()
        context['form']=form
        #print('post class based')
        stdid = request.POST['stdid']
        newname=request.POST['name']
        newtrack=request.POST['track']
    
        students.objects.filter(id=stdid).update(name=newname, track=newtrack)
        return render(request, 'updateStudent.html',context)

def deleteStudent(request):
    if (request.method == 'GET'):
        return render(request, 'deleteStudent.html')
    else:
        stdid = request.POST['stdid']
        students.objects.filter(id=stdid).delete()
        return render(request, 'deleteStudent.html')

def selectAll(request):
    context = {}
    context['studs'] = students.objects.all()
    return render(request, 'selectAll.html', context)

def search(request):
    if (request.method == 'GET'):
        return render(request, 'search.html')
    else:
        name = request.POST['name']
        context = {}
        context['studs'] = students.objects.filter(name__icontains=name)
        return render(request, 'search.html', context)