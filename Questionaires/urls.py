from django.urls import path
from django.conf.urls import include, url 
from Questionaires import views
from rest_framework import routers 
router = routers.DefaultRouter()
router.register('questionaire', views.questionaireViewset, 'questionaire')
router.register('questionairestatus', views.questionaireStatusViewSet, 'questionairestatus')
router.register('questiontype', views.questionTypeViewSet, 'questiontype')
router.register('question', views.questionViewSet, 'question')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'questionaireSave/$', views.questionaireSave),
    url(r'responseSubmit/$', views.responseSubmit),
]