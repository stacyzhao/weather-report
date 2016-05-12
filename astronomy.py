class Astronomy:
    def __init__(self, data):
        self.data = data
        self.sunrise = self.get_astro_time('sunrise')
        self.sunset = self.get_astro_time('sunset')

    def get_astro_time(self, phase):
        phase_data = self.data['sun_phase']
        return phase_data[phase]['hour'] + ":" + phase_data[phase]['minute']

    def __str__(self):
            return "Sunrise: {} Sunset: {}".format(self.sunrise, self.sunset)
