from django.shortcuts import render,redirect
from chat.models import ChatMessage, Thread
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

def read_message(request,pk):
    message = ChatMessage.objects.get(pk=pk)
    message.read = True
    message.save()
    return redirect("chat:draft")