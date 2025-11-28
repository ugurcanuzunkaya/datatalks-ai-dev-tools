from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todos"
    ordering = ["-created_at"]


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description", "due_date"]
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo-list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "description", "due_date", "is_completed"]
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo-list")


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy("todo-list")


def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect("todo-list")
