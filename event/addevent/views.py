# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json

# Create your views here.
from .forms import Model_Event_Form
from .models import Model_Event

def sample(request):
    content={}
    qs=Model_Event.objects.all()
    if request.user.is_authenticated:
        user=request.user
        dic_for={}
        for x in qs:
            cur=x.is_liked.filter(id=user.id).exists()
            dic_for[x]=cur
    else:
        return redirect('login')
    content['fgh']=dic_for
    print(dic_for.keys(),dic_for.values())
    for i in range(len(qs)):
        print(qs[0].event_name)
    return render(request, 'accounts/index.html',content)


class EventView(FormView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EventView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        content['form'] = Model_Event_Form
        return render(request, 'event/event1.html', content)

    def post(self, request):
        content = {}
        form = Model_Event_Form(request.POST,request.FILES)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.user = request.user
            ans.save()
        else:
            print("ERROROROR")
        content['form'] = Model_Event_Form()
        return render(request, 'event/event2.html', content)


class Like(FormView):
    def post(self, request):
        user = request.user
        pk = request.POST.get('pk')
        ans = Model_Event.objects.get(id=pk)
        psta = ans.is_liked.filter(id=request.user.id).exists()
        if ans.is_liked.filter(id=request.user.id).exists():
            print("inside if")
            ans.is_liked.remove(user)
            message = 'You disliked the answer'
        else:
            ans.is_liked.add(user.id)
            message = 'You liked this answer'
        yu = ans.count_likes()
        ctx = {'is_liked_count': yu, 'message': message}
        print("hello2")
        sta = ans.is_liked.filter(id=request.user.id).exists()

        return JsonResponse({'ctx': yu, "sta": sta, "psta": psta}, safe=False)
