from django.db import models


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(
        'auth.user', related_name='article', on_delete=models.CASCADE)
    title = models.CharField(null=False, blank=False, max_length=100)
    content = models.TextField(null=False, blank=False)

    def __str__(self):  # 본 클래스의 문자열 표현
        return self.content

    class Meta:
        ordering = ('created_at', )
