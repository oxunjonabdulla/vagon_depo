from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models import Banner, Blog, About, Service, OurResult


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
    list_display = ['title', 'description', "text", 'image']
    list_display_links = ['title']
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














