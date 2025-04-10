from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    class Status(models.TextChoices):
        TODO =  "Todo"
        PROCESSING = "Processing"
        DONE = "Done"

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.TODO)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE , related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
