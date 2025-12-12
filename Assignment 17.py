'''

Challenge: Optimize the function to handle large input lists efficiently.

==============================
Description: Develop a function called find_common_elements that takes two lists as input and returns a new list
containing elements that are common to both input lists.

'''

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

faiza = [1, 2, 3, 4, 5, 6]
generated = [10,5,6,0,20,50]

result = find_common_elements(faiza, generated)
print(result)