"""wikiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from entryapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('aws/', views.aws, name='aws'),
    path('linux/', views.linux, name='linux'),
    path('network/', views.network, name='network'),
    path('python/', views.python, name='python'),
    path('about/', views.about, name='about'),
]
