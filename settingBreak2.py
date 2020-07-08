from ShiftWorker import T1
from ShiftWorker import team_leader_result
from ShiftWorker import attendants


class SettingBreak2:
    id: str = ""
    start_break_time: float = 0
    end_break_time: float = 0
    work_times: list = []
    break_time: float = 0

    def __init__(self, id: str, start_break_time: str, end_break_time: str, work_times: list, break_time: int):
        self.id = id
        self.start_break_time = self.convert_str_time_to_float_time(start_break_time)
        self.end_break_time = self.convert_str_time_to_float_time(end_break_time)
        self.break_time = break_time/60
        self.work_times = []
        for i, work_time in enumerate(work_times):
            if i % 2 == 0:
                self.work_times.append({})
                self.work_times[int(i/2)]["start"] = self.convert_str_time_to_float_time(work_times[i])
            else:
                self.work_times[int(i/2)]["end"] = self.convert_str_time_to_float_time(work_times[i])

    @staticmethod
    def convert_str_time_to_float_time(str_time: str):
        hour_str = str_time.split(":")[0]
        minutes_str = str_time.split(":")[1]
        time_float = float(hour_str) + float(minutes_str)/60
        #print(time_float)
        return time_float

    def is_break_time_possible(self):
        possible_break_times = self.convert_work_times_to_break_times(self.start_break_time, self.end_break_time, self.work_times)
        for possible_break_time in possible_break_times:
            if self.check_if_possible(possible_break_time, self.break_time):
                return possible_break_time["start"]
        return None

    @staticmethod
    def check_if_possible(possible_break_time: dict, break_time: float):
        return possible_break_time["start"] + break_time <= possible_break_time["end"]

    @staticmethod
    def convert_work_times_to_break_times(start_break_time: float, end_break_time: float, work_times: list):
        break_times = [{}]
        break_times[0]["start"] = start_break_time
        #print(work_times)

        for i, work_time in enumerate(work_times):
            #print(work_time)
            if len(work_times[i]) != 0:
                break_times[i]["end"] = work_times[i]["start"]
                break_times.append({})
                break_times[i+1]["start"] = work_times[i]["end"]
            else:
                break
        break_times[len(break_times) - 1]["end"] = end_break_time
        #print(break_times)
        return break_times


class SettingBreak:
    hash_breakType = " "  # checks whether it's break or refreshment and sets time for
    employee_and_his_break = {}
    breakTime = 0
    set_flight_tl = []

    def set_none_shift(self):
        for j in range(self.emp.tl):
            for i in range(6):
                name = self.emp.skill["tl"][j][0]
                aval = self.emp.skill["tl"][j][1]
                if self.f[i].get_tl() == "" and aval == True:
                    self.f[i].set_tl(name)
                    self.emp.skill["tl"][j][1] = False
                    self.emp.skill["ga"][j][1] = False
                    break

    def create_shift_tl(self, work: list):
        j = 0
        for i in work:
            if j == 0:
                self.set_break(j, work=work)
                j += 1
            else:
                self.set_break(j, work=work)
                j += 1
        return self.employee_and_his_break

    def create_shift_attendants(self, work1: list):
        j = 0
        for i in work1:
            if j == 0:
                self.set_break(j, work=work1)
                j += 1
            else:
                self.set_break(j, work=work1)
                j += 1
        return self.employee_and_his_break

    def set_break(self, index, work: list):
        if work[index][4] == "19:00" and work[index][3] == "12:30" or work[index][4] == "19:00" and work[index][
            3] == "11:00" or work[index][4] == "21:00" and work[index][3] == "14:00" or work[index][4] == "01:30" and \
                work[index][3] == "18:00" or work[index][4] == "01:30" and work[index][3] == "19:00":
            SettingBreak.hash_breakType = "45_break"
            SettingBreak.breakTime = 0.45
            self.employee_and_his_break.setdefault(work[index][2], SettingBreak.breakTime)
            return self.employee_and_his_break
        elif work[index][4] == "01:30" and work[index][3] == "21:00":
            SettingBreak.hash_breakType = "no break"
            print(work[index][0], work[index][1], "have no break")
        #      elif shift_time <= 5:
        #         SettingBreak.hash_breakType = "refreshment"
        #        SettingBreak.breakTime = 0.20
        else:  # 10 hours shift
            SettingBreak.hash_breakType = "45_20_break"
            SettingBreak.breakTime = 1.05
            print(work[index][0], work[index][1], " have 1:05 min break")


ss = SettingBreak()
ss.employee_and_his_break = ss.create_shift_tl(team_leader_result)
#print(ss.employee_and_his_break)
team_flights = list(T1.team_flights.team_members.values())
#print("this is the teams flights: ", team_flights)
try_some = ss.employee_and_his_break.keys()
#print("this is the break: ", try_some)
iter_on_teams = 0
iter_on_employee = 0
iter_on_teams_keys = "0"
employees_shift = [{}]
j = 0


