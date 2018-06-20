from django.shortcuts import render, HttpResponse
from app.models import UserRecord
# Create your views here.
def first(request):
    return HttpResponse('麻瓜编程')

def second(request):
    context = {}
    # 逻辑处理
    return render(request, 'one.html', context)

def third(request):
    context = {}
    # ur = []
    # from faker import Factory
    # fake = Factory.create()
    # for i in range(1,31):
    #     u = UserRecord(username=fake.user_name(), address=fake.address())
    #     u.save()
    ur = UserRecord.objects.all()
    context['ur'] = ur
    return render(request, 'two.html', context)