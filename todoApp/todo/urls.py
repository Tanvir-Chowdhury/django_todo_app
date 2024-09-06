from django.contrib import admin
from django.urls import path
from todoApp import settings
from django.conf.urls.static import static
from todo import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('del/<int:task_id>', views.remove_task, name = "remove"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)