from array import ArrayType
import array
from multiprocessing import Array
from typing import List
from django.db import models

# Create your models here.
class Interview(models.Model):
    id = models.IntegerField(primary_key=True)
    candidate_name = models.CharField(max_length=40,default='Denny Dep')
    level = models.CharField(max_length=10,default='junior')
    sub_size = models.IntegerField(default=2)
  
    class Meta:
      verbose_name = 'Interview'
      verbose_name_plural = 'Interviews'

class Subject(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=40,default='.Net Developer')
  grade = models.CharField(max_length=40,default='junior')
  description = models.TextField()
  feedback = models.CharField(max_length=40,default='He is also good')
  interview = models.ForeignKey(Interview,related_name='subjects', null=True,on_delete=models.CASCADE)
  class Meta:
      verbose_name = 'Subject'
      verbose_name_plural = 'Subjects'

class Template(models.Model):
  id = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=40,default='.Net Developer')

  class Meta:
      verbose_name = 'Template'
      verbose_name_plural = 'Templates'         

class Temp_subj(models.Model):
    name = models.CharField(max_length=40,default='Devops')
    subject = models.TextField()
    template = models.ForeignKey(Template,related_name='subjects',null=True,on_delete=models.CASCADE)



  

  


    
    
   
