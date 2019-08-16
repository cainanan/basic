from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'content':"<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
