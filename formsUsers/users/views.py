from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def list_users(request):
    return render(request, 'main.html', context={
        'title': 'List users'
    })
