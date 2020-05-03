from rest_framework import serializers 

from .models import Questionaire, QuestionaireStatus, QuestionType, Question, RadioChoice, Response, ResponseItem

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
		fields = ('id', 'name', 'parent')

class RadioChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model=RadioChoice
		fields = ('id', 'text')

class QuestionSerializer(serializers.ModelSerializer):
	radioChoices = serializers.SerializerMethodField(read_only=True)
	
	def get_radioChoices(self, obj):
		rc = RadioChoice.objects.filter(question=obj)
		serializer = RadioChoiceSerializer(instance=rc, many=True)
		return serializer.data

	class Meta:
		model = Question
		fields = ('id', 'text', 'type', 'questionaire', 'order', 'radioChoices')

class ResponseItemSerializer(serializers.ModelSerializer):
	order = serializers.IntegerField(read_only=True, source="question.order")
	class Meta:
		model=ResponseItem
		fields = ('id', 'question', 'text', 'radio', 'checkbox', 'order')

class ResponseSerializer(serializers.ModelSerializer):
	items = serializers.SerializerMethodField(read_only=True)
	
	def get_items(self, obj):
		responseItems = ResponseItem.objects.filter(response=obj)
		serializer = ResponseItemSerializer(instance=responseItems, many=True)
		return serializer.data

	class Meta:
		model = Response
		fields = ('id', 'questionaire', 'created', 'items')