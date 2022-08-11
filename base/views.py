from django.views.generic.list import ListView
from .models import task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class task_list(ListView):
    model = task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = task.objects.filter(completed=False).count()
        searched_task = self.request.GET.get('search-area') or ""
        if searched_task:
            context['tasks'] = task.objects.filter(
                title__icontains=searched_task)
        context['searched'] = searched_task
        return context


class task_detail(DetailView):
    model = task
    template_name = 'base/task_detail.html'
    context_object_name = 'tasks'


class create_task(CreateView):
    model = task
    fields = ['title', 'content', 'due_date', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(create_task, self).form_valid(form)


class task_update(UpdateView):
    model = task
    fields = ['title', 'content', 'due_date', 'completed']
    success_url = reverse_lazy('tasks')


class task_delete(DeleteView):
    model = task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_delete.html'


class home(UpdateView):
    success_url = reverse_lazy('tasks')
