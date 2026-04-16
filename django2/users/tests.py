from django.test import TestCase
from django.conf import settings


User = settings.AUTH_USER_MODEL

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email = 'test@test.com',
            nickname = 'test',
        )

    def test_user_manager_create_user(self):
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.nickname, 'test')

    def test_user_manager_create_superuser(self):
        superuser = User.objects.create_superuser(
            email = 'admin@test.com',
            nickname = 'admin',
        )
        self.assertEqual(superuser.email, 'admin@test.com')
        self.assertEqual(superuser.nickname, 'admin')
        self.assertEqual(superuser.is_admin, True)
        self.assertEqual(superuser.is_superuser, True)