test = ['Hello', '1',True,'2.4', False, 2, '4']
test_even_function = [0,1,2,3,4,5,6,7,8]

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
    # print(number_list)

def is_even(list):
    even_list = []
    for element in list:
        if element %2 ==0:
            even_list.append(element)
    return even_list

def is_odd(list):
    odd_list = []
    for element in list:
        if element %2 !=0:
            odd_list.append(element)
    return odd_list   

# generate_num_list(1000)
# print(generate_num_list)
# a = is_even(test_even_function)
# print(a)
b = is_odd(test_even_function)
print(b)