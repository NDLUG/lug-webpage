from django.conf.urls import url

from voting import views


urlpatterns = [
    url(r"^", views.home, name='voting_home'),
]
