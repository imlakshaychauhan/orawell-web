from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# Create your views here
def index(request):
#     if user.request.is_anonymous:
#       return redirect("/login") 

    # messages.success(request,"This is success alert")
      return render(request, 'index.html')
      #return HttpResponse("Home")

def about(request):
      return render(request, 'about.html' )
     # return HttpResponse("about")

def contact(request):
      if request.method=="POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          desc = request.POST.get('desc')
          phone = request.POST.get('phone')
          contact=Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
          contact.save()
          messages.success(request, 'your message has been sent! We will contact you in next 24hrs')

      return render(request, 'contact.html' )
      # return HttpResponse("services")

def treatments(request):
      return render(request, 'treatments.html' )
     # return HttpResponse("about")

def loggedpage(request):
      # print(user.request)
      # if request.user.is_authenticated :  
      #     return redirect('/login')
      return render(request,'loggedpage.html')

def loginUser(request):
    if request.method=="POST":
       username = request.POST.get('username')    
       password = request.POST.get('password')    
       user = authenticate(username=username, password=password)
       print(username,password)

       if user is not None:
    # A backend authenticated the credentials
          return redirect('/loggedpage')
       else:
    # No backend authenticated the credentials
           return render(request, 'login.html' )

    return render(request, 'login.html' )

     # test user name:honey and password:honey@12345

#     return HttpResponse("LoginPage")  


def logoutUser(request):
      logout(request)
      return redirect("/login")
     # return HttpResponse("logout page")     
 
def findclinics(request):
      return render(request,'findclinics.html')

def findclinicsbylocation(request):
      return render(request, 'findclinicsbylocation.html')
      



def signupUser(request):
      if request.method == 'POST':
       firstName = request.POST.get('firstName')
       print('firstname = ',firstName)
       lastName = request.POST.get('lastName')
       username = request.POST.get('username')
       print('email = ',username)
       phone = request.POST.get('phone')
       print('phone',phone)
       pass1 = request.POST.get('pass1')
       print('password',pass1)
       pass2 = request.POST.get('pass2')
      # return render(request, 'signup.html')
           
           #check for errorneous inputs
           #

           #create the user
       
       myuser = User.objects.create_user( username ,pass1)
       myuser.first_name=firstName
       myuser.last_name=lastName
       myuser.save() 
       messages.success(request, 'Your Orawell account has been Successfully created')
       return redirect('/loggedpage')
      # else:
      #     return HttpResponse('Not allowed')

      return render(request, 'signup.html' ) 