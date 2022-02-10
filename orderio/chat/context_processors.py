from chat.models import Thread
def threads_list(request):
    try:
        threads = Thread.objects.by_user(user=request.user).order_by("-updated").prefetch_related('chatmessage_thread')
    except:
        threads = ""
        
    try:
        unread = 0
        for thread in threads:
            if (not thread.chatmessage_thread.last().read) and (thread.chatmessage_thread.last().user!=request.user):
                unread +=1
    except:
        unread = 0
    return{
            "threads_list" : threads,
            "unread":unread
        }