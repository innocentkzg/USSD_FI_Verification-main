from django.urls import path
from . import views
from .views import CategoryDetailView, CategoryView, InstitutionDetailView, InstitutionView, RoleDetailView, RoleView, UserDetailView, UserView, login, save_user

urlpatterns = [
    # path('api/ussd/', ussd, name='ussd'), # type: ignore
    # path('api/verify_institution/', verify_institution, name='verify_institution'), # type: ignore
    # Category URLs
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Institution URLs
    path('institutions/', InstitutionView.as_view(), name='institution-list'),
    path('institutions/<int:pk>/', InstitutionDetailView.as_view(), name='institution-detail'),

    # User URLs
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Role URLs
    path('roles/', RoleView.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),

     path('user/', save_user, name='save_user'),

     path('login/', login, name='login'),
]

