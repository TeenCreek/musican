from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import AlbumForm, ArtistForm, GenreForm, GroupForm, TrackForm
from .models import Album, Artist, Genre, Group, Track


class ArtistListView(ListView):
    model = Artist
    template_name = 'music/artist_list.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'music/artist_detail.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = self.object.track_artist.all()
        context['groups'] = self.object.groups.all()
        return context


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:artist_list')


class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:artist_list')


class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'music/confirm_delete.html'
    success_url = reverse_lazy('music:track_list')


class TrackListView(ListView):
    model = Track
    template_name = 'music/index.html'
    context_object_name = 'tracks'


class TrackDetailView(DetailView):
    model = Track
    template_name = 'music/track_detail.html'
    context_object_name = 'track'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'music/album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = self.object.track_album.all()

        return context


class GroupListView(ListView):
    model = Group
    template_name = 'music/group_list.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GroupDetailView(DetailView):
    model = Group
    template_name = 'music/group_detail.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = self.object.artist_groups.all()
        context['tracks'] = self.object.track_group.all()
        return context


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:group_list')


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:group_list')


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'music/confirm_delete.html'
    success_url = reverse_lazy('music:group_list')


class TrackCreateView(CreateView):
    model = Track
    form_class = TrackForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:track_list')


class TrackUpdateView(UpdateView):
    model = Track
    form_class = TrackForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:track_list')


class TrackDeleteView(DeleteView):
    model = Track
    template_name = 'music/confirm_delete.html'
    success_url = reverse_lazy('music:track_list')


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:track_list')


class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:track_list')


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'music/confirm_delete.html'
    success_url = reverse_lazy('music:track_list')


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:genre_list')


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'music/form.html'
    success_url = reverse_lazy('music:genre_list')
