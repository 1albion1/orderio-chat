from chat.models import Thread
def threads_list(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread')
    unread = 0
    for thread in threads:
        if (not thread.chatmessage_thread.last().read) and (thread.chatmessage_thread.last().user!=request.user):
            unread +=1
    return{
            "threads_list" : threads,
            "unread":unread
        }