from rest_framework import serializers 

from .models import Questionaire

class QuestionaireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questionaire
		fields = ('id', 'user', 'status', 'title', 'created')