def check_if_employee_exist(teams_work_on, team_key, emp_num):
    if len(teams_work_on) != 0:
        one_employee = teams_work_on.pop()
    while len(teams_work_on)+1 != 0:
        if one_employee[2] == emp_num:
            return one_employee
            break
        elif one_employee[2] != emp_num and len(teams_work_on) != 0:
            one_employee = teams_work_on.pop()
        else:
            employee_number = list(try_some).pop()
            teams_work_on = team_flights.pop(iter_on_teams)
            #print(employee_number)
            check_if_employee_exist(teams_work_on=teams_work_on, team_key=team_key, emp_num=employee_number)
    return None


def where_to_insert_the_break(work_times, break_time_total: dict):
    counter = 0
    work_times_include_break_time = {}
    for i,work_time in enumerate(work_times):
        if counter == 0:
            if work_times[i]["start"] < break_time_total["start_break"]:
                continue
            else:
                work_times_include_break_time = break_time_total
                break
    j = 1
    for j,work_time in enumerate(work_times):
        work_times_include_break_time.__setitem__(j, work_time)
    return work_times_include_break_time


#print("this is the flights: ", T1.team_flights.flights)
#print("this is the team members: ", T1.team_flights.team_members)

for i in try_some:
    iter_on_flights = 0
    one_team = team_flights.pop(0)
    iter_on_employee = 0
    one_emp = list(one_team).pop(iter_on_employee)
    if one_emp[2] == i:
        flight_works_on = T1.team_flights.flights.pop(iter_on_teams_keys)
        temp = int(iter_on_teams_keys)
        temp += 1
        iter_on_teams_keys = str(temp)
        start_end_work_time = []
        while len(flight_works_on) > iter_on_flights:
            start_end_work_time.append(flight_works_on[iter_on_flights][2])
            start_end_work_time.append(flight_works_on[iter_on_flights][1])
            iter_on_flights += 1
        value_for_break = ss.employee_and_his_break.get(i)

        ss2 = SettingBreak2(id=i, start_break_time=one_emp[3], end_break_time=one_emp[4], work_times=start_end_work_time, break_time=value_for_break)

        start_break_time = (ss2.is_break_time_possible())
        #print(start_break_time)
        end_break_time = start_break_time+value_for_break
        break_time_total = {}
        break_time_total.setdefault("start_break", start_break_time)
        break_time_total.__setitem__("end_break", end_break_time)
        #print(break_time_total)
        work_times_include_break_time = where_to_insert_the_break(work_times=ss2.work_times, break_time_total=break_time_total)

        employees_shift[j].__setitem__(i, work_times_include_break_time)
        j += 1
        #print(employees_shift)
        #employee_shift.append(work_times_include_break_time)
        employees_shift.append({})
        #print(employee_shift)
        #print("this is the work times: ", ss2.work_times)
        #print(end_break_time)
        #print(True, "this is the value: ", one_emp)

    else:
        one_emp = check_if_employee_exist(teams_work_on=one_team, team_key=iter_on_teams_keys,  emp_num=i)
        flight_works_on = T1.team_flights.flights.pop(iter_on_teams_keys)
        temp = int(iter_on_teams_keys)
        temp += 1
        iter_on_teams_keys = str(temp)
        start_end_work_time = []
        while len(flight_works_on) > iter_on_flights:
            start_end_work_time.append(flight_works_on[iter_on_flights][2])
            start_end_work_time.append(flight_works_on[iter_on_flights][1])
            iter_on_flights += 1
        value_for_break = ss.employee_and_his_break.get(i)
        ss2 = SettingBreak2(id=i, start_break_time=one_emp[3], end_break_time=one_emp[4], work_times=start_end_work_time, break_time=value_for_break)
        start_break_time = (ss2.is_break_time_possible())
        #print(start_break_time)
        end_break_time = start_break_time + value_for_break
        #print(end_break_time)
        break_time_total ={}
        break_time_total.setdefault("start_break", start_break_time)
        break_time_total.__setitem__("end_break", end_break_time)
        #print(break_time_total)
        work_times_include_break_time = where_to_insert_the_break(work_times=ss2.work_times, break_time_total=break_time_total)
        #employee_id = one_emp[2]
        employees_shift[j].__setitem__(i, work_times_include_break_time)
        j+=1
        #employee_shift.append(work_times_include_break_time)
        employees_shift.append({})
        #print(employees_shift)
        #print("this is the work times: ", ss2.work_times)
        #insert_break_time_into_work_time()
        #print(True, "this is the value: ", one_emp)

#ss2 = SettingBreak2(id="57519", start_break_time="11:45", end_break_time="18:50", work_times=["12:00", "13:30", "15:15", "17:30"], break_time=105)
#print(ss2.is_break_time_possible())
