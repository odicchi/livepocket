from django.db import models

# Create your models here.
# class PileColor(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=250)

#     def __str__(self):
#         return self.name

# class HedgeHog(models.Model):
#     name = models.CharField(max_length=250)
#     pile_color = models.ForeignKey('PileColor', on_delete=models.CASCADE)
#     start = models.FloatField(default=1.0)
#     description = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class Comment(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     hedgehog = models.ForeignKey('HedgeHog', on_delete=models.CASCADE)
#     comment = models.TextField()
#     visible = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    ticket_type = models.CharField(max_length=50)
    ticket_quantity = models.IntegerField()
    ticket_price = models.IntegerField()
