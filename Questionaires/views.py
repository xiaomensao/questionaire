from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import QuestionaireSerializer

from .models import Questionaire

# Create your views here.

def index(request):
    return HttpResponse("Create a questionaire here")

class questionaireViewset(viewsets.ModelViewSet):
    queryset = Questionaire.objects.all()
    serializer_class = QuestionaireSerializer
    def get_queryset(self): 
        queryset = self.queryset
        query_set=queryset.filter(user=self.request.user)
        return query_set
