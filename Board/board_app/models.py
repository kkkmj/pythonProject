from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class   sil_Board(models.Model): #글모델
    title = models.CharField(max_length=100, null=False) #글제목
    petname = models.CharField(max_length=20) #반려동물 이름
    petimage = models.ImageField(null=True, blank=True) #반려동물 사진
    petage = models.CharField(max_length=20, null=True, blank=True)
    petkind = models.CharField(max_length=30) #품종
    pettype = models.CharField(max_length=20) #축종
    character = models.CharField(max_length=200) #특징
    whereCD = models.CharField(max_length=200) #실종장소
    whereCGG = models.CharField(max_length=200)
    date = models.DateField() #실종날짜
    money = models.CharField(max_length=50)#사례금
    body = models.TextField() #내용
    created_at = models.DateTimeField(auto_now_add=True) #올린시간
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) #외부키 작성자

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title

class Comment(models.Model): #댓글 모델
    comment = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
    cuser = models.ForeignKey(User, on_delete=models.CASCADE, null=False) #외부키 작성자
    cpost = models.ForeignKey(sil_Board, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment