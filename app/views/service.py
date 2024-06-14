from django.shortcuts import render

from app.models import Service


def service_view(request):
    services = Service.objects.all()
    return render(
        request=request,
        template_name="app/service/service.html",
        context={"services": services}
    )


def service_details(request):
    return render(request=request,
                  template_name="app/service/service_details.html")
