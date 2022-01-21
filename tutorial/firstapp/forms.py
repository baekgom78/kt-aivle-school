from .models import Curriculum
from django import forms

class CurriculumForm(forms.ModelForm):
    class Meta:

        model = Curriculum

        fields = ['name']  
    
        labels = {  # fields에 명시된 속성만 사용
            'name': '과목'
        }
