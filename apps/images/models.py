# models.py
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from wagtail.wagtailimages.models import AbstractImage
from wagtail.wagtailimages.models import AbstractRendition
from wagtail.wagtailimages.models import Image


class CustomImage(AbstractImage):
    author = models.CharField(max_length=128, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        'author',
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )


# Delete the source image file when an image is deleted
@receiver(post_delete, sender=CustomImage)
def image_delete(sender, instance, **kwargs):
    instance.file.delete(False)


# Delete the rendition image file when a rendition is deleted
@receiver(post_delete, sender=CustomRendition)
def rendition_delete(sender, instance, **kwargs):
    instance.file.delete(False)
