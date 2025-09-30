from django.contrib import admin
from About.models import AboutModel, Team

@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'sub_title', 'function1', 'function2')
    list_display_links = ('image', 'title', 'sub_title', 'function1', 'function2')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'position', 'sub_title', 'x_link', 'facebook_link', 'instagram_link', 'Linkedin_link')
    list_display_links = ('image', 'name', 'position', 'sub_title', 'x_link', 'facebook_link', 'instagram_link', 'Linkedin_link')
    
