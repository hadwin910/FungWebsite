from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email

class Titanic(models.Model):
    survived = models.IntegerField()
    pclass= models.IntegerField()
    sex= models.IntegerField()
    age= models.FloatField()
    sibsp= models.IntegerField()
    parch= models.IntegerField()
    fare= models.FloatField()
    embarked=models.IntegerField()
    title=models.IntegerField()
