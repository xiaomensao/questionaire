from django.urls import path
from django.conf.urls import include, url 
from Questionaires import views
from rest_framework import routers 
router = routers.DefaultRouter()
router.register('questionaire', views.questionaireViewset, 'questionaire')

urlpatterns = [
    url(r'^', include(router.urls)),
]