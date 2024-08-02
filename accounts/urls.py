from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.access, name='login'),
    path('logout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/delete/<int:id>', views.delete_perfil, name='delete_perfil'),
]
