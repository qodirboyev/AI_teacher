from django.urls import path
from .views import courses,lesson_chat_view

urlpatterns = [
    path('', courses, name='courses'),
    path('lesson_chat/', lesson_chat_view, name='lesson_chat'),
]