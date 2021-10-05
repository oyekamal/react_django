from django.http import HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *

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