from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_created']

    def comment_count(self):
        return self.comment_set.all().count()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    content=models.CharField(max_length=250)

    def __str__(self):
        return self.content