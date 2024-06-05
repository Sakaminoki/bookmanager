from django.shortcuts import render

# Create your views here.
"""
视图，就是python函数
视图函数的2个要求：
    1.视图函数第一个参数是接受请求
"""
from django.http import HttpRequest, HttpResponse
# 通过localhost:8000/index/来访问视图函数
def index(request):

    return HttpResponse('ok')
