from django.db import models

# Create your models here.

from account.models import User

class Project(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)