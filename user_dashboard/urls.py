"""user_dashboard URL Configuration

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
from django.contrib import admin
from django.urls import path
from user.urls import urlpatterns as user_urls
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^dashboard/', include((user_urls, 'dashboard'), namespace='dashboard')),
]

if settings.DEBUG:
    urlpatterns += [
        # static files (images, css, javascript, etc.)
        url(r'^static/(?P<path>.*)$', serve)] + static(
            '/media/', document_root=settings.MEDIA_ROOT)