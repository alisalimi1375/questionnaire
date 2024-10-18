from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.QuestionnaireViewSet, 'questionnaires')

questions_router = NestedDefaultRouter(router, '', lookup='questionnaire')
questions_router.register('questions', views.QuestionViewSet, 'questions')

answer_router = NestedDefaultRouter(questions_router, 'questions', lookup='question')
answer_router.register('answers', views.AnswerViewSet, 'answers')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(questions_router.urls)),
    path('', include(answer_router.urls)),
]
