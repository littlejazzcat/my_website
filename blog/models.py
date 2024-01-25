from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField("标题", max_length=100)
    content = models.TextField("内容")
    creatr_time = models.DateField("发布时间")
    