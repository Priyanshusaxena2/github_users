from django.db import models

# Create your models here.


class User(models.Model):
    """

    """
    login = models.CharField(max_length=100)
    id = models.CharField(max_length=20,primary_key=True)
    node_id = models.CharField(max_length=100)
    avatar_url = models.URLField(blank=True,null=True)
    gravatar_id = models.CharField(max_length=20,blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    html_url = models.URLField(blank=True,null=True)
    followers_url = models.URLField(blank=True,null=True)
    following_url = models.URLField(blank=True,null=True)
    gists_url = models.URLField(blank=True,null=True)
    starred_url = models.URLField(blank=True,null=True)
    subscriptions_url = models.URLField(blank=True,null=True)
    organizations_url = models.URLField(blank=True,null=True)
    repos_url = models.URLField(blank=True,null=True)
    events_url = models.URLField(blank=True,null=True)
    received_events_url = models.URLField(blank=True,null=True)
    type = models.CharField(max_length=50,blank=True,null=True)
    site_admin = models.BooleanField()
    name = models.CharField(max_length=100,blank=True,null=True)
    company = models.CharField(max_length=100,blank=True,null=True)
    blog = models.CharField(max_length=256,blank=True,null=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(null=True,blank=True)
    hireable = models.NullBooleanField(null=True,blank=True)
    bio = models.CharField(max_length=256,blank=True,null=True)
    public_repos = models.IntegerField()
    public_gists = models.IntegerField()
    followers = models.IntegerField()
    following = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
