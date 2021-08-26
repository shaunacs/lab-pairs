from random import choice

all_students = []

present_students = []

rooms = ["Malala A", "Malala B", "Malala C", "Ruth A", "Ruth B", "Ruth C"]


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