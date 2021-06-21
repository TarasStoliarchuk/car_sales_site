from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post, Brands
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm, PostForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


def home(request):
    all_posts = Post.objects.all()
    all_brands = Brands.objects.all()
    return render(request, 'layout/basic.html', {'all_brands': all_brands, 'all_posts': all_posts})


class ShopLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(request):
    fst = Post.objects.filter(salesperson=request.user.pk)
    context = {'fst': fst}
    return render(request, 'main/profile.html', context)


class ShopLogoutView(LogoutView, LoginRequiredMixin):
    template_name = 'main/logout.html'


class RegisterUserView(CreateView):
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


@login_required
def profile_post_add(request):
    erorr = ''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:profile')
        else:
            erorr = 'Не верно введеные даные'
    else:
        form = PostForm(initial={'salesperson': request.user.pk})
    context = {'form': form, 'erorr': erorr}
    return render(request, 'main/profile_post_add.html', context)


def BrandListView(request, slug):
    bb = Brands.objects.filter(slug=slug)
    all_posts = Post.objects.filter(brand__in=bb)
    context = {
        'bb': bb,
        'all_posts': all_posts
    }
    return render(request, 'main/brand.html', context)


def post(request, pk):
    poost = Post.objects.filter(id=pk)
    context = {
        'poost': poost
    }
    return render(request, 'main/post_main.html', context)



