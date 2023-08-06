'''Exercise 1: Write a function called chop that takes a list 
and modifies it, removing the first and last elements, and returns None.
 Then write a function called middle that takes a list and returns a new list 
that contains all but the first and last elements.'''

lista2 = input('Enter the values of the list to be chopped: ')
#lista2 = input('Enter the values of the list to be meddled: ')
lista = int(lista2)
def chop(t):
    del t[0]              #deletes first
    del t[-1]             #deletes last
    print('None.')        #Returns None or print None?


def middle(t):
    return t[:]


print('The list is: ', lista)
chopped_lista = chop(lista)
print('The chopped list is: ', chopped_lista)

middled_lista = middle(lista)
print('the list asfter middling is: ', middled_lista)
#print(middle(lista))
'''
def chop(lst):
    """
    Takes a list, modifies it, removing the first and last elements, and
    returns None.
    Input:  lst -- a list
    Output: None
"""
    del lst[0]                          # Removes the first element
    del lst[-1]                         # Removes the last element


def middle(lst):
    """
    Takes a list and returns a new list that contains all but the first and
    last elements.
    Input: lst -- a list
    Output: new -- new list with first and last elements removed
    """
    new = lst[1:]                       # Stores all but the first element
    del new[-1]                         # Deletes the last element
    return new


my_list = [1, 2, 35, 4]
my_list2 = [1, 2, 38, 4, 90, 64]

chop_list = chop(my_list)
print(my_list)                          # Should be [2,3]
print(chop_list)                        # Should be None

middle_list = middle(my_list2)
print(my_list2)                         # Should be unchanged
print(middle_list)                      # Should be [2,3]
    '''