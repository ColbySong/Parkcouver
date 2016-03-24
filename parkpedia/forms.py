from django import forms
from parkpedia.models import FavouritePark


class FavouriteParkForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':90, 'placeholder':"Enter your favourite park's name",}))

    class Meta:
        model = FavouritePark
        fields = ('name',)
