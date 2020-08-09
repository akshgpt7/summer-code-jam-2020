from django.db import models
from django.contrib.auth.models import User
from ..users.models import Profile

class Post(models.Model):
    """
    The model to store Posts created by users.
    Fields-
    post_content: The text of the post
    posted_by: User who created the post
    post_date_posted: Date of making the post
    """

    post_content = models.TextField(verbose_name="content")
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_date_posted = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Published on")
