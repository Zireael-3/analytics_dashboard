from django.db import models


class UserAction(models.Model):
    amount_of_time_online = models.CharField(max_length=20)
    device = models.CharField(max_length=20)
    amount_of_tags = models.CharField(max_length=50)
    number_of_chats_per_entry = models.DecimalField(max_digits=5, decimal_places=2)