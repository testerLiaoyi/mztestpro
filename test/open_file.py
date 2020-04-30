try:
    with open('pi_digit.txt') as file_object:
        lines = file_object.read()
except FileNotFoundError:
    msg = "file notfound"
    print(msg)
    # print(contents)
    # for line in file_object:
    #     print(line.rstrip())
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))
