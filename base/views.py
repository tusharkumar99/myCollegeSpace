from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contacts, user, posts
from django.contrib.auth.hashers import make_password, check_password
from django.views import View



# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        message = request.POST.get('message','') 
        email = request.POST.get('email','')
        con = contacts(name=name, message=message, email=email)
        con.save()
        thank = True
        return render(request, 'base/contact.html', {'thank':thank})
    return render(request, 'base/contact.html')

def news(request):
    return render(request, 'base/news.html')

def entertainment(request):
    return render(request, 'base/entertainment.html')

def portal(request):
    if request.method == 'POST':
        name = request.session.get('name')
        post = request.POST.get('post','') 
        email = request.session.get('email')
        p = posts(name=name, email=email, post = post)
        p.save()
        all_posts = posts.objects.all()
        return render(request, 'base/portal.html',{'all_posts':all_posts})
    all_posts = posts.objects.all()
    return render(request, 'base/portal.html',{'all_posts':all_posts})

def notes(request):
    return render(request, 'base/notes.html')

def ebooks(request):
    return render(request, 'base/ebooks.html')

def research(request):
    return render(request, 'base/research.html')





# Sign Up/Log In
class Signup(View):
    def get(self, request):
        if not request.session.get('user'):
            return render(request, 'base/signup.html')
        else:
            return redirect('dashboard')

    def post(self, request):
       name = request.POST.get('name','')
       
       phone = request.POST.get('phone','') 
       email = request.POST.get('email','')
       password = request.POST.get('password','')
       repassword = request.POST.get('repassword','')

       u = user(name=name, email=email, phone=phone, password=password)

       values = {'name':name, 'phone':phone, 'email':email}

       error_message = None
       if len(phone)>10:
           error_message = "Please enter only 10 digits of your phone number"
       elif password!=repassword:
           error_message = "Your password doesn't match, enter again carefully"
       elif u.isExists():
           error_message = "Entered email address is already registered"
       
       if not error_message:
           u.password = make_password(u.password)
           u.save()
           thank = True
           return render(request, 'base/signup.html', {'thank':thank})
       else:
            return render(request, 'base/signup.html', {'error':error_message, 'values':values})       


class Login(View):
    def get(self, request):
        if not request.session.get('user'):
            return render(request, 'base/login.html')
        else:
            return redirect('dashboard')

    def post(self, request):
       email = request.POST.get('email','')
       password = request.POST.get('password','')
       try:
           u = user.objects.get(email=email)
       except:
           u = False
       error_message = None

       if u:
           flag = check_password(password, u.password)
           if flag:
               request.session['user'] = u.id   
               request.session['name'] = u.name 
               request.session['email'] = u.email 
               return redirect('home')
           else:
               error_message = "Invalid password"
       else:
           error_message = "Email not registered"

       return render(request, 'base/login.html', {'error':error_message, 'email':email})

def logout(request):
    request.session.clear()
    return redirect('home')

def dashboard(request):
    if request.session.get('user'):
        id = request.session.get('user')
        email = request.session.get('email')
        u = user.objects.filter(id=id)
        p = posts.objects.filter(email=email)
        return render(request, 'base/dashboard.html',{'u':u, 'p':p}) 
    else:
        return redirect('home')