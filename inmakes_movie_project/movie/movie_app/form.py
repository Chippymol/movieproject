from django import forms
from .models import movie_details


class FormMovies(forms.ModelForm):
    class Meta:
        model = movie_details
        fields = ['movie_name', 'movie_desc', 'year', 'Ticket_price', 'img']
