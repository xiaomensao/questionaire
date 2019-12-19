from rest_framework import serializers 

from .models import Questionaire, QuestionaireStatus, QuestionType, Question

class QuestionaireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questionaire
		fields = ('id', 'user', 'status', 'title', 'created')

class QuestionaireStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuestionaireStatus
		fields = ('id', 'name')

class QuestionTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuestionType
		fields = ('id', 'name')