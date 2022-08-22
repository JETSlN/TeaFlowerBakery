from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    return render(request, 'homepage/index.html')

def story(request):
    return render(request, 'homepage/story.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_tel = request.POST['message-tel']
        message = request.POST['message']
        context = {
            'message_name': message_name,
            'message_email': message_email,
            'message_tel': message_tel,
            'message': message,
        }

        send_mail(
            message_name, # subject
            message + "\n Phone Number: " + message_tel + '\n' + "Email: " + 
            message_email, # message
            message_email, # from email
            ['teaflowerbakery@gmail.com'], # to email

        )
        return render(request, 'homepage/contact.html', context)
    else:
        return render(request, 'homepage/contact.html')

def bread(request):
    return render(request, 'homepage/bread.html')

def drink(request):
    return render(request, 'homepage/drink.html')

def cookie(request):
    return render(request, 'homepage/cookie.html')

def loave(request):
    return render(request, 'homepage/loave.html')

def pastry(request):
    return render(request, 'homepage/pastry.html')

def cake(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_tel = request.POST['message-tel']
        message = request.POST['message']
        context = {
            'message_name': message_name,
            'message_email': message_email,
            'message_tel': message_tel,
            'message': message,
        }

        send_mail(
            message_name, # subject
            message + "\n Phone Number: " + message_tel + '\n' + "Email: " + 
            message_email, # message
            message_email, # from email
            ['teaflowerbakery@gmail.com'], # to email

        )
        return render(request, 'homepage/cake.html')
    else:
        return render(request, 'homepage/cake.html')
    