
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SignUpViewTests(TestCase):
    def test_successful_signup_creates_user_and_redirects(self):
        response = self.client.post(
            reverse('blog-sign-up'),
            {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password1': 'StrongPass123!',
                'password2': 'StrongPass123!',
            },
        )

        self.assertRedirects(response, reverse('blog-index'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_invalid_signup_renders_form_errors(self):
        response = self.client.post(
            reverse('blog-sign-up'),
            {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password1': 'StrongPass123!',
                'password2': 'Mismatch123!',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'errorlist')
        self.assertEqual(User.objects.count(), 0)