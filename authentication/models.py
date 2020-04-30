from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    added_on = models.DateField(default=timezone.now)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city = models.CharField(default="Delhi", max_length=100)
    pincode = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s %s for userid: %s" % (self.add1, self.add2, self.locality, self.user.pk)
