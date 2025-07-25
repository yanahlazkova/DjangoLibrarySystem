from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def books(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def add_books(request):
    template = loader.get_template('add_books.html')
    return HttpResponse(template.render())
