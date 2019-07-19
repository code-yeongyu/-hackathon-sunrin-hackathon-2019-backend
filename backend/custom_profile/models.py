from django.db import models
from django.conf import settings

from imagekit.models import ImageSpecField


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=True)
    is_certified = models.BooleanField(default=True)
    work_at = models.CharField(max_length=30,
                               blank=False,
                               null=True)
    location = models.TextField(blank=False,
                                null=True)
    images_id = models.TextField(null=False, blank=False, default="")
    school_type_students = models.CharField(max_length=20,
                                            blank=False,
                                            null=True)
    # for students
    career_teachers = models.CharField(max_length=20,
                                       blank=False,
                                       null=True)
    # for teachers


class Image(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/uploaded/represent/%Y/%m/%d/', )
    thumbnail = ImageSpecField(
        source='image',
        processors=[],
        format='JPEG',
        options={'quality': 60})
