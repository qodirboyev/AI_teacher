from multiprocessing import context
from django.shortcuts import render
import os
from google import genai
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
                hardoyim buni takiroroy aytishing shart 
                emas savolga qisqa va aniq javo bilan 
                darsni tushuntirishing kerak halos 
                agar savol bolmasa shunchaki darsga tayyor misiz deya javob qaytar
    
                Kurs: {course.name}
    
                O'quvchining savoli:
                {savol}
                """,
            )

            context["response"] = response.text

        except errors.ClientError as e:

            if e.code == 429:
                context["response"] = "AI Teacherni dars limiti tugadi. \nBirozdan keyin yana urinib ko‘ring."
            else:
                context["response"] = "AI Teacher sever bilan bog‘lanishda xatolik yuz berdi.Birozdan keyin yana urinib ko‘ring."

        except errors.ServerError:
            except errors.ServerError as e:
            # 500 va 503 ni ajratib ishlov beramiz
            if "500" in str(e) or getattr(e, "code", None) == 500:
                context[
                    "response"] = "AI Teacher serverida ichki xato yuz berdi (500). \nIltimos, keyinroq yana urinib ko‘ring."
            elif "503" in str(e) or getattr(e, "code", None) == 503:
                context[
                    "response"] = "AI Teacher serverida texnik tuzatish bo‘lmoqda (503). \nBirozdan keyin yana urinib ko‘ring."
            else:
                context["response"] = "AI Teacher serverida noma’lum xato yuz berdi."

    return render(request, template_name, context)


