import mysql.connector
import numpy as np



# we need to change the hours
# check whether the time differences allow us to set father & child, static function
def check_time_differences(first_hour, second_hour):
    arr_of_fh = first_hour.split(":")
    arr_of_sh = second_hour.split(":")
    str_of_fh = arr_of_fh[0]
    str_of_sh = arr_of_sh[0]
    str_of_fm = arr_of_fh[1]
    str_of_sm = arr_of_sh[1]
    first_cast_hour = int(str_of_fh)
    second_cast_hour = int(str_of_sh)
    first_cast_minute = int(str_of_fm)
    second_cast_minute = int(str_of_sm)
    decrease_hours = second_cast_hour - first_cast_hour
    dup_hour = decrease_hours * 60
    decrease_minutes = second_cast_minute - first_cast_minute
    if dup_hour != 0:
       if dup_hour + decrease_minutes > 20 or dup_hour + decrease_minutes == 20:
         #if dup_hour + decrease_minutes < 35 or dup_hour + decrease_minutes == 35:
             return True
       else:
            return False
    else:
        if decrease_minutes > 20 or decrease_minutes == 20:
            #if decrease_minutes < 35 or decrease_minutes == 35:
            return True
        else:
            return False


class Tree(object):
    queue_flights = []
    queue_tree = []
    num_of_teams = 0
    team_flights = None
    flight_mat = np.array([[]])

    # insert all the flights to the first queue for comparison
    def add_child(self, obj):
        self.queue_flights.append(obj)

    def build_the_matrix(self,  flights, tree, row, col):
        team_flights = None
        if self.flight_mat is None or flights is not None:  # first assignment for the tree
            self.flight_mat = [[0 for x in range(flights.__len__())] for y in range(flights.__len__())]

        if tree is None or flights is not None:     # first assignment for the tree
            tree.append(flights.pop(0))

        else:
            print("you have no flights in your sql")

        while flights.__len__() > 0:
             self.clash_flights(flights, tree, row, col)  # extract the first flight to tree
             tree.append(flights.pop(0))
             col += 1
             row += 1

        if tree is not None or flights is None:
            self.flight_mat[tree.__len__()-1][tree.__len__()-1] = 1
            #mat_of_teams = self.calc_the_num_of_emp(self.flight_mat, 0, 0)
            team_flights, number_of_teams = self.calc_the_num_of_emp2(self.flight_mat, self.queue_tree)
            """for i in range(mat_of_teams.__len__()):
                if mat_of_teams[i] == True:
                  number += 1
            self.num_of_teams = number
        return self.num_of_teams
        for i in self.flight_mat:
            print(i)"""
        self.team_flights = team_flights

    def clash_flights(self, flights, tree, row, col):
        # print(tree)
        if col == row:
            self.flight_mat[row][col] = 1
            col += 1

        while flights is not None:
            if row >= 0:
               if tree[row][0] != flights[0][0]:
                 time_difference = check_time_differences(tree[row][1], flights[0][2])

                 if time_difference is True:
                    self.flight_mat[row][col] = 0
                    self.flight_mat[col][row] = 0
                    row -= 1
                    # return False
                 else:
                    self.flight_mat[row][col] = 1
                    self.flight_mat[col][row] = 1
                    row -= 1
                    # return True
            else:
                break

    @staticmethod
    def is_flight_number_fit_to_team_id(team_id_to_flight_ids, flight_id, flight_matrix):
        for f_id in range(len(team_id_to_flight_ids)):
            if flight_matrix[team_id_to_flight_ids[f_id]][flight_id] == 1:
                return False
        return True

    @staticmethod
    def flight_id_already_exist(flight_id, team_ids_to_flight_ids):
        for team in team_ids_to_flight_ids:
            for f_id in team:
                if f_id == flight_id:
                    return True
        return False

    def calc_the_num_of_emp2(self, flight_matrix, flights):
        team_ids_to_flight_ids = []
        team_flights = TeamsFlights()
        number_of_flights_treated = 0

        for i in range(len(flight_matrix)):
            if number_of_flights_treated == len(flight_matrix):
                break
            if self.flight_id_already_exist(i, team_ids_to_flight_ids):
                continue
            team_ids_to_flight_ids.append([])
            for j in range(len(flight_matrix[i])):
                if self.flight_id_already_exist(j, team_ids_to_flight_ids):
                    continue
                if flight_matrix[i][j] == 0\
                   and self.is_flight_number_fit_to_team_id(team_ids_to_flight_ids[i], j, flight_matrix)\
                   or i == j:
                   team_ids_to_flight_ids[len(team_ids_to_flight_ids)-1].append(j)
                   team_flights.add_flight_to_team_by_id(len(team_ids_to_flight_ids)-1, flights[j])
                   number_of_flights_treated += 1
        print(type(team_flights))
        return team_flights, len(team_ids_to_flight_ids)

    def calc_the_num_of_emp(self, flight_matrix, row, col):
        toCheck = []
        decrease = 1

        while flight_matrix.__len__() -1 >= row:
            while flight_matrix.__len__()-1 >= col:
                if row == 0:
                   if flight_matrix[row][col] == 1:
                      toCheck.append(True)
                      col += 1
                   else:
                      toCheck.append(True)
                      toCheck[row] = False
                      row = col + 1
                else:
                    if flight_matrix.__len__() - 1 >= row:
                        if flight_matrix[row][col] == 1:
                           temp = col
                           while temp > 0:
                                if flight_matrix[row][temp] == 0 and temp-decrease == 0:
                                    toCheck[temp] = False
                                    decrease += 1
                                    break
                                elif flight_matrix[row][temp] == 0 and temp-decrease != 0:
                                    temp -= 1
                                else:
                                    temp -= 1
                           toCheck.append(True)
                        else:
                            toCheck[col] = False

                        row += 1
                        col += 1
                    else:
                        break
        return toCheck


class TeamsFlights:

    def __init__(self):
        self.flights = {}
        self.team_members = {}

    def add_flight_to_team_by_id(self, team_id, flight: tuple):
        if str(team_id) not in self.flights.keys():
            self.flights[str(team_id)] = []
        self.flights[str(team_id)].append(flight)

    def add_team_members(self, team_leaders, attendants):
        for i in range(len(self.flights)):
            self.team_members[str(i)] = {team_leaders[i], attendants[i]}
        """for j in self.flights:
           print(self.flights.get(j))
        for k in self.team_members:
           print(self.team_members.get(k))"""


conn = mysql.connector.connect(host='localhost',
                               database='ground_attendant',
                               user='root',
                               password='smadar')
cursor = conn.cursor()

# create object with flights needed to assigned with attendants
cursor.execute(
         ''' select flightNum,deptTime,boardingTime,date,destName
            from flights
            where boardingTime > 11 and boardingTime < 17
                ''')


assign_att = cursor.fetchall()
T1 = Tree()


def sort_by_boarding(flights):
    return flights[2]


for i in assign_att:
    T1.add_child(i)

T1.queue_flights.sort(key=sort_by_boarding)
for i in T1.queue_flights:
    print(i)

T1.build_the_matrix(T1.queue_flights, T1.queue_tree, 0, 0)

