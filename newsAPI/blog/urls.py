from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('cats/<slug:cat_slug>/', NewsCategory.as_view(), name='posts_by_category'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
]