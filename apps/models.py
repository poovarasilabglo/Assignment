from django.db import models

class student(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to = "images/",null = True)
    dob = models.DateField(null = True)
    def __str__(self):
        return '{}'.format(self.id)
    
class mark(models.Model):
    student1 = models.ForeignKey(student, on_delete = models.CASCADE)
    subject = models.CharField(max_length=50, null = True)
    mark = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    updated_at = models.DateTimeField(auto_now=True, null = True)
    create_name = models.CharField(max_length=50, null = True)
    modify_name = models.CharField(max_length=50, null = True)
# Create your models here.
