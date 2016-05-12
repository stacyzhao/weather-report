class Alert:
    def __init__(self, data):
        self.status = data['alerts']
        # self.hurricane = hurricane

    def check_alert_status(self):
        print(self.status)
        if len(self.status) != 0:
            for x in range(len(self.status)):
                print(self.status[x]['description'])

    def __str__(self):
        return self.status
