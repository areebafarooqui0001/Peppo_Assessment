from django.db import models  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from django.utils import timezone  # type: ignore


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.event_date}"

    def clean(self):
        """
        Ensure event_date is in the future.
        This runs when full_clean() is called on the model (or when explicitly invoked).
        """
        super().clean()
        if self.event_date <= timezone.now():
            raise ValidationError({"event_date": "Event date must be in the future."})
