from django.urls import path
from chat import views
app_name = "chat"
urlpatterns = [
    path("",views.index,name="index"),
    path("draft",views.draft,name="draft"),
    
]
