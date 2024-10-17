from rest_framework import serializers
from . import models


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questionnaire
        fields = '__all__'
