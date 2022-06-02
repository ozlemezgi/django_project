from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

  #  def get_absolute_url(self):
  #      return reverse("blog:blog-home-post",kwargs={"pk":self.pk})





class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,verbose_name = "Makale",related_name= "comments",null=True)
    comment_author = models.ForeignKey(to=Profile,on_delete=models.CASCADE,related_name='yorumlar')
    comment_content = models.CharField(max_length=200,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['comment_date']    

