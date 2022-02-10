from django.shortcuts import render,redirect
from chat.models import ChatMessage, Thread
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()
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
    threads = Thread.objects.by_user(user=request.user).order_by("-updated").prefetch_related('chatmessage_thread')
    context = {
        "threads" : threads,
        "users" : User.objects.all()
    }
    if request.user.role.name == 'manager':
        return render(request,"chat/manager-chat.html",context)
    else:
        return render(request,"chat/draft.html",context)

def read_message(request,pk):
    message = ChatMessage.objects.get(pk=pk)
    message.read = True
    message.save()
    thread  = message.thread
    
    if thread.first_person==request.user:
        active_user_id = thread.second_person.id
    else:
        active_user_id = thread.first_person.id
    request.session["active_user_id"]=active_user_id
   
    return redirect("chat:draft")

def create_thread(request,pk):
    try:
        second_person=User.objects.get(pk=pk)
        thread = Thread(first_person=request.user,second_person=second_person)
        thread.save()
        cm = ChatMessage(thread=thread,user=request.user,message=f"Hi {second_person.username}")
        cm.save()
    except:
        pass
    return redirect("chat:draft")