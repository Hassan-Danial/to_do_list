from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(default=one_week_hence)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
