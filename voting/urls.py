from django.conf.urls import url

from secretballot import views as secretballot_views

from voting import views


urlpatterns = [
    url(r"^$", views.home, name='voting_home'),
    url(r"^vote/(?P<content_type>voting.VotingTopic)/(?P<object_id>[0-9]{0,4})/(?P<vote>-?1)/$", secretballot_views.vote, name='voting_vote'),
]
