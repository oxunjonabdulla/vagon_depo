from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models import Banner, Blog, About, Service, OurResult, Gallery, History, Management, Contact, BlogSocialLink, \
    SocialLink


# Register your models here.


class CustomTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Banner)
class BannerAdmin(CustomTranslationAdmin):
    list_display = ['title', 'description', 'image']
    list_display_links = ['title']
    list_filter = ['title', 'description', 'image']
    search_fields = ['title', 'description']


@admin.register(Blog)
class BlogAdmin(CustomTranslationAdmin):
    list_display = ['title', 'description', "text", 'image', "created_at"]
    list_display_links = ['title']
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']


@admin.register(About)
class AboutAdmin(CustomTranslationAdmin):
    list_display = ['title', 'description', 'main_image', 'mini_image']
    list_display_links = ['title']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']


@admin.register(Service)
class ServiceAdmin(CustomTranslationAdmin):
    list_display = ['title', 'description', 'image']
    list_display_links = ['title']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']


@admin.register(OurResult)
class OurResultAdmin(CustomTranslationAdmin):
    list_display = ['title', 'number', 'icon']
    list_display_links = ['title']
    list_filter = ['title', 'number', 'icon']
    search_fields = ['title', 'number']


@admin.register(History)
class HistoryAdmin(CustomTranslationAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']
    list_filter = ['title', 'description', ]
    search_fields = ['title', 'description']


@admin.register(Management)
class ManagementAdmin(CustomTranslationAdmin):
    list_display = ['image', "fullname", "position", "admission_days"]
    list_display_links = ['fullname']
    list_filter = ['fullname', "position"]
    search_fields = ['fullname', "position"]


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display_links = ['title', ]
    list_display = ['title', "icon"]
    list_filter = ['title', ]
    search_fields = ['title', ]


admin.site.register([
    Gallery,
    Contact,
    # SocialLink,
    BlogSocialLink
])
