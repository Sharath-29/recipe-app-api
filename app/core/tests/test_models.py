from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@sharath.com'
        password = 'abd123'
        user = get_user_model().objects.create_user(
            email = email,password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user us normalized"""
        email = 'test@SHARATH.COM'
        user = get_user_model().objects.create_user(email, 'abd123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abd123')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@sharath.com',
            'abd123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
