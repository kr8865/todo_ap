from django.db import models

# Create y(our models here.
class Todo(models.Model):
    task=models.TextField()
    created_at=models.DateField()

