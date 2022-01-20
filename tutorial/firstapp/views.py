from django.shortcuts import render
from django.http import HttpResponse


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
