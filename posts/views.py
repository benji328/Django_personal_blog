from django.shortcuts import render


def covid19_map(request):
    return render(request, "posts/covid19_map.html")


def data_storage(request):
    return render(request, "posts/data_storage.html")


def projects(request):
    return render(request, "posts/projects.html")
