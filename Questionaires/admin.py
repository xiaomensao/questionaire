from django.contrib import admin
from .models import Questionaire, Question, QuestionaireStatus, QuestionType

# Register your models here.

admin.site.register(Questionaire)
admin.site.register(Question)
admin.site.register(QuestionaireStatus)
admin.site.register(QuestionType)
