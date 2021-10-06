from django.http import HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class QuestionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def question_choices(self, request):
        question_id = request.data['question_id']

        if question_id:
            choices = Choice.objects.filter(question=question_id)
            serializer = ChoiceSerializer(choices, many=True)

            return Response(serializer.data)
