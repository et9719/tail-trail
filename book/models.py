''' Imports '''
from django.db import models
# from tailtrail.settings import DATE_INPUT_FORMATS


class Availability(models.Model):
    ''' Define what we need to know for the availability '''
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    requested = models.BooleanField(default=False)
    # requested by ?
    approved = models.BooleanField(default=False)

    class Meta:
        ''' Show availability in a list orded by date '''
        ordering = ['date']

    # input_formats = {
    #     'date': DATE_INPUT_FORMATS,
    # }

    def __str__(self):
        return f"{self.date} {self.time}"


# Create Profile model
