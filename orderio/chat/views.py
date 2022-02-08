from django.shortcuts import render
from chat.models import Thread
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread')
    context = {
        "threads" : threads
    }
    return render(request,'chat/index.html',context)
@login_required
def draft(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread')
    context = {
        "threads" : threads
    }
    return render(request,"chat/draft.html",context)