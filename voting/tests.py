from django.test import TestCase
from django.contrib.auth.models import User

from voting.models import VotingTopic


class VotingClientTestCase(TestCase):
    def test_vanilla(self):
        c = self.client
        r = c.get('/voting/')
        self.assertEqual(200, r.status_code)

    def test_voting_topic_listed_on_page(self):
        c = self.client
        vt = VotingTopic(title='My cool topic')
        vt.save()
        r = c.get('/voting/')
        self.assertContains(r, vt.title)


class VotingUnitTestCase(TestCase):
    def test_can_vote_on_vote_topic_model(self):
        u = User(username='bob', password='dylan')
        u.save()
        vt = VotingTopic(title='My cool topic')
        vt.save()
        vt.add_vote('1.1.1.1', 1)
        vt_with_votes = VotingTopic.objects.get(pk=vt.pk)
        self.assertEqual(vt_with_votes.vote_total, 1)
