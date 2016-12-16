from django.forms import ModelForm

from stud.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student