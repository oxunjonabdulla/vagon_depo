from django.shortcuts import render


def service_view(request):
    return render(
        request=request,
        template_name="app/service/service.html"
    )


def service_details(request):
    return render(request=request,
                  template_name="app/service/service_details.html")
