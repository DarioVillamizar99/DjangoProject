from django.urls import path
from .views import TaskUserView

app_name = "tasks"

urlpatterns = [
    path('', TaskUserView.as_view(), name="home"),
]
