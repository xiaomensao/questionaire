from rest_framework import serializers 

from .models import Questionaire, QuestionaireStatus, QuestionType, Question

class QuestionaireSerializer(serializers.ModelSerializer):
	statusName = serializers.CharField(read_only=True, source="status.name")
	class Meta:
		model = Questionaire
		fields = ('id', 'user', 'status', 'title', 'created', 'statusName')

class QuestionaireStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuestionaireStatus
		fields = ('id', 'name')

class QuestionTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuestionType
		fields = ('id', 'name')

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('id', 'text', 'type', 'questionaire')