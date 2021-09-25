from django.db import models
#from django.contrib.auth.models import User
class home_quiz(models.Model):
    quiz_id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    number_of_questions=models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)
class home_question(models.Model):
    question_id=models.BigAutoField(primary_key=True)
    quiz_type_id=models.IntegerField(default=0)
    question = models.CharField(max_length=500)
    choice_1=models.CharField(max_length=500)
    choice_2=models.CharField(max_length=500)
    choice_3=models.CharField(max_length=500)
    choice_4=models.CharField(max_length=500)
    correct_choice=models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.question)

