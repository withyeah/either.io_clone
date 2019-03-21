from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, SmartResize
# Create your models here.

def ei_image_path(instance, filename):
    return f'ei/{instance.pk}/images/{filename}'
    
class Question(models.Model):
    title = models.CharField(max_length=30)
    select_a = models.TextField()
    select_b = models.TextField()
    image_a = ProcessedImageField(
                blank=True,
                upload_to = ei_image_path,         # 저장위치
                processors=[SmartResize(300,400)],  # 처리할 작업 목록
                format='JPEG',                       # 저장포맷
                options={'quality':90}               # title, content , image와같은 Field가 바뀌면 다시 migrate해야하지만
                                                     # 그 외에 속성을 추가하거나 속성을 변경하면 다시 안해 도 됌
            )
    image_b = ProcessedImageField(
                blank=True,
                upload_to = ei_image_path,         # 저장위치
                processors=[SmartResize(300,400)],  # 처리할 작업 목록
                format='JPEG',                       # 저장포맷
                options={'quality':90}               # title, content , image와같은 Field가 바뀌면 다시 migrate해야하지만
                                                     # 그 외에 속성을 추가하거나 속성을 변경하면 다시 안해 도 됌
            )
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField()
    comment = models.TextField()
    
    