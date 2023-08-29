from django.contrib import admin
from .models import Artist, Album, Song

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'release_year')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album_number')
