import sys

import requests
from django.http import HttpResponseNotFound, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseServerError, \
    HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.models import Post
from newsAPI import settings


CATEGORY_CHOICES = [
    'business',
    'entertainment',
    'education',
    'health',
    'sports',
    'technology',
    'travel',
    'general',
]


class NewsListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # paginate_by = 10

    def get_queryset(self):
        # print(self.qwargs['cat_slug'])
        api_key = settings.NEWS_API_KEY # оголосіть у .env
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
        resp = requests.get(url).json()

        return resp.get('articles', [])

    def get_context_data(self, *, object_list =None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NewsAPI'
        context['category'] = CATEGORY_CHOICES
        return context


def posts_by_category(request, category):
    return HttpResponse(f'category: {category}')


class AddPostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'



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