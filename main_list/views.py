from django.shortcuts import render
from pip._vendor import requests
from main_list.models import Blog
from django.utils import timezone
from datetime import date

def main_list(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    variable = str(date.today().month) + '/' + str(date.today().day)
    api_url = 'http://numbersapi.com/' + variable
    params = {
        'type': 'date',
        'json': True
    }
    res = requests.get(api_url, params=params).json()
    return render(request, 'main_list.html', {'blogs': blogs, 'res': res, 'date': date.today()})
