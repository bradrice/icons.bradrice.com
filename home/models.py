from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model

class HomePage(Page):
    max_count = 1
    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]
