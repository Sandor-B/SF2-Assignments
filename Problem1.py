#Given a 4 digit number, find the next number that has distinct digits
user = int(input("Give 4 digit num: "))

def is_distinct(num):
    return len(list(str(num))) == len(set(list(str(num))))

while not is_distinct(user):
    user += 1

print(user)
