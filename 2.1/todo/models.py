from django.db import models
class Task(models.Model):

    title = models.CharField(max_length=300)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title