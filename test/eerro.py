# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# print('hello word!')
print("Give me two numbers,and I'll divide them ")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
