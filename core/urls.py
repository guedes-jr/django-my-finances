from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('buttons/', views.buttons, name='buttons'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('typography/', views.typography, name='typography'),
    path('forms/', views.forms, name='forms'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
    path('icons/', views.icons, name='icons'),
    path('pages/login', views.login, name='login'),
    path('pages/register', views.register, name='register'),
    path('pages/404', views.not_found, name='not_found'),
    path('pages/505', views.internal_server_error, name='internal_server_error'),
    path('pages/blankpage', views.blankpage, name='blankpage'),
    path('pages/documentation', views.documentation, name='documentation'),
]