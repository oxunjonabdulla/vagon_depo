from django.urls import path

from app.views.blog import blog_view, blog_details_view
from app.views.other import index_view, about_view, contact_view, bad_request_view
from app.views.service import service_view, service_details

urlpatterns = [
    path('', index_view, name='index'),
    path("about/", about_view, name="about"),
    path("service/", service_view, name="service"),
    path("service_details/", service_details, name="service_details"),
    path("blog/", blog_view, name="blog"),
    path("blog_details/", blog_details_view, name="blog_details"),
    path("contact/", contact_view, name="contact"),
    path("404/", bad_request_view, name="404")
]
