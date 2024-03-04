import numpy as np

tda = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(tda)

# # print(tda[1][4])
print(tda[1,4]) #5th element on te 2nd row

print(tda[0:2,2]) #2nd index element in both row


print(tda[0][0:2],tda[1][0:2]) #from index 0 to 1 on both rows
# # print(tda[0,0:1])
# # print(tda[1,0:1])

print(tda[0:2 ,1:4]) #from index 1 to 3 on both rows print(array[row position , index position])
# print(tda[0][1:4],tda[1][1:4])
# # print(tda[0,1:3])
# # print(tda[1,1:3])


tda = np.array([[10,8,1,6,2],[5,3,7,9,4]])
print(np.sort(tda))
