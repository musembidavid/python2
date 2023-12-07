print("calculator")

print("enter number one")
num1 = input()

print("enter number two")
num2 = input()



choice =  input()

print("Selct an opr")
print(" 1 for addition")
print("2 for subtration")
print("3 for multiplication")
print("4 for division")


if choice == 1:
    sum = num1 + num2
    print("the answer is" + sum)

if choice == 2:
    res = num1 - num2
    print("the answer" + res)

if choice == 3:
    sum = num1 * num2
    print("the answer is " + sum)

if choice == 4:
    ans = num1 / num2
    print(" the answer is" + ans)
