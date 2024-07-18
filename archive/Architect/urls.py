from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('home/', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('deconnexion/', views.deconnexion, name='deconnexion')
]