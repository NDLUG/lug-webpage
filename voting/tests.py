from random import random

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

    def test_vote_topics_appear_with_number_of_votes(self):
        c = self.client
        topics = [VotingTopic(title='Topic ' + str(i)) for i in xrange(0, 5)]
        # Add votes
        for i, t in enumerate(topics):
            t.save()
            for j in xrange(0, i):
                t.add_vote(random(), 1)

        # Get votes
        topics = [VotingTopic.objects.get(pk=t.pk) for t in topics]
        r = c.get('/voting/')
        for t in topics:
            self.assertContains(
                r,
                "{title}: {v_count}".format(
                    title=t.title,
                    v_count=t.vote_total,
                ),
            )

    def test_can_vote_via_request(self):
        c = self.client
        vt = VotingTopic()
        vt.save()
        r = c.get(
            '/voting/vote/voting.VotingTopic/' + str(vt.id) + '/1/',
            {
                'content_type': 'VotingTopic',
                'object_id': vt.id,
                'vote': 1,
            }
        )
        self.assertEqual(r.status_code, 200)
        vt = VotingTopic.objects.get(pk=vt.pk)
        self.assertEqual(vt.vote_total, 1)


class VotingUnitTestCase(TestCase):
    def test_can_vote_on_vote_topic_model(self):
        vt = VotingTopic(title='My cool topic')
        vt.save()
        vt.add_vote('1.1.1.1', 1)
        vt_with_votes = VotingTopic.objects.get(pk=vt.pk)
        self.assertEqual(vt_with_votes.vote_total, 1)
