import sys

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseServerError, \
    HttpResponseForbidden
from django.shortcuts import render, redirect
from django.template.defaulttags import lorem
from django.views.generic import ListView

from blog.models import Post
from newsAPI import settings


def index(request):
    # from faker import Faker

    # fake = Faker(locale='uk_UA')
    # posts = ['post1', 'post2', 'post3', 'post4', 'post5', 'post6']

    # list_posts = [{'title': post.capitalize(),
    #                'data': fake.date_time(),
    #                'body': fake.text(200)} for post in posts]

    api_key = settings.NEWS_API_KEY  # оголосіть у .env
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    resp = requests.get(url).json()

    print(resp)

    list_posts = resp.get('articles', [])
    context = {
        'posts': list_posts
    }
    return render(request, 'blog/index.html', context)

# class NewsListView(LoginRequiredMixin, ListView):
# 	template_name = 'index.html'
# 	context_object_name = 'articles'
#
# 	def get_queryset(self):
# 		api_key = settings.NEWS_API_KEY  # оголосіть у .env
# 		url = f'https://newsapi.org/v2/top-headlines?country=ua&apiKey={api_key}'
# 		resp = requests.get(url).json()
# 		return resp.get('articles', [])


def archive(request, year):
    if int(year) > 2025:
        # raise Http404() # відображення сторінки з кодом 404 (функція page_not_found(request, exception))
        # return redirect('posts') # редірект з кодом 302 - url змінився тимчасово
        return redirect('home', permanent=True) # редірект з кодом 301 - постійний url permanent=True

    return HttpResponse(f'<h1>Архів за {year} рік</h1>')



def page_not_found(request, exception):
    """ Відображення сторінки 404 """
    return HttpResponseNotFound(f'<h1>Page not found</h1><p>Error: 404</p>')
    # return HttpResponseBadRequest(f'<h1>Bad Request</h1>', status=400)
    # return HttpResponseServerError(str(exception))
    # return HttpResponseForbidden(f'<h1>Доступ заборонений</h1><p>{exception}</p>')