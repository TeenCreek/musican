from django import forms

from .models import Album, Artist, Genre, Group, Track


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = (
            'name',
            'country',
            'birth_day',
            'groups',
            'tracks',
            'info',
        )
        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date'}),
            'info': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'country', 'date_foundation', 'members', 'tracks')
        widgets = {
            'date_foundation': forms.DateInput(attrs={'type': 'date'}),
        }


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = (
            'name',
            'duration',
            'album',
            'artist',
            'group',
            'genre',
            'text',
        )
        widgets = {
            'duration': forms.NumberInput(attrs={'step': 'any'}),
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'release_year', 'label')
        widgets = {
            'release_year': forms.DateInput(attrs={'type': 'date'}),
            'label': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)
