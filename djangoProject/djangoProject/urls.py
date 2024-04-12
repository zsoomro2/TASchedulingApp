from django.contrib import admin
from django.urls import path
from project_app.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
]