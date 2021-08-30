from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    cate_list =(
        ('Music', 'Music'),
        ('Social', 'Social'),
    )

    title = models.CharField(max_length=100)
    #content = models.TextField()
    content = RichTextField(blank= True, null= True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=cate_list)
    likes = models.ManyToManyField(User, related_name='blog_likes')
    img = models.ImageField(default = 'default.png', upload_to='Photos')
    vid = models.FileField(default = 'default.mp4', upload_to='videos/')

    def totalLikes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-dateil', kwargs={'pk': self.pk})
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'commnets', on_delete = models.CASCADE)
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post:{self.post} - commmented: {self.name} '

