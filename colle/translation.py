from .models import Cours
from modeltranslation.translator import TranslationOptions, register

@register(Cours)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)
