
import os
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from myapp.models import PersonalDetails,Textbooks
from myapp.forms import TextbookForm
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.conf import settings

# Create your views here.
def home(req):
      try:
        P=PersonalDetails.objects.get(user_id=req.user)
        return render(req,'home.html',{'ps':P})
      except:
        return render(req,'home.html')

def signup(req):
    if req.method=='POST':
         username=req.POST['uname']
         password=req.POST['psw1']
         psw2=req.POST['psw2']
         if password==psw2:
             u = User.objects.create_user(username=username,password=password)
             PersonalDetails.objects.create(user_id=u.id)
             return redirect(signin)
    else:
        return render(req,'signup.html')
         

def signin(req):
    if req.method=='POST':
         uname=req.POST['uname']
         psw=req.POST['psw']
         user=authenticate(username=uname,password=psw)
         if user:
           login(req,user)
           if req.POST['next']:
               return redirect(req.POST['next'])
           else:
               return redirect(home)
         else:
             return HttpResponse("ooooooooooo")
                 
    else:
        return render(req,'login.html')


def signout(req):
    logout(req)
    return redirect(home)


def userdetails(req):
    if req.method == 'POST':
      users=req.user
      users.first_name=req.POST['fname']
      users.last_name=req.POST['lname']
      users.username=req.POST['uname']
      users.email=req.POST['email']
      users.save()
      u=PersonalDetails.objects.get(user_id=users)
      u.city=req.POST['city']
      u.phone_number=req.POST['phone']
      u.date_of_birth=req.POST['dob']
      u.gender=req.POST['gender']
      u.save()
      try:
          u.image=req.FILES['file']
          u.save()
      except:
          pass 
    
      return render(req,'userdetails.html',{'ps':u})
    else:
         P=PersonalDetails.objects.get(user_id=req.user)
         return render(req,'userdetails.html',{'ps':P})
    

def class1(req):
       try:
          P=PersonalDetails.objects.get(user_id=req.user)
          return render(req,'class1.html',{'ps':P})
       except:
          return render(req, "class1.html")
       

def class2(req):
       
       t=Textbooks.objects.filter(classe=2)
       try:
          P=PersonalDetails.objects.get(user_id=req.user)
          return render(req,'class2.html',{'ps':P,'t':t})
       except:
          return render(req, "class2.html")


def raindrops(req):
      try:
        P=PersonalDetails.objects.get(user_id=req.user)
        return render(req,'raindrops.html',{'ps':P})
      except:
        return render(req, "raindrops.html")


def Marigold(req):
      try:
        P=PersonalDetails.objects.get(user_id=req.user)
        return render(req,'Marigold.html',{'ps':P})
      except:
        return render(req, "Marigold.html")


def Magic(req):
      try:
        P=PersonalDetails.objects.get(user_id=req.user)
        return render(req,'Magic.html',{'ps':P})
      except:
        return render(req, "Magic.html")


def एनसीईआरटीकक्षा१रिमझिम(req):
      try:
        P=PersonalDetails.objects.get(user_id=req.user)
        return render(req,'एन सी ई आर टी कक्षा १ रिमझिम.html',{'ps':P})
      except:
        return render(req, "एन सी ई आर टी कक्षा १ रिमझिम.html")



@login_required(login_url='/login')
def addbook(req):
    if req.method=='POST':
        Textbooks(classe=req.POST['class'],addedby=req.user,bookname=req.POST['textname'],book=req.FILES['file']).save()
    else:
        P=PersonalDetails.objects.get(user_id=req.user)
        return render(req,'addbooks.html',{'ps':P})
    


def classes(req):
       t=Textbooks.objects.all()
       try:
          P=PersonalDetails.objects.get(user_id=req.user)
          return render(req,'class.html',{'ps':P,'t':t})
       except:
          return render(req, "class.html")