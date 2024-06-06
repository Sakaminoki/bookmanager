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

    # return HttpResponse('ok')
    # request, template_name, context=None
    # request,请求
    # template name,模板名字
    # context=None,将视图中的数据传递给html模板，采用{{字典的键名}}显示数据

    # 模拟数据查询
    context={
        'name':'context使用'
    }

    return render(request, 'book/index.html',context=context)
