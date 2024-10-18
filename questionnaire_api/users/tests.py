from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


class UserAPITestCase(APITestCase):
    def test_get_all_users(self):
        url = reverse('users-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), list)

    def test_get_a_user(self):
        user = User.objects.create(
            firstname="test firstname",
            lastname="test lastname"
        )
        url = reverse('users-detail', kwargs={'pk':user.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_a_non_exsitent_user(self):
        url = reverse('users-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_a_user(self):
        url = reverse('users-list')
        data = {
            "firstname": "test firstname",
            "lastname": "test lastname"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(User.objects.filter(id=response.json()['id']).first())

    def test_update_a_user(self):
        user = User.objects.create(
            firstname="test firstname",
            lastname="test lastname"
        )
        self.assertEqual(User.objects.all().count(), 1)

        url = reverse('users-detail', kwargs={'pk': user.id})
        data = {
            "firstname": "updated test firstname",
            "lastname": "updated test lastname"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.first().firstname, data['firstname'])
        self.assertEqual(User.objects.first().lastname, data['lastname'])

    def test_update_a_non_existent_user(self):
        url = reverse('users-detail', kwargs={'pk': 1})
        data = {
            "firstname": "updated test firstname",
            "lastname": "updated test lastname"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_a_exsitent_user(self):
        user = User.objects.create(
            firstname="test firstname",
            lastname="test lastname"
        )
        self.assertEqual(User.objects.all().count(), 1)

        url = reverse('users-detail', kwargs={'pk': user.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)

    def test_delete_a_non_exsitent_user(self):
        url = reverse('users-detail', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
