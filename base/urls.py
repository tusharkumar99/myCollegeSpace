from django.contrib import admin
from django.urls import path, include
from .views import Login, Signup
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact' ),
    path('news/', views.news, name='news' ),
    path('entertainment/', views.entertainment, name='entertainment' ),
    path('portal/', views.portal, name='portal' ),
    path('notes/', views.notes, name='notes' ),
    path('ebooks/', views.ebooks, name='ebooks' ),
    path('research/', views.research, name='research' ),
    path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard")
]
