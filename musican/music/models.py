from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class CommonInfo(models.Model):
    """Абстрактная базовая модель для общих полей."""

    name = models.CharField('Имя', max_length=100)
    country = models.CharField('Страна', max_length=100)

    class Meta:
        abstract = True


class Artist(CommonInfo):
    """Модель для артиста."""

    birth_day = models.DateField('Дата рождения')
    groups = models.ManyToManyField(
        'Group',
        related_name='artist_groups',
        verbose_name='Группа',
        blank=True,
    )
    tracks = models.ManyToManyField(
        'Track', related_name='artist_tracks', verbose_name='Треки', blank=True
    )
    info = models.TextField('Об исполнителе', null=True, blank=True)

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.birth_day > timezone.now().date():
            raise ValidationError('Дата рождения не может быть в будущем.')

    def get_group_artists(self):
        return ', '.join([group.name for group in self.groups.all()])

    get_group_artists.short_description = 'Группы'


class Group(CommonInfo):
    """Модель для группы."""

    date_foundation = models.DateField('Дата основания')
    members = models.ManyToManyField(
        Artist,
        related_name='group_members',
        verbose_name='Артисты',
        blank=True,
    )
    tracks = models.ManyToManyField(
        'Track', related_name='group_tracks', verbose_name='Треки', blank=True
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.date_foundation > timezone.now().date():
            raise ValidationError('Дата основания не может быть в будущем.')


class Album(models.Model):
    """Модель для альбома."""

    name = models.CharField('Название альбома', max_length=100)
    release_year = models.DateField('Дата выхода')
    label = models.TextField('Описание')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ('release_year', 'name')

    def __str__(self):
        return self.name


class Track(models.Model):
    """Модель для трека."""

    name = models.CharField('Название трека', max_length=100)
    duration = models.FloatField(
        'Длительность', validators=[MinValueValidator(0.0)]
    )
    album = models.ForeignKey(
        Album,
        verbose_name='Альбом',
        related_name='track_album',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    artist = models.ForeignKey(
        Artist,
        verbose_name='Исполнитель',
        related_name='track_artist',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        related_name='track_group',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    genre = models.ForeignKey(
        'Genre',
        verbose_name='Жанр',
        on_delete=models.CASCADE,
    )
    text = models.TextField('Текст песни', blank=True, null=True)

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'
        ordering = ('name',)
        constraints = (
            models.UniqueConstraint(
                fields=('group', 'name'), name='unique_group_name'
            ),
        )

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.duration <= 0:
            raise ValidationError(
                'Длительность трека должна быть положительной  или больше нуля.'
            )


class Genre(models.Model):
    """Модель для жанров."""

    name = models.CharField('Жанр', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name
