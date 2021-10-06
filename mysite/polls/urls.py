from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'choice', views.ChoiceViewSet)

urlpatterns = [
    path('', views.index, name='index'),

    path("question_choices/", views.ChoiceViewSet.as_view({"post":"question_choices"}), name="question_choices"),
    path('', include(router.urls)),
]