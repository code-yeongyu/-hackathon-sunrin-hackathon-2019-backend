from rest_framework import serializers
from custom_profile.models import Profile, Image


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "is_student", "is_certified", "work_at",
                  "location", "school_type_students", "career_teachers")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')
