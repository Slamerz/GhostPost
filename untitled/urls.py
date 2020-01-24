"""untitled URL Configuration

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
from Ghost_Post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_details, name="postDetails"),
    path('post/<int:post_id>/up_vote/', views.post_upVote, name="upVote"),
    path('post/<int:post_id>/down_vote/', views.post_downVote, name="downVote"),
    path('post/new/', views.post_new, name="postNew"),
    path('create/', views.post_create, name="createPost")
]
