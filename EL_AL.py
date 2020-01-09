import numpy as np


class elal_emp:
    employee_name = " "
    employee_number = 0
    skill = {"ground_attendant": False, "s_s": False, "Team_leader": False}
    seniority = 0

    def __init(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number


p1 = elal_emp()
check_arr = [["Smadar cohen", 58719, 2, True, True, False], ["Hagay tik", 28719, 3, True, True, True]]


def skills(check_arr):
    for i in range(len(check_arr)):
        for j in range(6):
          if type(check_arr[i][j]) == bool:
           a = check_arr[i][j]
           b = p1.skill.get("ground_attendant")
           #p1.skill[j-3] = check_arr[i][j]
           if a != b:
               p1.skill["ground_attendant"] = a
               print(p1.skill)


def name_employee(check_arr):
    for i in range(len(check_arr)):
       for j in range(len(check_arr)):
        if(type(check_arr[i][j]) == str):
           p1.employee_name = check_arr[i][j]
           print(p1.employee_name, " is qualified to be: ")
           skills(check_arr)

def add_emp(check_arr):
    for i in range(len(check_arr)):

"""
def print_now():
    emp5 = elal_emp()
    for x,y in emp5.skill.items():
        print(x, y)
    z = emp5.skill.get("s_s")
    print(z)
"""

#print_now()
p2 = elal_emp()
name_employee(check_arr)