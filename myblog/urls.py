"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from contract.views import Contract
from django.conf.urls import handler404

from myapp.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    
)

urlpatterns = [
    #path('home/',home, name = 'home'),
    path('about/', about, name = 'about'),
    path('register/', user_views.register, name = 'register'),
    path('profile/', user_views.profile, name='profile'),
    path('admin/', admin.site.urls),
    # path('error/', user_views.error_page, name='error'),

    #cbv
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name = 'post_details.html'), name='post-detail'),
    path('post/new/', PostCreateView.as_view(template_name = 'post_form.html'), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name = 'post_form.html'), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name = 'post_delete.html'), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),

    #password_reset_view
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
         path('contract/', Contract, name = 'contract'),
        
        
]
# handler404 = user_views.handler404
# handler500 = user_views.handler404
