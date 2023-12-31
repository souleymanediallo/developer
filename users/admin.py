from django.contrib import admin
from .models import Profile, Skill, Message
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'location', 'short_intro', 'bio', 'profile_image', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website', 'create')
    list_display_links = ('user', 'name')
    search_fields = ('name', 'location')
    list_filter = ('location', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website')
    list_per_page = 25


admin.site.register(Profile, ProfileAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name')
    list_display_links = ('owner', 'name')
    search_fields = ('owner', 'name')
    list_filter = ('owner', 'name')
    list_per_page = 25


admin.site.register(Skill, SkillAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'name', 'email', 'subject', 'is_read')
    list_display_links = ('sender', 'recipient', 'name', 'email', 'subject')
    search_fields = ('sender', 'recipient', 'name', 'email', 'subject', 'is_read')
    list_filter = ('sender', 'recipient', 'name', 'email', 'subject', 'is_read')
    list_per_page = 25


admin.site.register(Message, MessageAdmin)