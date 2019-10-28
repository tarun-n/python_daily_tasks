#except multiples of 3 and 5
n=int(input("enter the range :"))
for i in range(n+1):
    if i%3==0 or i%5==0:
        continue
    print(i,end=" ")

#even number square
n=int(input("enter the range :"))
for i in range(n+1):
    if i%2==0:
        print(i**2,end=" ")

#odd dived by 7
for i in range(101):
    if i%2!=0 and i%7==0:
        print(i)

#vowels

string=input("enter a string :")
vowels="aeiou"
for i in string:
    if i in vowels:
        print(i)
