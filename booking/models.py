from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='messages')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='messages')
    meeting_subject = models.CharField(max_length=100)
    meeting_description = models.TextField()
    meeting_location = models.CharField(max_length=100)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_accepted = models.BooleanField(default=False)
    additional_notes = models.TextField()
    propose_alternative_location = models.CharField(max_length=100)
    propose_alternative_date = models.DateField()
    propose_alternative_time = models.TimeField()

    def __str__(self):
        return f'{self.sender.username} - {self.meeting_subject} - {self.meeting_date} {self.meeting_time}'
