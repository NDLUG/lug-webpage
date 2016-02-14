from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase


class EmailTestCase(TestCase):
    def test_send_email(self):
        mail.send_mail(
            'Subject',
            'message',
            'from@gmail.com',
            ['test@gmail.com'],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)


class RegistrationClientTestCase(TestCase):
    def create_new_user(self):
        self.username = 'jim'
        self.email = 'jim@gmail.com'
        self.password2 = self.password1 = 'superdupersecretpassword'
        self.client.post(
            self.url,
            {
                'username': self.username,
                'email': self.email,
                'password1': self.password1,
                'password2': self.password2,
            }
        )

    def setUp(self):
        self.url = '/accounts/register/'

    def test_register_page_loads(self):
        r = self.client.get(self.url)
        self.assertEqual(r.status_code, 200)

    def test_can_create_new_user(self):
        self.assertEqual(len(User.objects.all()), 0)
        self.create_new_user()
        self.assertEqual(len(User.objects.all()), 1)

    def test_newly_created_user_is_automatically_logged_in(self):
        # Make sure no one is logged in
        self.assertNotIn('_auth_user_id', self.client.session)
        self.create_new_user()
        self.assertIn('_auth_user_id', self.client.session)
