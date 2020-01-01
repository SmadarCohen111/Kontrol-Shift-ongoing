import time


class Flights:
    flight_num = 0
    flight_company = " "
    gate = " "
    dept_time = ""  # in 4 digits, colons after the first 2 digits
    boarding_time = " "  # in 4 digits, colons after the first 2 digits
    staff_size = 0

    def __init(self, flight_num, flight_company, gate, dept_time, boarding_time, staff_size):
        self.flight_num = flight_num
        self.flight_company = flight_company
        self.gate = gate
        self.dept_time = dept_time
        self.boarding_time = boarding_time
        self.staff_size = staff_size

    def __str__(self):  # printing method
        return str(self.__dict__)

    def delete_flight(self, flight):
        del flight





f1 = Flights()
f2 = Flights()
f3 = Flights()
flights_arr = ["f1", "f2", "f3"]  # creating sample DB

f1.flight_num = 1
f1.flight_company = "LY"
f1.gate = "D9"
f1.dept_time = "00:30"
f1.boarding_time = "23:35"
f1.staff_size = 8


f2.flight_num = 19
f2.flight_company = "LY"
f2.gate = "D7"
f2.dept_time = "01:00"
f2.boarding_time = "00:05"
f2.staff_size = 8


f3.flight_num = 27
f3.flight_company = "LY"
f3.gate = "D8"
f3.dept_time = "01:00"
f3.boarding_time = "00:05"
f3.staff_size = 7

print(f1)
print(f2)
print(f3)

"""
# להמשיך הדפסת אובייקטים וקישור אל מחלקת עובד
# date = datetime.datetime(2020, 5, 17)

"""
