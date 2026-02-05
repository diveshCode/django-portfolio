from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import request, HttpResponse
from django.conf import settings
from django.contrib import messages
from templates import *
from .models import Project
# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')


def projects_view(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            send_mail(
                subject=f"New contact from {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            print("Email sending failed:", e)

    return render(request, "portfolio/contact.html")