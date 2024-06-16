from django.urls import path

from app.views.blog import blog_view, blog_details
from app.views.other import index_view, about_view, contact_view, bad_request_view, management_view
from app.views.service import service_view, service_details

urlpatterns = [
    path('', index_view, name='index'),
    path("about/", about_view, name="about"),
    path("service/", service_view, name="service"),
    path("service_details/<int:id>/", service_details, name="service_details"),
    path("blog/", blog_view, name="blog"),
    path("blog_details/<slug:news>/", blog_details, name="blog_details"),
    path("contact/", contact_view, name="contact"),
    path("management/", management_view, name="management"),
    path("404/", bad_request_view, name="404"),

]
