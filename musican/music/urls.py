from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('tracks/', views.TrackListView.as_view(), name='track_list'),
    path(
        'tracks/<int:pk>/',
        views.TrackDetailView.as_view(),
        name='track_detail',
    ),
    path(
        'track/create/', views.TrackCreateView.as_view(), name='track_create'
    ),
    path(
        'track/<int:pk>/edit/',
        views.TrackUpdateView.as_view(),
        name='track_edit',
    ),
    path(
        'track/<int:pk>/delete/',
        views.TrackDeleteView.as_view(),
        name='track_delete',
    ),
    path('artists/', views.ArtistListView.as_view(), name='artist_list'),
    path(
        'artist/<int:pk>/',
        views.ArtistDetailView.as_view(),
        name='artist_detail',
    ),
    path(
        'artist/create/',
        views.ArtistCreateView.as_view(),
        name='artist_create',
    ),
    path(
        'artist/<int:pk>/edit/',
        views.ArtistUpdateView.as_view(),
        name='artist_edit',
    ),
    path(
        'artist/<int:pk>/delete/',
        views.ArtistDeleteView.as_view(),
        name='artist_delete',
    ),
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path(
        'group/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'
    ),
    path(
        'group/create/', views.GroupCreateView.as_view(), name='group_create'
    ),
    path(
        'group/<int:pk>/edit/',
        views.GroupUpdateView.as_view(),
        name='group_edit',
    ),
    path(
        'group/<int:pk>/delete/',
        views.GroupDeleteView.as_view(),
        name='group_delete',
    ),
    path(
        'album/create/', views.AlbumCreateView.as_view(), name='album_create'
    ),
    path(
        'album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'
    ),
    path(
        'album/<int:pk>/edit/',
        views.AlbumUpdateView.as_view(),
        name='album_edit',
    ),
    path(
        'album/<int:pk>/delete/',
        views.AlbumDeleteView.as_view(),
        name='album_delete',
    ),
]
