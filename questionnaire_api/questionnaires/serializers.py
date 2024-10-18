from rest_framework import serializers
from . import models


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questionnaire
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    questionnaire_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Question
        exclude = ('questionnaire',)


class AnswerSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Answer
        exclude = ('question', 'user')
