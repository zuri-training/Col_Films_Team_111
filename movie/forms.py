from django import forms

from .models import Movie
class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'category',
            'movie',
            'thumbnail',
            'length',
        )
        # widgets = {
        #     'thumbnail': forms.FileInput(attrs={'class': 'form_control'}),
        # }