from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from collections import Counter
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.utils import timezone

# Create your views here.


# Process and redirect login form data
# @login_required(login_url="/accounts/login")
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

