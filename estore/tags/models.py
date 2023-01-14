from django.db import models
from django.contrib.contenttypes.models import ContentType
 from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=250)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_types = modedels.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    