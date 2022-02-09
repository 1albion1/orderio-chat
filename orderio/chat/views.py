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
    thread  = message.thread
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread')
    if thread.first_person==request.user:
        active_user_id = thread.second_person.id
    else:
        active_user_id = thread.first_person.id
    request.session["active_user_id"]=active_user_id
    context = {
        "active_user_id" : active_user_id,
        "threads" : threads
    }
    return redirect("chat:draft")