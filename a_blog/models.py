from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from datetime import date

class BlogPage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    
    template = "a_blog/blog_page.html"
    
    def get_context(self, request):
        articles = self.get_children().live().order_by('-first_published_at')
        context = super().get_context(request)
        context['articles'] = articles
        return context
    
    
class ArticlePage(Page):
    intro = models.CharField(max_length=80)
    body = RichTextField(blank=True)
    date = models.DateField("Post date", default=date.today)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=80)
    
    content_panels = Page.content_panels +[
    FieldPanel('intro'),
    FieldPanel('image'),
    FieldPanel('caption'),
    FieldPanel('body'), 
    FieldPanel('date'),
    ]

class HomePage(Page):
    banner_title = models.CharField(max_length=120, help_text="Title for the homepage banner")
    banner_subtitle = RichTextField(blank=True, help_text="Subtitle text below the banner title")
    banner_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Upload a banner image"
    )

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        FieldPanel('banner_image'),
    ]
