class Kontrol(Flights, elal_emp):
    start_time = 0
    finish_time = 0  # both for shift hours
    hash_breakType = " "  # checks whether it's break or refreshment and sets time for
    breakTime = 0
    shift_definition = " "

    def set_shift(self):
        shift_time = Kontrol.finish_time - Kontrol.start_time;
        if shift_time == 4.5:
            Kontrol.hash_breakType = "no break"
        elif shift_time <= 5:
            Kontrol.hash_breakType = "refreshment"
            Kontrol.breakTime = 0.20
        elif shift_time <= 10:
            Kontrol.hash_breakType = "45_break"
            Kontrol.breakTime = 0.45
        else:  # 10 hours shift
            Kontrol.hash_breakType = "45_20_break"
            Kontrol.breakTime = 1.05

    def set_shift_day_part(self):
        morning_shifts = ["02:00 - 06:00", "02:00 - 08:30", "02:00 - 09:30", "02:00 - 10:10", "02:00 - 11:00",
                          "03:30 - 08:30", "03:30 - 09:30", "03:30 - 10:10", "03:30 - 11:30", "03:30 - 12:40",
                          "05:00 - 11:00", "05:00 - 12.40"]
        noon_shifts = ["08:00 - 12:40", "08:00 - 14:00", "08:00 - 15:50", "11:00 - 19:00", "11:00 - 21:00",
                       "12:30 - 19:00", "12:30 - 21:00", "12:30 - 00:30", "14:00 - 19:00", "14:00 - 21:00",
                       "14:00 - 22:00", "14:00 - 23:45", "14:00 - 00:30", "14:00 - 01:30", "15:45 - 21:00",
                       "15:45 - 00:30", "15:45 - 01:30"]
        night_shifts = ["18:00 - 00:30", "18:00 - 01:30", "18:00 - 02:30", "18:00 - 04:00", "18:00 - 06:00",
                        "19:00 - 00:30", "19:00 - 01:30", "19:00 - 02:30", "19:00 - 04:00", "19:00 - 06:00",
                        "19:00 - 08:30", "21:00 - 01:30", "21:00 - 02:30", "21:00 - 04:00", "21:00 - 06:00",
                        "21:00 - 08:30", "22:30 - 06:00", "22:30 - 08:30"]

    # loop that goes through every worker and change it's shift - flights
    #  gets working staff in shift, old shift, flights and returns shift
    def change(self, elal, old_kontrol, flight):
        new_kontrol = Kontrol()
        for i in flight: # יש מערך של עובדים משובץ בטיסות, נעבור על כל מערך הטיסות במשמרת ונשנה את הזמנים שלהם


        return new_kontrol


k = Kontrol()
print(k.set_shift_day_part())

""""
 to do  - 
    function that checks shift time
    allocate time according to break type, twice in 45_20_break
    

"""
