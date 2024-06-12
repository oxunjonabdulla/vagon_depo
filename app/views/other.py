from django.shortcuts import render

from app.models import Banner, Blog, About, Service, OurResult


def index_view(request):
    banners = Banner.objects.all()
    latest_blogs = Blog.objects.all()[:3]
    about = About.objects.first()
    services = Service.objects.order_by("-created_at").all()[:3]
    our_results = OurResult.objects.all()[:4]
    return render(request=request,
                  template_name='app/index.html',
                  context={'banners': banners,
                           'latest_blogs': latest_blogs,
                           "about": about,
                           "services": services,
                           "our_results": our_results}
                  )


def about_view(request):
    return render(request=request,
                  template_name="app/about.html")


def contact_view(request):
    return render(request=request,
                  template_name="app/contact.html")


def bad_request_view(request):
    return render(request=request,
                  template_name="app/404.html")


from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
