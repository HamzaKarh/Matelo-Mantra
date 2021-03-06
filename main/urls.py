from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .posts import urls as posts
from .picture_albums import urls as pAlbums
from .music_albums import urls as mAlbums
from .descriptions import urls as descriptions
#from .views import PostView, CreatePostView
from .posts import urls

urlpatterns = [

    path("", views.landing, name="landing"),
    path("home/", views.home, name="Home"),
    path("post/", include(posts)),
    path("travels/", include(pAlbums)),
    path("music/", include(mAlbums)),
    path("descriptions/", include(descriptions))

]