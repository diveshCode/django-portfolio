from utils.send_email import send_contact_email
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

from django.shortcuts import render

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email_sent = send_contact_email(name, email, message)

        if email_sent:
            messages.success(request, "Your message has been sent successfully!")
            return render(request, "portfolio/contact.html", {"success": True})
        else:
            messages.error(request, "Failed to send your message.")
            return render(request, "portfolio/contact.html", {"error": True})

    return render(request, "portfolio/contact.html")