import json

from django.http import JsonResponse, Http404
from django.contrib.auth.models import User

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from community.models import Article
from community.serializers import ArticleSerializer
from backend import settings


class ArticleList(generics.ListAPIView, APIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, format=None):
        if request.user.is_authenticated:
            articles = Article.objects.filter(writer=request.user).values()
            return Response(articles, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):  # 작성자 이름 자동추가 기능을 위해 post용 뷰 분리
        if request.user.is_authenticated:  # 사용자가 인증 되었을경우
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(writer=request.user)  # 작성자 요청자로 설정
                return JsonResponse(
                    serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)  # 폼에 오류가 있을 경우
        return Response(status=status.HTTP_401_UNAUTHORIZED)  # 인증되지 않았을 경우


class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        if str(getattr(article, 'writer')) == request.user.username:  # 인증
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, pk, formoat=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if str(getattr(article, 'writer')) == request.user.username:  # 인증
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response("This is not your article.", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        if str(getattr(article, 'writer')) == request.user.username:  # 인증
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("This is not your article.", status=status.HTTP_400_BAD_REQUEST)
