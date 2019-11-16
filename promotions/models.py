from django.db import models
from django.utils import timezone

class HomepageSlider(models.Model):
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100)
    image = models.FileField(max_length=100, upload_to="promotions")

    def __str__(self):
        return self.title

    def image_url(self):
        return "http://localhost:8000/%s" % self.image.url
