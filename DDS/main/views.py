from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Status, Subcategory, Category, DDS, Type


def index(request):
    ddes = DDS.objects.all()
    filters = {}
    if request.GET.get('date_from'):
        filters['date__gte'] = request.GET['date_from']
    if request.GET.get('date_to'):
        filters['date__lte'] = request.GET['date_to']
    if request.GET.get('status'):
        filters['status_id'] = request.GET['status']
    ddes = ddes.filter(**filters)
    categories = Category.objects.all()
    types = Type.objects.all()
    statuses = Status.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'main/index.html', {"ddes": ddes, "categories": categories,
                                               "types": types, "statuses": statuses, "subcategories": subcategories})


def to_add_dds(request):
    statuses = Status.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'main/add_dds.html', {"statuses": statuses, "subcategories": subcategories})


def add_dds(request):
    if request.method == "POST":
        dds = DDS()
        dds.amount = request.POST.get("amount")
        dds.subcategory_id = request.POST.get("subcategory")
        dds.status_id = request.POST.get("status")
        dds.comment = request.POST.get("comment")
        dds.save()
    return HttpResponseRedirect("/")


def edit_dds(request, id):
    try:
        dds = DDS.objects.get(id=id)
        if request.method == "POST":
            dds.date = datetime.fromisoformat(request.POST.get("date"))
            dds.amount = request.POST.get("amount")
            dds.subcategory_id = request.POST.get("subcategory")
            dds.status_id = request.POST.get("status")
            dds.comment = request.POST.get("comment")
            dds.save()
            return HttpResponseRedirect("/")
        else:
            statuses = Status.objects.all()
            subcategories = Subcategory.objects.all()
            formatted_date = dds.date.strftime("%Y-%m-%dT%H:%M")
            return render(request, 'main/edit_dds.html', {"statuses": statuses, "subcategories": subcategories, "dds": dds, "formatted_date": formatted_date})
    except DDS.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")


def delete_dds(request, id):
    try:
        dds = DDS.objects.get(id=id)
        dds.delete()
        return HttpResponseRedirect("/")
    except DDS.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")


def categories(request):
    categories = Category.objects.all()
    types = Type.objects.all()
    return render(request, 'main/categories.html', {"categories": categories, "types": types})


def add_category(request):
    if request.method == "POST":
        category = Category()
        category.name = request.POST.get("name")
        category.type_id = request.POST.get("type")
        category.save()
    return HttpResponseRedirect("/categories")


def edit_category(request, id):
    try:
        category = Category.objects.get(id=id)
        if request.method == "POST":
            category.name = request.POST.get("name")
            category.type_id = request.POST.get("type")
            category.save()
            return HttpResponseRedirect("/categories")
        else:
            types = Type.objects.all()
            return render(request, 'main/edit_category.html', {"types": types, "category": category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Категория не найдена</h2>")


def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect("/categories")
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Категория не найдена</h2>")


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
    subcategories = Subcategory.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/subcategories.html', {"subcategories": subcategories, "categories": categories})


def add_subcategory(request):
    if request.method == "POST":
        subcategory = Subcategory()
        subcategory.name = request.POST.get("name")
        subcategory.category_id = request.POST.get("category")
        subcategory.save()
    return HttpResponseRedirect("/subcategories")


def edit_subcategory(request, id):
    try:
        subcategory = Subcategory.objects.get(id=id)
        categories = Category.objects.all()
        if request.method == "POST":
            subcategory.name = request.POST.get("name")
            subcategory.category_id = request.POST.get("category")
            subcategory.save()
            return HttpResponseRedirect("/subcategories")
        else:
            return render(request, 'main/edit_subcategory.html', {"subcategory": subcategory, "categories": categories})
    except Subcategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Подкатегория не найдена</h2>")


def delete_subcategory(request, id):
    try:
        subcategory = Subcategory.objects.get(id=id)
        subcategory.delete()
        return HttpResponseRedirect("/subcategories")
    except Subcategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Подкатегория не найдена</h2>")


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


def edit_type(request, id):
    try:
        type = Type.objects.get(id=id)
        if request.method == "POST":
            type.name = request.POST.get("name")
            type.save()
            return HttpResponseRedirect("/types")
        else:
            return render(request, 'main/edit_type.html', {"type": type})
    except Type.DoesNotExist:
        return HttpResponseNotFound("<h2>Тип не найден</h2>")


def delete_type(request, id):
    try:
        type = Type.objects.get(id=id)
        type.delete()
        return HttpResponseRedirect("/types")
    except Type.DoesNotExist:
        return HttpResponseNotFound("<h2>Тип не найден</h2>")