from modeltranslation.translator import register, TranslationOptions
from Category.models import Tag, CategoryModel

@register(Tag)
class TagModelTranslationOptions(TranslationOptions):
    fields = ('name',)



@register(CategoryModel)
class CategoryModelModelTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'author', 'sub_title', 'second_title', 'text')
