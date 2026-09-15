from django.shortcuts import render
import os

from google import genai
from google.genai import errors , Client

from courses_app.models import Courses, Lessons

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

        try:
            client = genai.Client(
                api_key=os.getenv("API_KEY")
            )

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=f"""
                Sen AI Teacher san.

                Senga savollar beriladi.
                Sen dars o'tasan.

                Savolga qisqa va aniq javob ber.
                Mavzuni tushunarli qilib tushuntir.
                Keraksiz gaplarni yozma.

                Agar savol bo'lmasa:
                "Darsga tayyormisiz?" deb javob ber.

                Kurs: {course.name}

                O'quvchining savoli:
                {savol}
                """,
            )

            context["response"] = response.text

        except errors.ClientError as e:

            if e.code == 429:
                context["response"] = (
                    "AI Teacher limiti tugadi. "
                    "Birozdan keyin yana urinib ko'ring."
                )

            else:
                context["response"] = (
                    "❌ AI Teacher server bilan bog'lanishda "
                    "xatolik yuz berdi. Birozdan keyin yana urinib ko'ring."
                )

        except errors.ServerError as e:

            if e.code == 500:
                context["response"] = (
                    "AI Teacher serverida ichki xato yuz berdi (500). "
                    "Iltimos, keyinroq yana urinib ko'ring."
                )

            elif e.code == 503:
                context["response"] = (
                    "AI Teacher serveri hozir band (503). "
                    "Birozdan keyin yana urinib ko'ring."
                )

            else:
                context["response"] = (
                    "❌ AI Teacher serverida noma'lum xato yuz berdi."
                )

    return render(request, template_name, context)