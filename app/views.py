from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import movies,tv

def home(request):
    """Renders the home page."""
    movie = movies.objects.all()
    context={'movie':movie}
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def support(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def tv_page(request):
    tvs = tv.objects.all()
    context={'tvs':tvs}
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tv_page.html',
         context,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )