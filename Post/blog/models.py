from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)  
 
    def __str__(self):
        return "%s (%s)" % (self.name, self.email)  
    class Meta:
        db_table = "author"

 
class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    body = models.TextField()  
 
    def summary(self):
        return self.body[:100]       
    def __str__(self):
        return "%s (%s)" % (self.title, self.author.name)
    class meta:
        db_table = "post"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content =  models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, self.timestamp, str(self.user.username)) 
    class meta:
        db_table = "comment"
