from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('api/employee/', views.EmployeeListCreate.as_view()),
    path('api/employee/<int:pk>/', views.EmployeeRetrieveUpdateDestroy.as_view()),
]
