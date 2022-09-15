from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Home, CategoryView, ServiceView, CategoryNew

urlpatterns = [
    path('', Home.as_view() , name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('categories/', CategoryView.as_view(), name='category_list'),
    path('categories/new', CategoryNew.as_view(), name='category_new'),
    path('services/', ServiceView.as_view(), name='service_list'),
]