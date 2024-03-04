import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])


print("array is ", arr) #prints the array
print(type(arr)) #prints the type
print(arr[0]) #prints the zeroth element

print(arr[3] + arr[4]) #sums the 3rd and 4th index elements

print(arr[:4]) #first four elements

print(arr[4:]) #elements from index 4 onwards

print(arr[1:5:2]) #index 1 to 5 step 2

print(arr[1::2]) #every second elements 

print(np.where(arr==4)) #finding the position of elements 4

arr_sort = np.array([3,5,7,8,1,6,4,2,9])
print(sorted(arr_sort))