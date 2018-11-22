# coding utf-8

from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from wagtail.core.models import Page


@register(Page)
class PageTR(TranslationOptions):
    pass
