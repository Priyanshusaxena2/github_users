import requests


def get_results_from_api(username):
    """

    :return:
    """
    API_URL = "https://api.github.com/"
    query_string = API_URL + 'users/' + username
    result = requests.get(query_string).json()
    return result