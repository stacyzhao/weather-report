class Forecast:
    def __init__(self, data, future=False):
        self.data = data
        if future:
            self.get_10_day_forecast()
        else:
            self.get_current_forecast()

    def get_current_forecast(self):
        observation = self.data['current_observation']
        self.temp = observation['temp_c']
        self.feelslike = observation['feelslike_c']
        self.humidity = observation['relative_humidity']

    def get_10_day_forecast(self):
        observation = self.data["forecast"]["simpleforecast"]["forecastday"]
        self.day = observation
        self.high = observation[self.day]['high']['celsius']
        self.low = observation[self.day]['low']['celsius']
        self.conditions = observation[self.day]['conditions']

    def __str__(self):
        return "Current temperature is {} C and feels like {} C  \n\
                Humidity: {}".format(self.temp, self.feelslike, self.humidity)
