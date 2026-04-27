from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from .models import HabitGroup, Todo


# ── Serializers ──────────────────────────────────────────

class TodoSerializer(ModelSerializer):
    class Meta:
        model  = Todo
        fields = ['id', 'text', 'done', 'memo', 'order']


class HabitGroupSerializer(ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model  = HabitGroup
        fields = ['id', 'name', 'icon', 'color', 'order', 'todos']


# ── ViewSets ─────────────────────────────────────────────

class HabitGroupViewSet(viewsets.ModelViewSet):
    queryset           = HabitGroup.objects.all()
    serializer_class   = HabitGroupSerializer
    http_method_names  = ['get', 'post', 'patch', 'delete']

    @action(detail=True, methods=['post'], url_path='todos')
    def create_todo(self, request, pk=None):
        """POST /api/groups/<id>/todos/"""
        group = self.get_object()
        ser   = TodoSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save(group=group)
        return Response(ser.data, status=status.HTTP_201_CREATED)


class TodoViewSet(viewsets.ModelViewSet):
    queryset           = Todo.objects.all()
    serializer_class   = TodoSerializer
    http_method_names  = ['get', 'patch', 'delete']


# ── Template view ─────────────────────────────────────────

def index(request):
    return render(request, 'index.html')
