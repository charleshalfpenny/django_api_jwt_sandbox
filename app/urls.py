from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


from . import views
from . import jwt_token_custom

urlpatterns = [
    path('', views.index, name='index'),

    # Token endpoints
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', jwt_token_custom.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),


    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('api/protected/', views.ProtectedView.as_view(), name='protected_view'),


    path('api/employee/', views.EmployeeListCreate.as_view()),
    path('api/employee/<int:pk>/', views.EmployeeRetrieveUpdateDestroy.as_view()),

]
