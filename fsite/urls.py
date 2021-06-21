from django.urls import path
from . import views
from .views import ShopLoginView, profile, ShopLogoutView, RegisterUserView, RegisterDoneView, profile_post_add, \
    BrandListView, post

app_name = 'main'

urlpatterns = [
    path('accounts/profile/add', profile_post_add, name='profile_post_add'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', ShopLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', ShopLoginView.as_view(), name='login'),
    path('post/<int:pk>/', post, name='post_main'),
    path('<slug:slug>/', BrandListView, name='brand'),
    path('', views.home),
]
