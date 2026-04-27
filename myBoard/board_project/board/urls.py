from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'groups', views.HabitGroupViewSet, basename='group')
router.register(r'todos',  views.TodoViewSet,       basename='todo')

urlpatterns = [
    path('',       views.index,    name='index'),
    path('api/',   include(router.urls)),
]
