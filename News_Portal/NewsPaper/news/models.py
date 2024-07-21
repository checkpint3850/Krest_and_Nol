from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = self.posts.aggregate(pr=Coalesce(Sum('post_rating'), 0))['pr']
        comments_rating = self.user.comments.aggregate(cr=Coalesce(Sum('comment_rating'), 0))['cr']
        posts_comments_rating = self.posts.aggregate(pcr=Coalesce(Sum('comment__comment_rating'), 0))['pcr']

        print(posts_rating)
        print('---------------------')
        print(comments_rating)
        print('---------------------')
        print(posts_comments_rating)

        self.author_rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    news_article = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    article = 'A'
    news = 'N'
    POSITIONS = [
        (article, "Статья"),
        (news, "Новость"),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField(max_length=1, choices=POSITIONS, default=news)
    datetime_in = models.DateTimeField(auto_now_add=True)
    news_article = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=60)
    text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        point = '....'
        return self.text[:124] + point


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    time_comment = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
