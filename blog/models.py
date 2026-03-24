from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_created']
    def __str__(self):
        return self.title