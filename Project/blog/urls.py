"""blog app URL configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [

    path('', PostListView.as_view(), name = "blog-page"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "post_detail-page"),
    path('post/new/', PostCreateView.as_view(), name = "create_post-page"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="update_post-page"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="delete_post-page"),
]
