from backend import settings

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from custom_profile.models import Profile
from custom_profile.serializers import ProfileSerializer
from custom_profile.forms import SignUpForm


class ProfileOverall(APIView):  # 자신의 프로필 수정
    def get(self, request):  # 프로필 조회
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except:
                Profile.objects.create(user=request.user)
                profile = Profile.objects.get(user=request.user)
            return Response(
                {
                    'is_high': Profile.is_high
                },
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except:
                Profile.objects.create(user=request.user)
                profile = Profile.objects.get(user=request.user)
                serializer = ProfileSerializer(profile, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            'is_high': Profile.is_high
                        },
                        status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def sign_up(request):  # 회원가입
    form = SignUpForm(request.POST)
    try:
        User.objects.get(email=request.data.get('email'))
        return Response(
            {
                "email": "해당 이메일은 이미 존재합니다."
            },
            status=status.HTTP_406_NOT_ACCEPTABLE)
    except User.DoesNotExist:  # 이메일이 중복이 아닐경우에
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            Profile.objects.create(user=user)
            Token.objects.create(user=user)
            return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
