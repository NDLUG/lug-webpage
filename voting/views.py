from django.shortcuts import render_to_response
from django.template import RequestContext

from voting.models import VotingTopic


def home(request):
    topics = VotingTopic.objects.all()
    context = {'topics': topics}
    return render_to_response(
        'voting/index.html',
        context,
        context_instance=RequestContext(request),
    )
