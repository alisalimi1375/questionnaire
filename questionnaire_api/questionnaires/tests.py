from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Questionnaire


class QuestionnaireAPITestCase(APITestCase):
    def test_get_all_questionnaires(self):
        url = reverse('questionnaires-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), list)
    
    def test_get_a_questionnaire(self):
        questionnaire = Questionnaire.objects.create(
            title="test title",
            description="test description"
        )
        url = reverse('questionnaires-detail', kwargs={'pk':questionnaire.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_a_non_exsitent_questionnaire(self):
        url = reverse('questionnaires-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_a_questionnaire(self):
        url = reverse('questionnaires-list')
        data = {
            "title": "test title",
            "description": "test description"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Questionnaire.objects.filter(id=response.json()['id']).first())
    
    def test_update_a_questionnaire(self):
        questionnaire = Questionnaire.objects.create(
            title="test title",
            description="test description"
        )
        self.assertEqual(Questionnaire.objects.all().count(), 1)

        url = reverse('questionnaires-detail', kwargs={'pk': questionnaire.id})
        data = {
            "title": "updated test title",
            "description": "updated test description"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Questionnaire.objects.first().title, data['title'])
        self.assertEqual(Questionnaire.objects.first().description, data['description'])

    def test_update_a_non_existent_questionnaire(self):
        url = reverse('questionnaires-detail', kwargs={'pk': 1})
        data = {
            "title": "updated test title",
            "description": "updated test description"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_a_exsitent_questionnaire(self):
        questionnaire = Questionnaire.objects.create(
            title="test title",
            description="test description"
        )
        self.assertEqual(Questionnaire.objects.all().count(), 1)

        url = reverse('questionnaires-detail', kwargs={'pk': questionnaire.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Questionnaire.objects.all().count(), 0)
    
    def test_delete_a_non_exsitent_questionnaire(self):
        url = reverse('questionnaires-detail', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
