from django.db import models

# Create your models here.
class Question(models.Model): #Question extends Model class
    question_text = models.CharField(max_length=200) #Specify fields here
    #primary key is created automatically
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text #make sure when it's called, we return question text only

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #If Question is deleted also delete choice
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

