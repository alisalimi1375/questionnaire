from django.db import models
from users.models import User
from .validators import question_details_validator, answer_details_validator


class Questionnaire(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    order = models.PositiveIntegerField()
    text = models.TextField()
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    detials = models.JSONField(validators=[question_details_validator])

    def __str__(self):
        return f'{self.order}. {self.text:.27}...'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    detials = models.JSONField(validators=[answer_details_validator])

    def __str__(self):
        return f'{str(self.user)} to {str(self.question)}...'
