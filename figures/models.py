from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model

class FigureIndex(Page):
  # Al list of all the iconic figures in the database
    subpage_types = ['figures.FigureDetail']
    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['figure_entries'] = FigureDetail.objects.live().descendant_of(self)
        return context


class FigureDetail(Page):
    parent_page_types = ['FigureIndex']
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

