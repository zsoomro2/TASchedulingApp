from django.contrib import admin
from django.urls import path
import views
from views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
]