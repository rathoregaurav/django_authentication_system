from django.urls import path
from art.views import Registration, Login, UserDetails, Logout

urlpatterns = [
    path('registration/', Registration.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('details/', UserDetails.as_view()),
    path('logout/', Logout.as_view(), name='logout_user'),

    
]