test = ['Hello', '1',True,'2.4', False, 2, '4']
test_even_function = [0,1,2,3,4,5,6,7,8]
test_of_tens = [10,20, 30, 40 ,50 ,60 ,70, 71 ,80 ,99, 100]
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

odd_list = [x for x in test_even_function if x%2 !=0]
# print(odd_list)  

#func consumes a list and a returns a list of all numbers greater than floor
def is_greater_than_specified(list_of_values, floor):
    floor_list = []
    for num in list_of_values:
        if num > floor:
            floor_list.append(num)
    return floor_list



#func consumes a list and a returns a list of all numbers less than ceiling
def is_less_than_specified(list_of_values, ceiling):
    ceiling_list = []
    for num in list_of_values:
        if num < ceiling:
            ceiling_list.append(num)
    return ceiling_list

def remove_multiples_of_ten(list_of_values):
    list_of_no_tens = []
    for num in list_of_values:
        if num %10 !=0:
            list_of_no_tens.append(num)
    return list_of_no_tens


def remove_odd_numbers(list_of_values):
    list_of_no_odds = []
    for num in list_of_values:
        if num %2 ==0:
            list_of_no_odds.append(num)
    return list_of_no_odds

char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def remove_a_from_list(list_of_chars):
    no_a_list = []
    for char in list_of_chars:
        if char != 'a':
            no_a_list.append(char)
    return no_a_list

no_char_as = remove_a_from_list(char_list)
print(no_char_as)


# d = remove_odd_numbers(test_of_tens)
# print(d)
# no_tens_in_list = [x for x in test_of_tens if x %10 !=0]
# print(no_tens_in_list)
# c = remove_multiples_of_ten(test_of_tens)
# print(c)
# b = is_less_than_specified(test_even_function, 5)
# print(b)

# a = is_greater_than_specified(test_even_function, 5)
# print(a)


# generate_num_list(1000)
# print(generate_num_list)
# a = is_even(test_even_function)
# print(a)
# b = is_odd(test_even_function)
# print(b)