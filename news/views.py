from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.views.generic import UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Article
from django.urls import reverse_lazy

# Create your views here.



class NewsListView(ListView):
    model = Article
    template_name = 'news_list.html'


class NewUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = 'new_edit.html'
    fields = ['title','qisqacha','body','photo']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class NewDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'new_delete.html'
    success_url = reverse_lazy('news')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class NewDetailView(DetailView):
    model = Article
    template_name = 'new_detail.html'


class NewCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Article
    template_name = 'new_create.html'
    fields = ['title','qisqacha','body','photo',]

    ## mualifni avtomatik yaratganni oladi
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
