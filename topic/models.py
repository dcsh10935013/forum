from django.db import models
from django.contrib.auth.models import User
# 討論主題
class Topic(models.Model):
    subject = models.CharField('討論主題', max_length=255)
    content = models.TextField('內文')
    author = models.ForeignKey(User, on_delete=models.CASCADE)#串聯式處理
    
    created = models.DateTimeField('建立時間', auto_now_add=True)
    replied = models.DateTimeField('回覆時間', null=True, blank=True)

    def __str__(self):
# Create your models here.
