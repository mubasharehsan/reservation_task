from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('DONE', 'Done'),
    )

    flight_name = models.CharField(max_length=50, blank=True, null=True)
    flight_number = models.CharField(max_length=10)
    scheduled = models.DateTimeField(blank=True, null=True)
    expected_arrival = models.DateTimeField(blank=True, null=True)
    depart_from = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    fare = models.FloatField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'

    def __str__(self):
        return 'Reservation-ID: {} Flight name: {} Flight Number: {}'.format(
            self.id, self.flight_name, self.flight_number
        )
