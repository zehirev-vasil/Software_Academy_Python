from enum import Enum


class BatteryType(Enum):
    Li_Ion = "Li-Ion"
    NiMH = "NiMH"
    NiCd = "NiCd"


class MobilePhone:
    nokiaN95 = ('Nokia N95', 'NOKIA', 100, 'Vasil', {"model": "BN-LA2021", "idle_time": 10, "hours_talk": 5},
                {'size': "6", 'color': 'green'})

    def __init__(self, model=None, manufacturer=None, price=None, owner=None, battery=None, battery_type=None,
                 screen=None):
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.owner = owner
        self.battery = battery
        self.screen = screen
        self.battery_type = battery_type

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Price: {self.price}")
        print(f"Owner: {self.owner}")
        print(f"Battery: {self.battery}")
        print(f"Screen: {self.screen}")

    @staticmethod
    def display_nokiaN95_info():
        print(MobilePhone.nokiaN95)

    def __str__(self):
        return (f"Model: {self.model}, Manufacturer: {self.manufacturer}, Price: {self.price}, "
                f"Owner: {self.owner}, Battery: {self.battery}, Battery Type: {self.battery_type}, Screen: {self.screen}")

    def add_call(self, date, time, duration):
        call_archive = Call(date=date, time=time, duration=duration)
        Call._call_history.append(call_archive)

    def delete_call(self, call):
        Call._call_history.remove(call)

    def sum_duration(self, price_per_minute):
        sum = 0
        for call in Call._call_history:
            sum += call.duration
        return sum / 60 * price_per_minute

    def view_history(self):
        for call in Call._call_history:
            print(call)


class TestMobilePhone:
    _mobile_phones = []

    @staticmethod
    def create_mobile_phones():
        phonebattery = {"model": "BN-LA2021", "idle_time": 10, "hours_talk": 5}
        screen = {'size': "6", 'color': 'green'}

        TestMobilePhone._mobile_phones.append(
            MobilePhone("iPhone 14", "Apple", 2000, "Gorge", phonebattery, BatteryType.Li_Ion, screen))
        # TestMobilePhone._mobile_phones.append(
        #     MobilePhone('Nokia N200', 'NOKIA', 100, 'Mitko', {"model": "BN-LA2023", "idle_time": 10, "hours_talk": 20},
        #                 {'size': "6", 'color': 'green'}))

    @staticmethod
    def run_test():
        TestMobilePhone.create_mobile_phones()

        # Assert that mobile phones were created
        assert len(TestMobilePhone._mobile_phones) == 1, "Expected 2 mobile phones"

        for phone in TestMobilePhone._mobile_phones:
            print(phone)


class Call:
    date = None
    time = None
    duration = None

    _call_history = []

    def __init__(self, date, time, duration):
        self.date = date
        self.time = time
        self.duration = duration

    @property
    def call_history(self):
        return self._call_history

    def add_call(self, call):
        self._call_history.append(call)

    def __str__(self):
        return f"Call(date={self.date}, time={self.time}, duration={self.duration})"



new_phone = MobilePhone("iPhone 14", "Apple", 2000, "Gorge", {"model": "BN-LA2021", "idle_time": 10, "hours_talk": 5})
print(new_phone)

new_phone.add_call("12.12.2020", "12:12", 12)
new_phone.add_call("13.12.2020", "12:12", 20)
new_phone.add_call("14.12.2020", "12:12", 30)

new_phone.view_history()