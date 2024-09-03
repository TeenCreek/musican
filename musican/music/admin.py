from django.contrib import admin

from .models import Album, Artist, Genre, Group, Track

EMPTY_VALUE = '-ПУСТО-'


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'birth_day', 'get_group_artists')
    search_fields = ('name',)
    list_filter = ('name', 'country')
    empty_value_display = EMPTY_VALUE


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'date_foundation')
    search_fields = ('name',)
    list_filter = ('name', 'country', 'date_foundation')
    empty_value_display = EMPTY_VALUE


@admin.register(Album)
class AlbumRegister(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_year', 'label')
    search_fields = ('name',)
    list_filter = ('name', 'release_year')
    empty_value_display = EMPTY_VALUE


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'duration',
        'album',
        'artist',
        'group',
        'genre',
    )
    search_fields = ('name', 'artist', 'genre')
    list_filter = ('album', 'artist', 'group', 'genre')
    empty_value_display = EMPTY_VALUE


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
