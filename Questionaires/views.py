from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import QuestionaireSerializer, QuestionaireStatusSerializer, QuestionTypeSerializer, QuestionSerializer

from .models import Questionaire, QuestionaireStatus, QuestionType, Question
from django.contrib.auth.models import User

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

import json

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

class questionaireStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionaireStatus.objects.all()
    serializer_class = QuestionaireStatusSerializer

class questionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer

class questionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get_queryset(self): 
        queryset = self.queryset
        questionaireId = self.request.query_params.get('questionaireId', None)
        if questionaireId:
            model_q = Questionaire.objects.get(id=questionaireId)
            queryset=queryset.filter(questionaire=model_q)
        return queryset

@api_view(["POST"])
def questionaireSave(request):
    retVal = {'result': 'success'}
    received_q = json.loads(request.body)
    model_status = QuestionaireStatus.objects.get(id=received_q['status'])
    if int(received_q['id']) < 0:
        # create
        # save questionaire
        model_q = Questionaire(user=request.user, status=model_status, title=received_q['title'])
        model_q.save()

    else:
        # update
        model_q = Questionaire.objects.get(id=received_q['id'])
        model_q.user = request.user
        model_q.status = model_status
        model_q.title = received_q['title']
        model_q.save()
        #delete old questions
        oldQues = Question.objects.filter(questionaire=model_q)
        for q in oldQues:
            q.delete()
        
    #save questions
    for question in received_q['questions']:
        model_type = QuestionType.objects.get(id=question['type'])
        model_ques = Question(type=model_type, text=question['text'])
        model_ques.save()
    return Response(retVal, status=HTTP_200_OK)
