def get_fibonacci_number(position):
    pass #Remove this line and insert your code here. Do not forget this function implements recursion.

def get_fibonacci_number_sequence(number):
    pass #Remove this line and insert your code here. Do not forget to use get_fibonacci_number to create your list of numbers.

#most of this code was done in class from Dr. Calderon's lecture. Will refine later



# def count_number(n):
#     for x in range(n):
#         print(x+1)

# def count_number_with_recursion(number):
#     if number > 0:
#         print(number)

# # count_number(10)

# count_number_with_recursion(15)
#recursion = function + iterative process + boolean that keeps process going, 



# def bubble_sort_with_recursion(list_to_order,sort_length=None):
#     if sort_length is None:
#         sort_length = len(list_to_order)
    
#     if sort_length == 1:
#         return
    
#     for i in range(sort_length-1):
#         if list_to_order[i]>list_to_order[i+1]:
#             temp_variable = list_to_order[i+1]
#             list_to_order[i+1] = list_to_order[i]
#             list_to_order[i] = temp_variable

#     print(list_to_order)
#     bubble_sort_with_recursion[list_to_order,sort_length-1]

# list_to_test=[12,3,5,36,46254,234,21,2,7,7445,66,8]

# bubble_sort_with_recursion(list_to_test)

# print(list_to_test)

#fibonacci without recursion

# def get_fibonacci_number(number):
#     if number == 0:
#         return 0
#     if number == 1:
#         return 1
    
#     previous_a = 0
#     previous_b = 1

#     for x in range(2,number+1):
#         current_fibonacci_number = previous_a + previous_b
#         previous_a = previous_b
#         previous_b = current_fibonacci_number

#     return previous_b
# def get_fibonacci_sequence(n):
#     if n == 0:
#         return [0]
    
#     if n == 1:
#         return [0,1]
    
#     previous_x = 0
#     previous_y = 1

#     number_sequence = [0,1]

#     for i in range(2, n+1):
#         current = previous_x + previous_y
#         previous_x = previous_y
#         previous_y = current

#         number_sequence.append(current)

#     return number_sequence

# print(get_fibonacci_number(3))

def fibonacci_number_with_recursion(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    return fibonacci_number_with_recursion(number-1)\
        +fibonacci_number_with_recursion(number-2)

print(fibonacci_number_with_recursion(6))

if __name__ == "__main__":
    pass #Remove this line and insert your code to test your Fibonacci function here