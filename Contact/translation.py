from modeltranslation.translator import register, TranslationOptions
from Contact.models import Information

@register(Information)
class InformationModelTranslationOptions(TranslationOptions):
    fields = ('address',)