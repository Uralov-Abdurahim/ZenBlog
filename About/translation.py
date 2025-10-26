from modeltranslation.translator import register, TranslationOptions
from About.models import AboutModel, Team

@register(AboutModel)
class AboutModelTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'function1', 'function2')



@register(Team)
class TeamModelTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'sub_title')