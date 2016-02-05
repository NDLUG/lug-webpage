from django.shortcuts import render_to_response
from django.template import RequestContext

from voting.models import Topic


def index(request):
    context = {}
    context['main_topic'] = Topic.objects.all()[0]
    return render_to_response(
        'voting/index.html',
        context=context,
        context_instance=RequestContext(request)
    )
