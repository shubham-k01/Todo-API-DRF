from django.db import models

# Create your models here.
class TodoItem(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=False,null=False)
    status = models.BooleanField(default=False,blank=True,null=False)
