from django.db import models

class Comparison(models.Model):
    user1 = models.CharField(max_length=128)
    user2 = models.CharField(max_length=128)
    user1_stats = models.TextField()
    user2_stats = models.TextField()
