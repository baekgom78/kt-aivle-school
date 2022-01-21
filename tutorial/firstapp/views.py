import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index1(request):
    return HttpResponse('<u>Hello</u>')


def index2(request):
    return HttpResponse('<u>Hi</u>')

def main(request):
    return HttpResponse('<u>Main</u>')

def home(request):
    return HttpResponse('<b>Home</b>')

from .models import Curriculum

def insert(request):
    Curriculum.objects.create(name='linux')
    c = Curriculum(name='python')
    c.save()
    Curriculum(name='python').save()
    Curriculum(name='django').save()
    return HttpResponse('ok')


def show(request):
    curriculum = Curriculum.objects.all()
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)

    return render(request, 'firstapp/show.html', 
                  {'score': 100, 'data' : curriculum}
                  )
    
def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)

def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')

def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')

def req_ajax4(request):
    return render(request, 'firstapp/ajax4.html')

@csrf_exempt
def req_json(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    return JsonResponse(data)


def tag(request):
    persons = [
        {'num': 1, 'name': 'Park', 'score': 100},
        {'num': 2, 'name': 'Choi', 'score': 70},
        {'num': 3, 'name': 'Kim', 'score': 80}
    ]
    animals = ['Cat2', 'Dog']
    context = {
        'persons': persons,
        'animals': animals 
    }
    return render(request, 'firstapp/tag.html', context)

def custom_filter(request):
    context = { 'price': 39800.5 }
    return render(request, 'firstapp/custom_filter.html', context)

def template(request):
    return render(request, 'firstapp/template.html')