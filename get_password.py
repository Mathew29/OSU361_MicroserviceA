import requests
from typing import Optional


def get_password(uppercase: bool, lowercase: bool, special: bool, numbers: bool, length: Optional[int] = None):
    """
    Password generator that requests a random password from a open source API.
    API: https://api.genratr.com
    Returns:
        __str__: "password"
    """

    url = 'https://api.genratr.com/'

    params = {}

    if length is not None:
        params['length'] = length
    if uppercase:
        params["uppercase"] = "uppercase"
    if lowercase:
        params["lowercase"] = "lowercase"
    if special:
        params["special"] = "special"
    if numbers:
        params["numbers"] = "numbers"
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            password = response.json()
            return password['password']

    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
    except ValueError as err:
        print(f"Error JSON response: {err}")


if __name__ == "__main__":
    get_password(True, True, False, True, 19)
