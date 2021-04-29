from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('on-campus/', views.oncampus, name='on-campus'),
    path('off-campus/', views.offcampus, name='off-campus'),
    path('intern/', views.intern, name='intern'),
]