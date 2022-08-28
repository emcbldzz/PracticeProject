# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Car import Car
from Bus import Bus


def get_sum_rent(days):
    pass
    rental_fee = 0
    vehicle_type = input('Do you want to rent Car or Bus\n')
    if vehicle_type == 'Car':
        car_type = input('Choose car type from car_2x, car_3x and car_5x, the have daily rate of 300, 350 and 500 respectively\n')
        car1 = Car(car_type)
        msg = f" For renting {car_type} for {days} days. It would be ${car1.rental_fee_calc(days)}."
        print(msg)
    elif vehicle_type == 'Bus':
        bus_seats = input('How many seats the bus need. Under 16 it would be $400. Above 16 seats costs $600\n')
        bus1 = Bus(bus_seats)
        msg = f" For renting {bus_seats} for {days} days. It would be ${bus1.rental_fee_calc(days)}."
        print(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    days = int(input('How many days to rent?\n'))
    get_sum_rent(days)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
