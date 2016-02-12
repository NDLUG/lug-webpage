from django.test import TestCase

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
