import numpy as np

thda = np.array([[[1,2,3],
                  [4,5,6]],
                 [[7,8,9,],
                  [10,11,12,]]])
print(thda)

print(thda[0,1,2])
print(thda.shape) #(metrix,row,element)
print(np.sort(thda))

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr = np.concatenate((arr1,arr2))
print("concatenated array:- ",new_arr)
# print(f"concatenated array:- {new_arr}")

thda1 = np.array([[[1,2,3],
                  [4,5,6]],
                 [[7,8,9,],
                  [10,11,12,]],
                 [[7,8,9,],
                  [10,11,12,]]])
print(thda1.shape) #(3,2,3)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.array_split(arr,3))