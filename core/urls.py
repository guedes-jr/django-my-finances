from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('portifolio/', views.portifolio, name='portifolio'),
    path('portifolio/update/<int:id>', views.update_portifolio, name='update_portifolio'),
    path('portifolio/delete/<int:id>', views.delete_portifolio, name='delete_portifolio'),
    path('goal/', views.goal, name='goal'),
    path('goal/update/<int:id>', views.update_goal, name='update_goal'),
    path('goal/delete/<int:id>', views.delete_goal, name='delete_goal'),
    path('icons/', views.icons, name='icons'),
    path('pages/documentation', views.documentation, name='documentation'),
]