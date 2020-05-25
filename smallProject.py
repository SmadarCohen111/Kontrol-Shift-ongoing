import mysql.connector


# check whether the time differences allow us to set father & child, static function
def check_time_differences(first_hour, second_hour):
    arr_of_fh = first_hour.split(":")
    arr_of_sh = second_hour.split(":")
    str_of_fh = arr_of_fh[0] + arr_of_fh[1]
    str_of_sh = arr_of_sh[0] + arr_of_sh[1]
    first_cast = int(str_of_fh)
    second_cast = int(str_of_sh)
    if second_cast - first_cast > 20 or second_cast - first_cast == 20 and second_cast - first_cast < 30 or second_cast - first_cast == 30:
        return True
    else:
        return False


class Tree(object):
    parent = []
    children = []
    queue_flights = []
    queue_tree = []

    # insert all the flights to the first queue for comparison
    def add_child(self, obj):
        self.queue_flights.append(obj)

    # build the tree
    def _insert(self, flights, possible_fathers_tree, counter):
        positioning_fc = Tree()                                      # create object, assign to fathers children's queue
        if possible_fathers_tree is None or flights is not None:     # first assignment for the tree
            possible_fathers_tree.append(flights.pop(0))

            while flights.__len__() > 0:
                  check_insert = self.equal_flight(flights, possible_fathers_tree, positioning_fc.parent, positioning_fc.children, counter)  # extract the first flight to tree

                  if flights.__len__() > 0 and check_insert is False:
                      possible_fathers_tree.append(flights.pop(0))
                      counter += 1

                  elif flights.__len__() > 0 and check_insert is True:
                       counter -= 1
                       continue

                  else:
                      break

    # make sure that we make the right is insertion and check whether we have a match father & son
    def equal_flight(self, flights, possible_fathers_tree, parent, children, counter):

        while counter >= 0 and flights is not None:
            if possible_fathers_tree[counter][0] != flights[0][0]:
                time_difference = check_time_differences(possible_fathers_tree[counter][1], flights[0][2])

                if time_difference is True and self.queue_tree.__len__() == 1:   # if the time differences is good,
                   parent.append(possible_fathers_tree.pop(0))             # and we have only one potential father
                   children.append(flights.pop(0))
                   return True

                elif time_difference is True and self.queue_tree.__len__() > 1:    # if the time differences is good,
                   parent.append(possible_fathers_tree.pop(0))                  # potential father
                   children.append(flights.pop(0))
                   return True

                else:                                                              # no one matches to be the father
                  counter -= 1
        return False


conn = mysql.connector.connect(host='localhost',
                               database='ground_attendant',
                               user='root',
                               password='smadar')
cursor = conn.cursor()

# create object with flights needed to assigned with attendants
cursor.execute(
         ''' select flightNum, deptTime, boardingTime, destName
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


T1._insert(T1.queue_flights, T1.queue_tree, 0)
counter = 1
for p in T1.parent:
    print("father: ", p, " number: ", counter)
    counter += 1

count = 1
for c in T1.children:
    print("child: ", c, " number: ", count)
    count += 1

#for p in T1.parent and c in T1.children:
#        print("this is my child: ", c, "im your father: ", p)


for qt in T1.queue_tree:
    print("i'm a father without children: ", qt)