from datetime import datetime, timedelta


class Car:
    def __init__(self, car_type):
        self.car_type = car_type

class Reservation:
    def __init__(self, car_type, start_date, end_date):
        self.car_type = car_type
        self.start_date = start_date
        self.end_date = end_date

class CarInventory:
    def __init__(self):
        self.inventory = {
            "sedan": [],
            "SUV": [],
            "van": []
        }
        self.reserved_cars = {
            "sedan": [],
            "SUV": [],
            "van": []
        }

    def add_car(self, car_type):
        self.inventory[car_type].append(Car(car_type))

    def is_available(self, car_type, start_date, days):
        end_date = start_date + timedelta(days=days)
        reserved_count = sum(
            not (end_date <= reservation.start_date or start_date >= reservation.end_date)
            for reservation in self.reserved_cars[car_type]
        )
        return len(self.inventory[car_type]) > reserved_count

    def reserve_car(self, car_type, start_date, days):
        if self.is_available(car_type, start_date, days):
            end_date = start_date + timedelta(days=days)
            self.reserved_cars[car_type].append(Reservation(car_type, start_date, end_date))
            return True
        return False

class CarRentalSystem:
    def __init__(self):
        self.inventory = CarInventory()

    def add_car_to_inventory(self, car_type, quantity):
        for _ in range(quantity):
            self.inventory.add_car(car_type)

    def make_reservation(self, car_type, start_date, days):
        return self.inventory.reserve_car(car_type, start_date, days)

if __name__ == "__main__":
    crs = CarRentalSystem()
    crs.add_car_to_inventory("sedan", 2)
    crs.add_car_to_inventory("SUV", 1)
    crs.add_car_to_inventory("van", 1)

    start_date = datetime.now()
    reserved = crs.make_reservation("sedan", start_date, 2)
    print("Have you been able to book a sedan:", reserved)