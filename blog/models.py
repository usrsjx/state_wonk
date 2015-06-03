from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    contents = models.TextField(blank=False, null=False, unique=False)
    created = models.DateTimeField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created',)