from django.conf.urls import url
from custom_profile import views

urlpatterns = [
    url(r'^signup/$', views.sign_up),  # 회원가입 요청을 넣는 라우트
    url(r'^$', views.ProfileOverall.as_view()),  # 프로필 정보를 얻거나 , 변경하는 라우트
    url(r'^images/(?P<pk>[0-9]+)/$', views.image),  # 이미지를 얻는 라우트
    url(r'^images/$', views.create_image),  # 이미지를 업로드하는 라우트
]
