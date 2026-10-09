from django.urls import path
from .views import Teacher_faceView

urlpatterns = [
    path('', Teacher_faceView.as_view(), name='teacher_face'),
]