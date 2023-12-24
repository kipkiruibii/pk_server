from django.db import models
from datetime import datetime, timezone
import pytz


class CustomerDetails(models.Model):
    phone_number = models.TextField(default='Phone Number')
    email_address = models.TextField(default='Email Address')
    date_registered = models.DateTimeField(default=datetime.now(pytz.timezone('Africa/Nairobi')))

    def __str__(self):
        return self.phone_number

