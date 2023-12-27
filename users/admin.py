from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'location', 'short_intro', 'bio', 'profile_image', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website', 'create')
    list_display_links = ('user', 'name')
    search_fields = ('name', 'location')
    list_filter = ('location', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website')
    list_per_page = 25


admin.site.register(Profile, ProfileAdmin)