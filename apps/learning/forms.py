from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title', 
            'slug', 
            'description', 
            'instructor', 
            'category', 
            'status', 
            'cover_image_url'
        ]