from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import UpdateView, CreateView, ListView, FormView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from twistter.forms import UserModelForm, EditUserModelForm, TextForm, Source, BiografiaForm
from twistter.models import PostText, Profile


# Create your views here.



class DashBoardDetail(LoginRequiredMixin, ListView):
    template_name = 'twistter/dashboard.html'
    model = PostText
    form_class = Source

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(pk=self.request.user.pk)
        context['form_bio'] = BiografiaForm(instance=self.request.user.profile)
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        users = list(self.request.user.profile.friends.values_list('pk',flat=True))+[self.request.user.pk]
        return queryset.filter(user__id__in=users)


class MakeFriends(LoginRequiredMixin, View):

    def get(self, request, user_pk, friend_pk):
        user = User.objects.get(pk=user_pk)
        friend = User.objects.get(pk=friend_pk)
        user.profile.friends.add(friend)
        return HttpResponseRedirect(reverse_lazy('dashboard'))


class RemoveFriends(LoginRequiredMixin, View):

    def get(self, request, user_pk, friend_pk):
        user = User.objects.get(pk=user_pk)
        friend = User.objects.get(pk=friend_pk)
        user.profile.friends.remove(friend)
        return HttpResponseRedirect(reverse_lazy('dashboard'))


class PostCreate(LoginRequiredMixin, CreateView):
   form_class = TextForm
   success_url = reverse_lazy('dashboard')

   def form_valid(self, form):
       candidate = form.save(commit=False)
       candidate.user = self.request.user
       candidate.save()
       return HttpResponseRedirect(self.success_url)


class SignUp(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = UserModelForm


class EditUser(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    success_url = reverse_lazy('dashboard')
    form_class = EditUserModelForm
    model = User


# class EditBiografia(LoginRequiredMixin, UpdateView):
#     form_class = BiografiaForm
#     model = Profile

#     def form_valid(self, **kwargs):
#         super().form_valid(**kwargs)
#         return HttpResponseRedirect(reverse_lazy('dashboard'))

class Search(LoginRequiredMixin, ListView, FormView):
    template_name = 'search.html'
    form_class = Source
    model = User

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        name = self.request.GET.get('user')
        if name:
            queryset = User.objects.filter(username__icontains=name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('user')
        return context



class Profile(LoginRequiredMixin, DetailView):
    template_name = 'profile.html'
    model = User


def edit_password(request):
    template_name = 'edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    sucess_url = reverse_lazy('login')
    return render(request, template_name, context)


class Home(View):
    template_name = 'home.html'
    def get(self, request, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, **kwargs):
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            return HttpResponseRedirect(reverse_lazy('signup'))

#     form = EditUserModelForm()
#     context = {}
#     if request.method == 'POST':
#             form = EditUserModelForm(request.POST, instance=request.user)
#             if form.is_valid():
#                     form.save()
#                     form = EditUserModelForm(instance=request.user)
#                     context['sucess'] = True
#     else:
#             form = EditUserModelForm(instance=request.user)
#     context['form'] = form
#     return render(request, template_name, context)


# class EditPassword(LoginRequiredMixin, UpdateView):
#     template_name = 'edit_password.html'
#     sucess_url = reverse_lazy('dashboard')
#     form_class = PasswordChangeForm
#     model = User