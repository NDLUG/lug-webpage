"""ndlug URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from registration.backends.simple.views import RegistrationView

from ann import views

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/'

urlpatterns = [
    url(r"^announcements/", include("announcements.urls")),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',  # needed to overwrite normal redirect
        MyRegistrationView.as_view(),
        name='registration_register',
        ),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
