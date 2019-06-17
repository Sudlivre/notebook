from django.shortcuts import render

# Create your views here.
from home.tasks import celery_test


def index(request):
    if request.method == 'GET':
        # 调用异步任务函数
        celery_test.delay()
        return render(request, 'index.html')