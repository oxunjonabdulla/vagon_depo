from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from app.models import Blog


def blog_view(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, per_page=6)
    page_number = request.GET.get('page', 1)
    blog_list = paginator.get_page(page_number)
    return render(request=request,
                  template_name="app/blog/blog.html",
                  context={"blogs": blog_list})


def blog_details(request, news):
    blog = get_object_or_404(Blog, slug=news)
    latest_blogs = Blog.objects.order_by("-created_at")[:3]
    return render(request=request,
                  template_name="app/blog/blog_details.html",
                  context={"blog": blog,
                           "latest_blogs": latest_blogs})
