from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def contact(request):

    if request.method == "POST":
        json_str = request.body
        result = json.loads(json_str)
        return JsonResponse({'result': result})
    else:
        data = {'name': "张三", 'gender': [{'name': '男', 'value': '0', 'checked': True},
                                         {'name': '女', 'value': '1', 'checked': False}],
                'skills': [{'name': 'HTML', 'value': 'html', 'checked': True},
                               {'name': 'CSS', 'value': 'css', 'checked': True},
                               {'name': 'JAVASCRIPT', 'value': 'js', 'checked': False},
                               {'name': 'PYTHON', 'value': 'python', 'checked': False}],
                'option': "测试"
                }
        return JsonResponse({'data': data})
