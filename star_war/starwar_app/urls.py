from django.urls import include, path
from .views import PlanetView, MovieView

app_name = "starwar_app"

urlpatterns = [
    path('planets', PlanetView.as_view(), name='list-planets'),
    path('movies', MovieView.as_view(), name='list-movies')
    ]
