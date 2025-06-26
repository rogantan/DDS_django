from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Status, Subcategory, Category, DDS, Type


def index(request):
    return render(request, 'main/index.html')


def categories(request):
    return render(request, 'main/categories.html')


def add_category(request):
    pass


def edit_category(request):
    pass


def statuses(request):
    statuses = Status.objects.all()
    return render(request, 'main/statuses.html', {'statuses': statuses})


def add_status(request):
    if request.method == 'POST':
        if len(request.POST.get("name")) == 0:
            return HttpResponseRedirect("/statuses")
        status = Status()
        status.name = request.POST.get("name")
        status.save()
    return HttpResponseRedirect("/statuses")


def edit_status(request, id):
    try:
        status = Status.objects.get(id=id)
        if request.method == "POST":
            status.name = request.POST.get("name")
            status.save()
            return HttpResponseRedirect("/statuses")
        else:
            return render(request, 'main/edit_status.html', {"status": status})
    except Status.DoesNotExist:
        return HttpResponseNotFound("<h2>Статус не найден</h2>")


def delete_status(request, id):
    try:
        status = Status.objects.get(id=id)
        status.delete()
        return HttpResponseRedirect("/statuses")
    except Status.DoesNotExist:
        return HttpResponseNotFound("<h2>Статус не найден</h2>")


def subcategories(request):
    return render(request, 'main/subcategories.html')


def add_subcategory(request):
    pass


def edit_subcategory(request):
    pass


def delete_subcategory(request):
    pass


def types(request):
    types = Type.objects.all()
    return render(request, 'main/types.html', {"types": types})


def add_type(request):
    if request.method == "POST":
        if len(request.POST.get("name")) == 0:
            return HttpResponseRedirect("/types")
        type = Type()
        type.name = request.POST.get("name")
        type.save()
    return HttpResponseRedirect("/types")


def edit_type(request):
    pass


def delete_type(request):
    pass