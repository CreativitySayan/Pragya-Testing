from django.db import models

class Certificate(models.Model):
    certificate_number = models.CharField(max_length=13, unique=True)
    participant_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    event_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.certificate_number
