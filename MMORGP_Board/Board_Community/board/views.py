from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Response
from .filters import PostFilter
from .forms import PostForm, ResponseForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User


class PostsList(ListView):
    model = Post
    ordering = '-datetime_in'
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_template_names(self):
        if self.request.path == '/board/search/':
            return 'search.html'
        return 'board.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'ad.html'
    context_object_name = "post"


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'ad_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'ad_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_post',)
    model = Post
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('post_list')


class ResponseList(ListView):
    model = Response
    ordering = '-time_response'
    template_name = 'response.html'
    context_object_name = "response"
    paginate_by = 10


class ResponseCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_response',)
    form_class = ResponseForm
    model = Response
    template_name = 'response_edit.html'
    success_url = reverse_lazy('response_list')


class ResponseDelete(DeleteView):
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('Response_list')


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.Post:
            user = User.objects.filter(code=request.Post['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'users/invalid_code.html')
            return redirect('account_login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
