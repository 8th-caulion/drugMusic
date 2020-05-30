"""drugMusicProject URL Configuration

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
from django.conf import settings # 이거 추가
from django.conf.urls.static import static # 이거 추가
import drugMusicApp.views
import drugMusicApp.schedule

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', drugMusicApp.views.main, name="main"),
    path('profile/new', drugMusicApp.views.profileNew, name="profileNew"),
    path('profile/save', drugMusicApp.views.profileSave, name="profileSave"),
    path('schedule', drugMusicApp.views.schedule, name="schedule"),
    path('profile/', drugMusicApp.views.profile, name="profile"),
    path('profile/<int:id>', drugMusicApp.views.detailProfile, name="profile"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
