total = 0
student = 1
lockers = [0] * 1000
target = 0
for x in range(1000):
    student = student + 1
    for i in range(1000//student):
        target = i * student
        target = target + student - 1
        if lockers[target] == 0:
            lockers[target] = 1
        else:
            lockers[target] = 0
for i in range(1000):
    if lockers[i] == 0:
        total = total + 1
print(total)
