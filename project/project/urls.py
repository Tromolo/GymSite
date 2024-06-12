"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('users/', views.users, name='users'),
    path('trainers/', views.trainers, name='trainers'),
    path('trainers/<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail' ),
    path('assign_trainer/<int:user_id>/<int:trainer_id>/', views.assign_trainer, name='assign_trainer'),
    path('create_training_plan/<int:trainer_id>/', views.create_training_plan, name='create_training_plan'),
    path('user_training_plans/<int:user_id>/', views.user_training_plans, name='user_training_plans'),
    path('create_diet_plan/<int:trainer_id>/', views.create_diet_plan, name='create_diet_plan'),
    path('user_diet_plans/<int:user_id>/', views.user_diet_plans, name='user_diet_plans'),
    path('create_goal/<int:user_id>/', views.create_goal, name='create_goal'),
    path('user_show_goal/<int:user_id>/', views.user_show_goal, name='user_show_goal'),
    path('update_goal/<int:goal_id>/', views.update_goal, name='update_goal'),
    path('delete_goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),
    path('create_payment/<int:user_id>/', views.create_payment, name= 'create_payment'),
    path('user_show_payment/<int:user_id>/', views.user_show_payment, name='user_show_payment'),
    path('update_payment/<int:payment_id>/', views.update_payment, name='update_payment'),
    path('delete_payment/<int:payment_id>/', views.delete_payment, name='delete_payment'),
    path('trainer_show_training_plan/<int:trainer_id>/', views.trainer_show_training_plan, name='trainer_show_training_plan'),
    path('trainer_show_diet_plan/<int:trainer_id>/', views.trainer_show_diet_plan, name='trainer_show_diet_plan'),
]
