from django.db import models
from django.contrib.auth.models import User # 장고가 기본제공해주는 1:다 관계 테이블 이용

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # , null=True, blank=True - 구조 잡는데 거슬리지 않게 처음에는 이렇게 세팅하고 작업한다고 함
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


        # 마이그레이션 해줘야 sql문 생성
        # python manage.py makemigrations : base app 안에 slq문 생성
        # python manage.py migrate : 실제로 생성시킴
        # db 변경할때마다 위의 두개는 실행시켜줘야 함

        # admin 만들기
        # python manage.py createsuperuser