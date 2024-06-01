from django.db import models
from .event import Event

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    sales_start_date = models.DateTimeField()
    sales_end_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='Available')

    def __str__(self):
        return f"{self.ticket_type} - {self.event.name}"
