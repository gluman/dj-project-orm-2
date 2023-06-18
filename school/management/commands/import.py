from django.core.management.base import BaseCommand
import json
from school.models import Teacher, Student, Releations


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('school.json', 'rb') as f:
            data = json.load(f)
            for record in data:
                if record['model'] == 'school.teacher':
                    teacher = Teacher(id=record['pk'], name=record['fields']['name'], subject=record['fields']['subject'])
                    teacher.save()
                if record['model'] == 'school.student':
                    student = Student(id=record['pk'], name=record['fields']['name'], group=record['fields']['group'])
                    student.save()
                    current_teachers = Teacher.objects.get(id=record['fields']['teacher'])
                    student_teachers = Releations(students=student, teachers=current_teachers)
                    student_teachers.save()
            return print('done')

