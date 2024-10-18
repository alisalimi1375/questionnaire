from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, ValidationError
from users.models import User
from .models import Questionnaire, Question, Answer
from .serializers import QuestionnaireSerializer, QuestionSerializer, AnswerSerializer


class QuestionnaireViewSet(ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.queryset.filter(
            questionnaire_id = self.get_questionnaire_or_404().id,
        )

    def perform_create(self, serializer):
        serializer.save(
            questionnaire_id = self.get_questionnaire_or_404().id,
        )

    def get_questionnaire_or_404(self) -> Questionnaire:
        try:
            questionnaire = Questionnaire.objects.get(
                id = self.kwargs['questionnaire_pk'],
            )
        except Questionnaire.DoesNotExist:
            raise NotFound('Questionnaire is not found.')
        return questionnaire


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return self.queryset.filter(
            question_id = self.get_question_or_404().id,
        )

    def perform_create(self, serializer):
        serializer.save(
            question_id = self.get_question_or_404().id,
            user_id = self.get_user_or_404().id,
        )

    def get_question_or_404(self) -> Question:
        try:
            question = Question.objects.get(
                id = self.kwargs['question_pk'],
            )
        except Question.DoesNotExist:
            raise NotFound('Question is not found.')
        return question

    def get_user_or_404(self) -> User:
        try:
            user = User.objects.get(
                id = self.request.data['user_id'],
            )
        except KeyError:
            raise ValidationError({'user_id': ['this field is required.']})
        except User.DoesNotExist:
            raise NotFound('User is not found.')
        return user
