"""color_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from colors.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('color', FavoriteColorView.as_view()),
    # path('get_cookie', get_cookie_data , name='get_cookie'),
    # path('set_cookie', set_cookie_data , name='set_cookie'),
    # path("anony_user", MyViewAnony.as_view(), name='anony_user'),
    # path("logged_user", MyViewAuth.as_view(), name='logged_user'),

    path("get-book/", book_list),
    path("get-author", author_list)
]
