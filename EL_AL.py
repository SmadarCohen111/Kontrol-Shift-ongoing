
class elal_emp:
    employee_name = " "
    employee_number = 0
    skill = {"ground_attendant": False, "s_s": False, "Team_leader": False}
    seniority = 0

    def __init(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number


p1 = elal_emp()
p3 = elal_emp()
#pointer = 0
check_arr = [["Smadar Cohen", 58719, 2, True, True, False], ["Hagay Tik", 28719, 3, True, True, True] , ["Osher Avraham", 59314, 1, True, False, False], ["Luba Epshtein", 59315, 4, True, False, True],
             ["Adi Biton", 59317, 3, True, True, True], ["Amichai Friedman", 29136, 2.5, True, True, True], ["Amit Senouf", 29315, 4, True, True, False], ["Anna Kulik", 29317, 1, True, True, False],
             ["Anna Zicherman", 38193, 4, True, False, False], ["Ayala Josef", 37195, 3, True, True, False], ["Bar Tangi", 37197, 1.5, True, False, False],["Bar Hanash", 43195, 3.5, True, True, False],
             ["Chemdat Ofir Lipscker", 43193, 1, True, True, True], ["Chen Vashadi", 45193, 2, True, False, True], ["Einat Skornik", 65237, 3, True, False, False],["Eshchar Ben-Haiem", 67193, 2.5 , True, False, False],
             ["Eylon Segal", 65233, 2, True, True, True], ["Gal Ben-nun", 57133, 2, True, True, False],["Gal Ben Yishay", 57135, 2, True, True, True]]

"""
def emp_number(check_arr):
    for i in range(len(check_arr)):
        for j in range(6):
            if type(check_arr[i][j]) == int and str(check_arr[i][j]).__len__() > 2:
                if p1.employee_number == 0:
                  p1.employee_number =  check_arr[i][j]
                  print(p1.employee_number)
                  break
                elif p3.employee_number == 0 and p1.employee_number == 0:
                  p3.employee_number = check_arr[i][j]
                  print(p3.employee_number)
                elif p1.employee_number != 0:
                    break
"""


def get_value(skill):
    return list(p1.skill.values())

def get_key(skill):
    return list(p1.skill.keys())

def skills(check_arr, counter):
    for i in range(len(check_arr)):
        if i > counter:
            counter += 1
            name_employee(check_arr, counter)
        for j in range(3,6):
          if type(check_arr[counter][j]) == bool:
           organ = check_arr[counter][j]
           value = get_value(p1.skill)
           if organ != value.pop(j-3):
               key = get_key(p1.skill)
               for i in range(1):
                p1.skill[key.pop(j-3)] = organ
        if i == counter:
         print(p1.skill)


def name_employee(check_arr, counter):
     for i in range(len(check_arr)):
        print("counter: ", counter, "length of arr: ", len(check_arr))
        if type(check_arr[counter][i]) == str:
          if i+1 != len(check_arr):
           p1.employee_name = check_arr[counter][i]
           print(p1.employee_name, " is qualified to be: ")
           skills(check_arr, counter)
          elif i+1 == len(check_arr):
            break
     return None



p2 = elal_emp()
name_employee(check_arr, 0)