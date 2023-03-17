from django.http import request
from django.shortcuts import render,HttpResponse
from django .contrib import messages
from . models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def indexland(request):
    return render(request,'index-landing.html')

# log_out
def logout(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'login.html',{'logger_data':logger_data})

# reg
def reg(request):
    return render(request,'reg.html')

# register_form_submission
def register_form_submission(request):
    if request.method=="POST":
        if register_table.objects.filter(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),password=request.POST.get('password')):
            messages.error(request,'Already this user name and password has taken',extra_tags='error')
            print("already register")
            return render(request,'reg.html')
        else:
            reg=register_table(first_name=request.POST.get('first_name'),
                               last_name=request.POST.get('last_name'),
                               password=request.POST.get('password'),
                               email=request.POST.get('email'),
                               phone=request.POST.get('phone'),
                               profile_picture=request.POST.get('profile_picture'))
            
            # if len(request.FILES)!=0:
            #     reg.profile_picture=request.FILES.get('profile_picture')
            reg.save()
            messages.error(request,'Registration successful !',extra_tags='reg')
            # ************* API SEND EMAIL ************
            try:
                first_name=request.POST.get('first_name')
                last_name=request.POST.get('last_name')
                email=request.POST.get('email')

                subject="Welcome to Medice Lab"
                message=f'Hi {first_name}{last_name} \n Your email is {email} \n Thank you for registering Medice Lab site.'
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[email, ]
                send_mail(subject, message, email_from, recipient_list)
                print("mail sent successfully")
                return render(request,'login.html')
            except:
                print("sorry mail not send properly ")
                return render(request,'login.html')   
    else:
        return render(request,'reg.html')

# login
def login(request):
    return render(request,'login.html')

# login_form_submisssion
def login_form_submission(request):
    if request.method=="POST":
        if register_table.objects.filter(first_name=request.POST.get('first_name'),
                                         last_name=request.POST.get('last_name'),
                                         password=request.POST.get('password')):
            print("login successful")
            logger_data=register_table.objects.get(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),password=request.POST.get('password'))
            return render(request,'index.html',{'logger_data':logger_data})
        else:
            print("invalid user name & password")
            messages.error(request,'Invalid user name & password',extra_tags='invalid')
            return render(request,'login.html')

# contact form submission

def contact_form_submission(request):
    contact=contact_table(name=request.POST.get('name'),
                              email=request.POST.get('email'),
                              subject=request.POST.get('subject'),
                              message=request.POST.get('message'),)
    contact.save()
    return HttpResponse(contact)