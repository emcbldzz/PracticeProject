from Vehicle import Vehicle


class Car(Vehicle):
    car_2x = 300
    car_3x = 350
    car_5x = 500
    brand = 'random_car_brand'
    vehicle_num = 'random_car_id'

    def __init__(self, car_type):
        super().__init__(self.brand, self.vehicle_num)
        self.rate = 0
        if car_type == 'car_2x':
            self.rate = self.car_2x
        elif car_type == 'car_3x':
            self.rate = self.car_3x
        elif car_type == 'car_5x':
            self.rate = self.car_5x
        else:
            raise ValueError("The Car Type is incorrect")

    def rental_fee_calc(self, days):
        return days * self.rate

