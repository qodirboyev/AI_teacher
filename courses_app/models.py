from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    lessons = models.IntegerField()
    DIRECTIONS = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("cyber", "Cyber Security"),
        ("robot", "Robotatexnika"),
        ("os", "OS"),
        ("ai", "AI"),
        ("mobile", "Mobil dasturlash"),
    ]
    direction = models.CharField(
        max_length=20,
        choices=DIRECTIONS
    )
    image = models.ImageField(upload_to="courses_image/")

    def __str__(self):
        return self.name





class Lessons(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course_lessons")
    lesson_number = models.IntegerField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.course} {self.lesson_number}-dars: {self.subject}"

    class Meta:
        ordering = ['lesson_number']