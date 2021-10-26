from random import choice
from students import all_students, present_students

rooms = ["Malala A", "Malala B", "Malala C", "Malala D", "Malala E", "Malala F", "Ruth A", "Ruth B", "Ruth C"]


def make_lab_pairs(students, rooms):
    """Makes lab pairs from list of students and list of rooms"""

    pairings = []

    while students != []:
        if len(students) > 1:
            student_to_pair = choice(students)
            students.remove(student_to_pair)
            pair = choice(students)
            students.remove(pair)
            pairings.append([student_to_pair, pair])
        else:
            last_pair = students[0]
            pairings[-1].append(last_pair)
            students.remove(last_pair)

    for idx, pair in enumerate(pairings):
        if len(pair) == 2:
            print(f'{rooms[idx]} -- {pair[0]} & {pair[1]}')
        elif len(pair) == 3:
            print(f'{rooms[idx]} -- {pair[0]}, {pair[1]} & {pair[2]}')


def make_random_student_list(students):
    """Shuffles list of students"""

    shuffled_students = []

    while students != []:
        student_to_add = choice(students)
        shuffled_students.append(student_to_add)
        students.remove(student_to_add)
    
    return shuffled_students


def make_whiteboarding_groups(students):

    malala_a = []
    malala_b = []
    malala_c = []
    malala_d = []


    while students != []:
        if len(malala_a) <= 3:
            student = choice(students)
            malala_a.append(student)
            students.remove(student)
        elif len(malala_b) <= 2:
            student = choice(students)
            malala_b.append(student)
            students.remove(student)
        elif len(malala_c) <= 2:
            student = choice(students)
            malala_c.append(student)
            students.remove(student)
        else:
            student = choice(students)
            malala_d.append(student)
            students.remove(student)

    print(", ".join(malala_a))
    print(", ".join(malala_b))
    print(", ".join(malala_c))
    print(", ".join(malala_d))