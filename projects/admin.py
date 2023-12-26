from django.contrib import admin
from .models import Project, Tag, Review
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_image', 'demo_link', 'source_link', 'vote_total', 'vote_ratio')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('projet', 'value', 'id')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'id')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Review, ReviewAdmin)