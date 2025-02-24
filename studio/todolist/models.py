from django.db import models

# Create your models here.
import uuid

from account.models import User
from project.models import Project

class Todo(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)    
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    created_by=models.ForeignKey(User,related_name='todolists',on_delete=models.CASCADE)
    project=models.ForeignKey(Project,related_name='todolists',on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} - {self.description}"
        