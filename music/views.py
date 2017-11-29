
from .models import Album,Song
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.

class IndexView(generic.ListView):
    template_name ='music/index.html'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = "music/details.html"

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist_name','album_name','album_icon']

class SongCreate(CreateView):
    model = Song
    fields = ['album_name','file_name','song_choose']
