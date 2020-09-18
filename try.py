num=12345
output=map(int,str(num))
input('Enter the number : ')


n= 12345
sum=0
while n >0 :
    m= n %10
    sum +=m
    n=n//10
print(sum)