from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.UserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls)),
]
