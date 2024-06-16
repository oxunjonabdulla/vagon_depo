from django.shortcuts import render

from app.models import Service


def service_view(request):
    services = Service.objects.all()
    return render(
        request=request,
        template_name="app/service/service.html",
        context={"services": services}
    )


def service_details(request, id):
    service = Service.objects.filter(id=id).first()
    services = Service.objects.all()
    services_list = []
    for i in services:
        if service !=i:
            services_list.append(i)
    return render(request=request,
                  template_name="app/service/service_details.html",
                  context={"service": service,
                           "services":services_list})
