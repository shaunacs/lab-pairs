from random import choice

all_students = []

present_students = []

rooms = ["Malala A", "Malala B", "Malala C", "Ruth A", "Ruth B", "Ruth C"]

pairings = []

while present_students != []:
    if len(present_students) > 1:
        student_to_pair = choice(present_students)
        present_students.remove(student_to_pair)
        pair = choice(present_students)
        present_students.remove(pair)
        pairings.append([student_to_pair, pair])
    else:
        last_pair = present_students[0]
        pairings[-1].append(last_pair)
        present_students.remove(last_pair)

# test push
for idx, pair in enumerate(pairings):
    if len(pair) == 2:
        print(f'{rooms[idx]} -- {pair[0]} & {pair[1]}')
    elif len(pair) == 3:
        print(f'{rooms[idx]} -- {pair[0]}, {pair[1]} & {pair[2]}')