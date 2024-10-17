from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class QuestionnaireViewSet(ModelViewSet):
    queryset = models.Questionnaire.objects.all()
    serializer_class = serializers.QuestionnaireSerializer
