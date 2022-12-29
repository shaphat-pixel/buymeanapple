from django.urls import path, re_path

from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView
from . import views



urlpatterns = [
	path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('profile/', views.ProfileView, name = "user-profile"),
    path('withdrawal/', views.WithdrawalView, name = "withdrawal"),
    path('withdrawal-list/', views.WithdrawalListView, name = "withdrawal-list"),
    path('page-list/', views.UserPageListView, name = 'page-list'),
    path('page-create/<str:pk>', views.UserPageCreateView, name = 'page-create'),
    path('<slug:slug>/', views.UserPageView, name = "user-page"),
     


    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),
]