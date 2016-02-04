from __future__ import unicode_literals

from django.db import models

import secretballot


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


secretballot.enable_voting_on(Topic)
