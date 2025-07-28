"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from solvexa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', auth, name='auth'),
    path('logout/', logout_user, name='logout_user'),
    # path('contact/', contact_form, name='contact_form'),
     # Include the messages view
    
    path('messages/', message, name='message'),
    path('mark-as-read/<int:pk>/', mark_as_read, name='mark_as_read'),
    path("__reload__/", include("django_browser_reload.urls")),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'solvexa.views.custom_404_view'


