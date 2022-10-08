from django.db import models

class student(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to = "images/",null = True)
    dob = models.DateField(null = True)
    def __str__(self):
        return '{}'.format(self.id)
    
class mark(models.Model):
    student1 = models.ForeignKey(student, on_delete = models.CASCADE)
    Tamil = models.IntegerField(null = True)
    English = models.IntegerField(null = True)
    Computer = models.IntegerField(null = True)
    

# Create your models here.
