input_list = [1, 2, 3, 4, 5, 6, 7]

# bad practice
for i in range(len(input_list)):
    print(i, input_list[i])

# best practice
for index, value in enumerate(input_list):
    print(index, value)
