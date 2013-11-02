from models import TodoItem
from rest_framework import viewsets
from django.shortcuts import render_to_response
from django.template import RequestContext

from serializers import TodoItemSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


def home(request, template_name="index.html"):
    """
A index view.
"""
    return render_to_response(template_name,
                              context_instance=RequestContext(request))
