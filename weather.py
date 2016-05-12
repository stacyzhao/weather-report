import requests
from urllib.parse import urljoin
from astronomy import Astronomy
from forecast import Forecast
from alert import Alert


def get_data(zip_code):
    key = "ed67bdaaf4fec173"
    zipcode = zip_code + ".json"
    features = '/conditions/forecast10day/astronomy/alerts/currenthurricane/q/'
    url = urljoin('http://api.wunderground.com/api/', key + features + zipcode)

    response = requests.get(url)
    return response.json()


def get_zip_code():
    user_zip = str(input("What's Your Zipcode? \n"))
    return user_zip


def main():
    data = get_data(get_zip_code())

    print(Forecast(data))
    # print(Forecast(data, True))
    print(Astronomy(data))
    Alert(data)

if __name__ == '__main__':
    main()
