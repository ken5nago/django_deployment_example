from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimages = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=1)   #null=ture は空のデータが入ってきても大丈夫だよ　
    read = models.IntegerField(null=True, blank=True, default=1)   #blank=true はformのvaridation時に空でもオッケーよ　
    readtext = models.TextField(null=True, blank=True, default=' ')
    
    
