from django.db import models
from django.conf import settings


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
    school_type_students = models.CharField(max_length=20,
                                            blank=False,
                                            null=True)
    # for students
    career_teachers = models.CharField(max_length=20,
                                       blank=False,
                                       null=True)
    # for teachers
