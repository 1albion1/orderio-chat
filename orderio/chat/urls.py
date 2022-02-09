from django.urls import path
from chat import views
app_name = "chat"
urlpatterns = [
    path("",views.index,name="index"),
    path("draft",views.draft,name="draft"),
    path("read_message/<int:pk>",views.read_message,name="read_message"),
    path("create_thread/<int:pk>",views.create_thread,name="create_thread")
]
