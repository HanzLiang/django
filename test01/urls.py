"""test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

# 按照顺序进行匹配
urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/1', views.page1_view),
    path('page/2', views.page2_view),
    path('page/<int:pg>',views.pagen_view),
    path('<int:n>/<str:op>/<int:m>',views.page_calculate_view),
    path('request/', views.page_test_request),
    path('get/', views.test_get),
    path('html/', views.test_html),
    path('if/', views.test_if_for),
    path('mycal/', views.mycal),
    path('base/', views.base_view),
    # path('music/', views.music_view),
    path('sport/', views.sport_view),
    path('test_static/', views.test_static),
    path('music/', include('music.urls'))
]
