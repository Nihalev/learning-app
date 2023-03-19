
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(req):
    return render(req,'home.html')



def class1(req):
      pdf_url = "static\1678883530925-01.jpeg"
      return render(req, "class1.html", {"pdf_url": pdf_url})






def signup(req):
    if req.method=='POST':
         fname=req.POST['fname']
         lname=req.POST['lname']
         username=req.POST['uname']
         password=req.POST['psw1']
         psw2=req.POST['psw2']
         email=req.POST['email']
         if password==psw2:
             User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
             return redirect(signin)
    else:
        return render(req,'signup.html')
         





def signin(req):
    if req.method=='POST':
         uname=req.POST['uname']
         psw=req.POST['psw']
         user=authenticate(username=uname,password=psw)
         if user is not None:
           login(req,user)
           return redirect(home)
         else:
             return HttpResponse("ooooooooooo")
                 
    else:
        return render(req,'login.html')



def signout(req):
    logout(req)
    return redirect(home)



