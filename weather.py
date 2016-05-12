import requests
from urllib.parse import urljoin
from astronomy import Astronomy
from forecast import Forecast
from alert import Alert


def get_data():
    key = "ed67bdaaf4fec173"
    zipcode = str(40342) + ".json"
    features = '/conditions/forecast10day/astronomy/alerts/currenthurricane/q/'
    url = urljoin('http://api.wunderground.com/api/', key + features + zipcode)

    response = requests.get(url)
    return response.json()


def main():
    data = get_data()
    print(Forecast(data))
    # print(Forecast(data, True))
    print(Astronomy(data))
    Alert(data)

if __name__ == '__main__':
    main()
