from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name ="title"),
    path('wiki/?q=<str:title>',views.title, name = 'search')
]
