from Vehicle import Vehicle


class Bus(Vehicle):
    under_16 = 400
    above_16 = 600
    brand = 'random_bus_name'
    vehicle_num = 'random_bus_id'

    def __init__(self, no_seats):
        super().__init__(self.brand, self.vehicle_num)
        self.rate = 0
        try:
            no_seats = int(no_seats)
        except ValueError:
            print("The input was not a valid integer.")

        if int(no_seats) <= 16:
            self.rate = self.under_16
        else:
            self.rate = self.above_16

    def rental_fee_calc(self, days):
        return days * self.rate





