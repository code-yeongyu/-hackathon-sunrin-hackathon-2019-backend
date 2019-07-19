from django.conf.urls import url
from community import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^$', views.ArticleList.as_view()),  # 게시글을 업로드하거나, 리스트를 얻을 수 있는 라우트
]
