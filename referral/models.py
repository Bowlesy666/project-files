from django.db import models
from django.contrib.auth.models import User


class Referral(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_referrals')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_referrals')
    referral_subject = models.CharField(max_length=100)
    referral_description = models.TextField()
    proposed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    is_percentage_editable = models.BooleanField(default=True)
    contract_agreed = models.BooleanField(default=False)
    contract_rejected = models.BooleanField(default=False)
    rejection_reason = models.CharField(max_length=200)
    contract_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username} - Amount: {self.amount_proposed}, Percentage: {self.percentage}%"

    def calculate_commission(self):
        return (self.proposed_amount * self.percentage) / 100
