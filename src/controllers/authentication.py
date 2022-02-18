import requests


def login(username, password, login_url, test_url):
    """Function to handle user authentication

    Parameters:
        username (str):The username used to log in.
        password (str):The password used to log in.
        login_url (string):The url used to log in the given username and password.
        test_url (string):Used to get a response and see if the user is authenticated or not.
    Returns:
        True (bool):User is authenticated.
        False (bool):User is not authenticated(due to wrong username or password).
    """

    # create the session with the login_url
    client = requests.session()
    client.get(login_url)

    # retrieve the csrf token from session cookies
    csrftoken = client.cookies['csrftoken']

    login_data = {'username': username, 'password': password, 'csrfmiddlewaretoken': csrftoken}

    # login in the login_url with the given login_data
    client.post(login_url, data=login_data)
    # gets the response to check if the user is authenticated or not
    login_response = client.get(test_url)

    # http responses
    if login_response.status_code == 403:
        return None
    if login_response.status_code == 200:
        return client
