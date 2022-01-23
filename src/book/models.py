from django.db import models

from embed_video.fields import EmbedVideoField

class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Üerschrift', blank=False)
    position = models.IntegerField(help_text='Sortierfeld', default=0, blank=True)
    video = EmbedVideoField(blank=True, null=True)

    class Meta:
        ordering = ['position', 'pk']
