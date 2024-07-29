from django.urls import path
from .views import signup, signout, access

urlpatterns = [
    path('login/', access, name='login'),
    path('logout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
]
