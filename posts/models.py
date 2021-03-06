import uuid

from django.db import models


class Post(models.Model):
    author = models.ForeignKey("users.Author",on_delete=models.CASCADE,related_name='post')
    image = models.FileField(upload_to='posts/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=128,null=True,blank=True)
    likes = models.ManyToManyField('users.Author',related_name='likes',blank=True)
    
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


