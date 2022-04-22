from django.db import models

class twitter_data(models.Model):
    tweets = models.CharField(max_length=300)
    user = models.CharField(max_length=300,default=None,null=True)
    created_at = models.CharField(max_length=200,default='')
    hashtags = models.CharField(max_length=200,default='')
    user_mentions = models.CharField(max_length=500,default='')
    url = models.CharField(max_length=200,default="")


    def __str__(self):
        return tweets