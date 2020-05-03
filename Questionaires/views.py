from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import QuestionaireSerializer, QuestionaireStatusSerializer, QuestionTypeSerializer, QuestionSerializer, ResponseSerializer

from .models import Questionaire, QuestionaireStatus, QuestionType, Question, RadioChoice, Response as Res, ResponseItem
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

@permission_classes([permissions.IsAuthenticatedOrReadOnly,])
class questionaireViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Questionaire.objects.all()
    serializer_class = QuestionaireSerializer
    def get_queryset(self): 
        queryset = self.queryset
        if self.request.user.is_authenticated:
            queryset=queryset.filter(user=self.request.user)
        else:
            queryset=queryset.filter(status_id=2)
        return queryset

class questionaireStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionaireStatus.objects.all()
    serializer_class = QuestionaireStatusSerializer

class questionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer

@permission_classes([permissions.IsAuthenticatedOrReadOnly,])
class questionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get_queryset(self): 
        queryset = self.queryset
        questionaireId = self.request.query_params.get('questionaireId', None)
        if questionaireId:
            queryset=queryset.filter(questionaire_id=questionaireId).order_by('order', 'type')
        return queryset

class responseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Res.objects.all()
    serializer_class = ResponseSerializer
    def get_queryset(self): 
        queryset = self.queryset
        questionaireId = self.request.query_params.get('questionaireId', None)
        if questionaireId:
            queryset=queryset.filter(questionaire_id=questionaireId).order_by('created')
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
            oldRadios = RadioChoice.objects.filter(question=q)
            for r in oldRadios:
                r.delete()
            q.delete()
        
    #save questions
    for question in received_q['questions']:
        model_type = QuestionType.objects.get(id=question['type'])
        model_ques = Question(questionaire=model_q, type=model_type, text=question['text'], order=question['order'])
        model_ques.save()
        
        if question['radioChoices']:
            for rc in question['radioChoices']:
                model_rc = RadioChoice(question=model_ques, text=rc['text'])
                model_rc.save()
    return Response(retVal, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes([permissions.AllowAny,])
@authentication_classes([])
def responseSubmit(request):
    retVal = {'result': 'success'}
    received_r = json.loads(request.body)

    #save response
    model_q = Questionaire.objects.get(id=received_r['questionaireId'])
    model_r = Res(questionaire=model_q)
    model_r.save()
        
    #save responseItems
    for item in received_r['items']:
        model_ques = Question(id=item['quesId'])
        model_item = ResponseItem(response=model_r, question=model_ques, text=item['text'], checkbox=item['checkbox'])
        if item['radio']:
            model_radio = RadioChoice(id=item['radio'])
            model_item.radio = model_radio
        model_item.save()
    return Response(retVal, status=HTTP_200_OK)
