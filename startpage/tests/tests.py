from django.test import TestCase


class AnnoucementsTestCase(TestCase):

    def test_vanilla(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
