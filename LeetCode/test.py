import random

TRIALS = 100000
num_people = 23
same_birthdays = 0

for _ in range(TRIALS):
    birthdays = []

    for i in range(num_people):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f'{same_birthdays / TRIALS * 100}%')
         
