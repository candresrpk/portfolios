from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.shortcuts import reverse

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField()
    published_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    slug = models.SlugField(null=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(uuid4()))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:posts_detail", kwargs={"slug": self.slug})

    def get_like_url(self):
        return reverse("posts:post_like", kwargs={"slug": self.slug})

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post}'


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
