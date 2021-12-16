from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Team

# Create your views here.


class TeamList(ListView):
    model = Team
    context_object_name = 'team'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['team'].count()

        return context

class TeamDetail(DetailView):
    model = Team
    context_object_name = 'team_member'
    template_name = 'base/team.html'


class TeamCreate(CreateView):
    model = Team
    fields = '__all__'
    success_url = reverse_lazy('teamList')

class TeamUpdate(UpdateView):
    model = Team
    context_object_name = 'team_member'
    fields = '__all__'
    success_url = reverse_lazy('teamList')

class DeleteView(DeleteView):
    model = Team
    context_object_name = 'team_member'
    success_url = reverse_lazy('teamList')
