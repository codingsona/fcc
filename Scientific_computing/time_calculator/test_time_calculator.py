import unittest
from time_calculator import time_calculator

class UnitTests(unittest.TestCase):

    def test_same_period(self):
        actual = time_calculator("3:30 PM", "2:12").add_time()
        expected = "5:42 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')

    def test_different_period(self):
        actual = time_calculator("11:55 AM", "3:12").add_time()
        expected = "3:07 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')

    def test_next_day(self):
        actual = time_calculator("9:15 PM", "5:30").add_time()
        expected = "2:45 AM (next day)"
        self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')

    def test_period_change_at_twelve(self):
        actual = time_calculator("11:40 AM", "0:25").add_time()
        expected = "12:05 PM"
        self.assertEqual(actual, expected, 'Expected period to change from AM to PM at 12:00')

    def test_twenty_four(self):
        actual = time_calculator("2:59 AM", "24:00").add_time()
        expected = "2:59 AM (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"')

    def test_two_days_later(self):
        actual = time_calculator("11:59 PM", "24:05").add_time()
        expected = "12:04 AM (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')

    def test_high_duration(self):
        actual = time_calculator("8:16 PM", "466:02").add_time()
        expected = "6:18 AM (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')

    def test_no_change(self):
        actual = time_calculator("5:01 AM", "0:00").add_time()
        expected = "5:01 AM"
        self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')

    def test_same_period_with_day(self):
        actual = time_calculator("3:30 PM", "2:12", "Monday").add_time()
        expected = "5:42 PM, Monday"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')

    def test_twenty_four_with_day(self):
        actual = time_calculator("2:59 AM", "24:00", "saturDay").add_time()
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

    def test_two_days_later_with_day(self):
        actual = time_calculator("11:59 PM", "24:05", "Wednesday").add_time()
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "Friday" to return "12:04 AM, Friday (2 days later)"')

    def test_high_duration_with_day(self):
        actual = time_calculator("8:16 PM", "466:02", "tuesday").add_time()
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')

if __name__ == "__main__":
    unittest.main()