from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class QuestionaireStatus(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return str(self.name)

class Questionaire(models.Model):
    created = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(QuestionaireStatus, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
    	return str(self.created)

class QuestionType(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Question(models.Model):
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE, default=1)
    questionaire = models.ForeignKey(Questionaire, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, default='')
    order = models.IntegerField(default=1)
    def __str__(self):
        return str(self.text)

class RadioChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, default='')
    def __str__(self):
        return str(self.text)