from . models import ArmyShop
from .models import Course
from .forms import CourseForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


def main(request):
    return HttpResponse('<b>Main</b>')


def insert(request):
    Course(name='데이터 분석', cnt=30).save()
    Course(name='데이터 수립', cnt=20).save()
    Course(name='웹개발', cnt=25).save()
    Course(name='인공지능', cnt=20).save()
    return HttpResponse('<u>Insert</u>')


def show(request):
    c = Course.objects.all()
    # result = ''
    # for c in course:
    #     result += '%s %s <br>' % (c.name, c.cnt)
    return render(
        request, 'secondapp/show.html',
        {'data': c}
    )


def army_shop(request):
    prd = request.GET.get('prd')
    shop = ArmyShop.objects.filter(name__contains=prd)
    result = ['%s %s %s<br>' % (i.year, i.month, i.name) for i in shop]
    return HttpResponse(''.join(result))


def army_shop2(request, year, month):
    shop = ArmyShop.objects.filter(year=year, month=month)

    # result = ''
    # for i in shop :
    #     result += '%s %s %s<br>' % (i.year, i.month, i.name)
    result = ['%s %s %s<br>' % (i.year, i.month, i.name) for i in shop]

    return HttpResponse(''.join(result))


@csrf_exempt
def ajaxGet(request):
    c = Course.objects.all()
    data = []
    for a in c:
        d = model_to_dict(a)
        data.append(d)
    return JsonResponse(data, safe=False)


def ajaxExam(request):
    return render(request, 'secondapp/exam.html')


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('secondapp:course_create')
    else:
        form = CourseForm()
    return render(request, 'secondapp/course_create.html', {'form': form})
