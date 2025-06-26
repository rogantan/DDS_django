from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def categories(request):
    return render(request, 'main/categories.html')


def statuses(request):
    return render(request, 'main/statuses.html')


def subcategories(request):
    return render(request, 'main/subcategories.html')


def types(request):
    return render(request, 'main/types.html')
