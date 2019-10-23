#amstrong

n=int(input("enter a number :"))
c=0
temp=n
while temp>0:
    i=temp%10
    c=c+(i**3)
    temp//=10
if c==n:
    print(f'{n} is an amstrong number')
else:
    print("%d is not an amstrong number"%(n))



#prime


n=int(input("enter a number :"))
c=0
for i in range(1,n+1):
    for j in range(1,i+1):
        c+=1
if c==2:
    print("%d is an prime number"%n)
else:
    print("%d is not an prime number"%n)



#febonacci


n=10
a=0
b=1
print(a)
print(b)
for i in range(n+1):
    c=a+b
    a=b
    b=c
    print(c)



#odd even count


n=int(input("enter the starting range :"))
m=int(input("enter the ending range :"))
c=0
d=0
for i in range(n,m+1):
    if i%2==0:
        c+=1
    else:
        d+=1
print("there are %d even numbers in the given range"%c)
print("there are %d odd numbers in the given range"%d)




#pattern


n=5
for i in range(1,n+1):
    print("*"*(n-i))'''

#multiple of 9
'''n=int(input("enter a number :"))
if n%9==0:
    print('%d is an multiple of 9'%n)
else:
    print("%d is not a muntiple of 9"%n)



#divisible by 2or3


for i in range(0,51):
    if i%2==0 and i%3==0:
        print(i)





#sum of digits of numbers


n=int(input("enter a number :"))
temp=n
sum=0
while temp>0:
    r=temp%10
    sum+=r
    temp//=10
print(sum)
    


        


