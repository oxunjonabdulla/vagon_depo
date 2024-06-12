from django.shortcuts import render


def blog_view(request):
    return render(request=request,
                  template_name="app/blog/blog.html")


def blog_details_view(request):
    return render(request=request,
                  template_name="app/blog/blog_details.html")
