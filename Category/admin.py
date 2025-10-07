from django.contrib import admin
from Category.models import CategoryModel, Comment, Tag
from django.utils.text import Truncator
from django.utils.html import format_html

@admin.register(CategoryModel)
class CategroyAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'short_title', 'author','short_sub_title', 'second_short_title', 'Text', 'created_at', 'updated_at', 'get_tag', 'views')
    list_display_links = ('image_tag', 'short_title', 'author', 'short_sub_title', 'second_short_title', 'Text', 'created_at', 'updated_at', 'get_tag', 'views')
    search_fields = ('title', 'author', 'created_at', 'get_tags')
    list_filter = ('title', 'author', 'created_at', 'tag', 'views')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit: cover;" />', obj.image.url)
        return "No Image"

    def short_sub_title(self, obj):
        return Truncator(obj.sub_title).chars(30)  # faqat 30 ta belgigacha
    short_sub_title.short_description = "Sub Title"

    def short_title(self, obj):
        return Truncator(obj.title).chars(30)  # faqat 30 ta belgigacha
    short_title.short_description = "Title"

    def second_short_title(self, obj):
        return Truncator(obj.second_title).chars(30)  # faqat 30 ta belgigacha
    second_short_title.short_description = "Second Title"

    def Text(self, obj):
        return Truncator(obj.text).chars(30)  # faqat 30 ta belgigacha
    Text.short_description = "Text"

    def get_tag(self, obj):
        return ", ".join([tag.name for tag in obj.tag.all()])
    get_tag.short_description = "Tags"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "text", "created_at")
    search_fields = ("user__username", "text")
    list_filter = ("created_at", "category")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)