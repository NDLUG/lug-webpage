from __future__ import unicode_literals

from django.db import models

import secretballot


class VotingTopic(models.Model):
    title = models.CharField(max_length=100)


secretballot.enable_voting_on(VotingTopic)
