from django.urls import path
from .views import SignUpForm

urlpatterns = [
    path('signup/', SignUpForm.as_view(), name='signup'),
]