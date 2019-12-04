from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)

from .utils import get_movies, get_planets


# Create your views here.

class PlanetView(GenericAPIView):
    """
    View to list planets from SWAPI.
    """
    def get(self, request):
        """
        Return list of planets.
        :param request:
        :return:
        """
        page = request.query_params.get('page')
        search = request.query_params.get('search')

        result = get_planets(page, search)

        return Response(result, status=HTTP_200_OK)


class MovieView(GenericAPIView):
    """
    View to list movies from SWAPI.
    """
    def get(self, request):
        """
        Return list of movies.
        :param request:
        :return:
        """
        page = request.query_params.get('page')
        search = request.query_params.get('search')

        result = get_movies(page, search)

        return Response(result, status=HTTP_200_OK)
