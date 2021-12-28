from enum import Enum


class MobileType(Enum):
    FeaturePhone = 1
    SmartPhone = 2


class Mobile:

    def __init__(self, model, devicetype):
        self.model = model
        self.devicetype = devicetype

    def make_calls(self, number):
        print("calling.. " + number)

    def send_message(self, number, text):
        print("Sent message to " + number)
        print(text)


class Samsung(Mobile):

    def __init__(self, model, devicetype, series):
        super().__init__(model, devicetype)
        self.series = series

    def show_device_info(self):
        print("Samsung " + self.devicetype + " " + self.series + " " + self.model)

