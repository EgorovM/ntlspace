from django.shortcuts import render
from student.models import StudentProfile
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils import timezone
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.utils import timezone
from PIL      import Image
import datetime
import json
import StringIO
import threading

def index(request):
    return render(request,"main/index.html")
