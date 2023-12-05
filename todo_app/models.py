from django.db import models
from django.utils import timezone


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title

class Tag(models.Model):
    value = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.value
