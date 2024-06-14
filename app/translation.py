from modeltranslation.translator import TranslationOptions, register

from .models import Banner, Blog, About, Service, OurResult, History, Management


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', "text","slug")


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(OurResult)
class OurResultTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ("title", "description",)


@register(Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ("position", "admission_days" ,)
