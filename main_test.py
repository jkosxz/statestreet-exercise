import unittest
from datetime import datetime, timedelta
from main import CarRentalSystem

class TestCarRentalSystem(unittest.TestCase):
    def test_car_rental_system(self):
        crs = CarRentalSystem()
        crs.add_car_to_inventory("sedan", 2)
        crs.add_car_to_inventory("SUV", 1)
        crs.add_car_to_inventory("van", 1)

        start_date = datetime.now()

        self.assertTrue(crs.make_reservation("sedan", start_date, 2), "Sedan reservation failed")

        self.assertTrue(crs.make_reservation("SUV", start_date, 3), "SUV reservation failed")

        crs.make_reservation("sedan", start_date, 2)
        self.assertFalse(crs.make_reservation("sedan", start_date, 2), "It should not be possible to book an additional sedan")

        crs.make_reservation("SUV", start_date, 2)
        overlapping_start = start_date + timedelta(days=1)
        self.assertFalse(crs.make_reservation("SUV", overlapping_start, 2), "Reservations with overlapping dates should be rejected")

        crs.make_reservation("van", start_date, 2)
        non_overlapping_start = start_date + timedelta(days=3)
        self.assertTrue(crs.make_reservation("van", non_overlapping_start, 2), "Booking with non-overlapping dates should be possible")

if __name__ == "__main__":
    unittest.main()