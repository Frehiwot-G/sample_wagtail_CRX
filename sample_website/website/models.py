"""
Create or customize your page models here.
"""
from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel,StreamFieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage,
)


class ArticlePage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Article"
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "coderedcms/pages/article_page.html"
    search_template = "coderedcms/pages/article_page.search.html"


class ArticleIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = "Article Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.ArticlePage"]

    template = "coderedcms/pages/article_index_page.html"


class FormPage(CoderedFormPage):
    """
    A page with an html <form>.
    """

    class Meta:
        verbose_name = "Form"

    template = "coderedcms/pages/form_page.html"


class FormPageField(CoderedFormField):
    """
    A field that links to a FormPage.
    """

    class Meta:
        ordering = ["sort_order"]

    page = ParentalKey("FormPage", related_name="form_fields")


class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """

    page = ParentalKey("FormPage", related_name="confirmation_emails")


class WebPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    """

    class Meta:
        verbose_name = "Web Page"

    template = "coderedcms/pages/web_page.html"


class MenuIndexPage(CoderedWebPage):
    """
    Landing page for menu
    """
    class Meta:
        verbose_name = "Menu Landing Page"

    index_query_pagemodel = 'website.MenuPage'

    subpage_types = ['website.MenuPage']

    template = 'coderedcms/pages/menu_index_page.html'


class MenuPage(CoderedWebPage):
    
    class Meta:
        verbose_name = "Menu Page"

    parent_page_types = ['website.MenuIndexPage']

    template = "coderedcms/pages/menu_page.html"
    
    description = RichTextField(
        verbose_name="picture discription",
        null=True,
        blank=True,
        default=""
    )
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='menu Photo',
    )
    
    body_content_panels = CoderedWebPage.body_content_panels + [
         FieldPanel("photo"),
        # StreamFieldPanel("photo"),
        FieldPanel("description"),
    ]


@register_setting
class SnipcartSettings(BaseSetting):
    """
    Snipcart API Key
    """

    class Meta:
        verbose_name = ("Snipcart")

    snipcart_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=("Snipcart API Key"),
        help_text=("The API Key used for Snipcart."),
    )
