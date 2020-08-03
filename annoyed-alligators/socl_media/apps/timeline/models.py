from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    post_content = models.TextField(verbose_name="content")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date_posted = models.DateTimeField(auto_now_add=True,
                                               verbose_name="Published on")

    def __str__(self):
        return self.post_title
