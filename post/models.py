from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_secret = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)  # 추가

    def can_view(self, user):
        if not self.is_secret:
            return True
        return user == self.author or user.has_perm('post.view_secret_post')

    def __str__(self):
        return self.title

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_secret = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_replies', blank=True)  # 추가

    def can_view(self, user):
        if not self.is_secret:
            return True
        return user == self.post.author or user.has_perm('post.view_secret_post')

    def __str__(self):
        return f"Reply to {self.post.title}"
