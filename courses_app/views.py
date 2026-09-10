from multiprocessing import context
from google import genai
from django.shortcuts import render
import os
from google.genai import errors


from courses_app.models import Courses,Lessons


# Create your views here.


def courses(request):
    template_name = 'courses_templates/courses.html'
    direction = request.POST.get("direction")
    context = {
        'courses': Courses.objects.filter(direction = direction)
    }
    return render(request, template_name, context)



def lesson_chat_view(request):

    template_name = "courses_templates/lesson_chat.html"

    course_pk = request.POST.get("course_pk") or request.GET.get("course_pk")

    course = Courses.objects.get(id=course_pk)

    lessons = Lessons.objects.filter(course=course_pk)

    context = {
        "lesson": lessons,
        "course": course,
    }

    if request.method == "POST":

        savol = request.POST.get("savol")

        client = genai.Client(api_key=os.getenv("API_KEY"))
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=f"""
                Sen AI Teacher san senga savollar boladi sen dars otasan lekin 
                hardoyim buni takiroroy aytishing shar 
                emas savolga qisqa javo bilan 
                darsni tushuntirishing kerak halos
                agar savol bolmasa shunchaki darsga tayyor misiz deya javob qaytar
    
                Kurs: {course.name}
    
                O'quvchining savoli:
                {savol}
                """,
            )

            context["response"] = f"AI Teacher: {response.text}"

        except errors.ClientError as e:

            if e.code == 429:
                context["response"] = "🤖 AI Teacher hozircha band. \nBirozdan keyin yana urinib ko‘ring."
            else:
                context["response"] = "❌ AI Teacher bilan bog‘lanishda xatolik yuz berdi."

        except errors.ServerError:
            context["response"] = "🤖 AI Teacher serveri hozir band. \nBirozdan keyin yana urinib ko‘ring."

    return render(request, template_name, context)


