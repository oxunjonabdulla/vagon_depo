from modeltranslation.translator import TranslationOptions, register

from .models import Banner, Blog, About, Service, OurResult


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', "text")


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(OurResult)
class OurResultTranslationOptions(TranslationOptions):
    fields = ('title',)


















