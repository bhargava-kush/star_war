import requests


def get_planets(page=1, search=None):
    """
    list of planets from swapi
    :param page:
    :param search:
    :return:
    """
    params = {
        'page': page,
        'search': search
    }
    response = requests.get(f"https://swapi.co/api/planets/", params=params)
    return response.json()


def get_movies(page=1, search=None):
    """
    list of movies from swapi
    :param page:
    :param search:
    :return:
    """
    params = {
        'page': page,
        'search': search
    }
    response = requests.get(f"https://swapi.co/api/films/", params=params)
    return response.json()
