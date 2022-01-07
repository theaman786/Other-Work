num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
Biggest_Num = 0
if num1 >= num2:
    if num1 >= num3:
        Biggest_Num = num1
    else:
        Biggest_Num = num3
elif num1 >= num3:
    Biggest_Num = num2
elif num2 >= num3:
    Biggest_Num = num2
else:
    Biggest_Num = num3
print(Biggest_Num)