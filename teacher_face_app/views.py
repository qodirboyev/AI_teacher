from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class Teacher_faceView(TemplateView):
    template_name = 'teacher_face_app/teacher_face.html'