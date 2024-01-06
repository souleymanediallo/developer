from django.db import models
import uuid
from users.models import Profile
# Create your models here.

URL_PRODUCT = "https://media.istockphoto.com/id/1305995602/fr/photo/conception-r%C3%A9active-flottante-r%C3%A9active.jpg?s=2048x2048&w=is&k=20&c=NQYG8GK8BdSKqDWsefpwJhcnUlC_ZJoALD-nGM_Tbgk="


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    featured_image = models.CharField(max_length=300, null=True, blank=True, default=URL_PRODUCT)
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name