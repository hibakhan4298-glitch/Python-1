'''
Develop a function called sort_list that takes a list of numbers as input and returns a new list
containing the same elements sorted in ascending order.

'''

def sort_list(numbers):
    return sorted(numbers)

nums = [5, 7, 9, 4, 3]
result = sort_list(nums)
print("Sorted list:", result)