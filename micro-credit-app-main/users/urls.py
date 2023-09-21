from django.urls import path

from .views import (
    LogIn,
    apply_loan,
    user_logout,
    SignUp,
    profilepage,
    update_profile
)

urlpatterns = [
    path("", LogIn.as_view(), name="login"),
    path("apply_loan/", apply_loan, name="apply_loan"),
    path("logout/", user_logout, name="logout"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("profile/", profilepage, name="profile"),
    path('update/<int:id>/', update_profile,name='update_profile'),
]
