array1=[3,8,98,54,11,33, 9834, 234, 234234, 23423234]
max1=max(array1)
array2=array1.copy()
array2.remove(max1)
max2=max(array2)
print(max1*max2)