import uuid
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True,editable=False)
    image = models.FileField(upload_to='profile/')
    bio = models.TextField(blank=True,null=True)
    website = models.URLField(blank=True,null=True)

    following = models.ManyToManyField('users.Author', blank=True, related_name='followers')

    def __str__(self):
        return str(self.user.username)
