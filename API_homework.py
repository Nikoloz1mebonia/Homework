import requests


def get_data(url):
    try:
        response = requests.get(url)
        print(response.text)

    except:
        print("Invalid URL or some error occured while making the GET request to the specified URL")


get_data("https://api.github.com/")
get_data("https//nothing")
