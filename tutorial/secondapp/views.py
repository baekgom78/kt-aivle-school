from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('<b>Main</b>')

from .models import Course
def insert(request):
    Course(name='데이터 분석', cnt=30).save()
    Course(name='데이터 수립', cnt=20).save()
    Course(name='웹개발', cnt=25).save()
    Course(name='인공지능',cnt=20).save()
    return HttpResponse('<u>Insert</u>')

def show(request):
    c = Course.objects.all()
    # result = ''
    # for c in course:
    #     result += '%s %s <br>' % (c.name, c.cnt)
    return render(
        request, 'secondapp/show.html', 
                  {'data' : c}
                  )

def army_shop(request):
    prd = request.GET.get('prd')
    shop = ArmyShop.objects.filter(name__contains=prd)
    result = [ '%s %s %s<br>' % (i.year, i.month, i.name) for i in shop]
    return HttpResponse(''.join(result))

from . models import ArmyShop    
def army_shop2(request, year, month):
    shop = ArmyShop.objects.filter(year=year, month=month)
    
    # result = ''
    # for i in shop :
    #     result += '%s %s %s<br>' % (i.year, i.month, i.name)   
    result = [ '%s %s %s<br>' % (i.year, i.month, i.name) for i in shop]
    
    return HttpResponse(''.join(result))