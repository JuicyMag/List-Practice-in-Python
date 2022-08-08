test = ['Hello', '1',True,'2.4', False]

# print(test)
# print(test[1], test[4], test[len(test)-3])



# for x in range(10):
#     number_list.append(x)
# print(number_list)

#this function will take a range defined by the user, and generate a list of those numbers
def generate_num_list(b):
    number_list = []
    for x in range(b):
        number_list.append(x)
    print(number_list)

generate_num_list(1000)
print(generate_num_list)