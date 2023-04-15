import requests


def get_status(ip):
    response = requests.api.get(f"https://api.mcsrvstat.us/2/{ip}").json()
    return response


