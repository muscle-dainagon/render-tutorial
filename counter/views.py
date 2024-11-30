from django.shortcuts import render


def index(request):
    """トップページのビュー"""
    return render(request, "counter/index.html")