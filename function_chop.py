'''Exercise 1: Write a function called chop that takes a list 
and modifies it, removing the first and last elements, and returns None.
 Then write a function called middle that takes a list and returns a new list 
that contains all but the first and last elements.'''


def chop(t):
    del t[0]              #deletes first
    del t[-1]             #deletes last
    return t
    # print(t)  # print('None.')        #Returns None or print None?


def middle(t):
    return t[:]

# Prompt the user for list input:
list_input = input('Enter the values of the list to be chopped and middled separated by spaces: ')
#lista2 = input('Enter the values of the list to be meddled: ')

# split the string to get individual numbers
splitted_input = list_input.split()

# Convert the number strings to interger to create the list
lista = [int(num) for num in splitted_input]

print('The list is: ', lista)
chopped_lista = chop(lista)
print('The chopped list is: ', chopped_lista)

middled_lista = middle(lista)
print('the list after middling is: ', middled_lista)