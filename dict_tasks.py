
d={"python":3,"mysql":7.2,"php":8,"java":8}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for i in d.items():
    print(i)
     
###############



n=int(input("enter a number"))
s={}
for i in range(0,n+1):
      s[i]=i**2
print(s)

n=int(input("enter start point"))
m=int(input("enter end  point"))
s={}
l=[]
for i in range(n,m+1):
    l.clear()
    for j in range(1,i+1):
        if i%j==0:
            l.append(j)
        s[i]=l
print(s)


###############


l1=[1,2,3,4]
l2=[12,23,45,6]
d={}
if len(l1)==len(l2):
    for i in range(len(l1)):
        d[l1[i]]=l2[i]
print(d)


############
    
stmt=input("enter stmt : ")
#stmt.split()
d={}
string=""
for i in stmt.split():
    for j in range(0,len(i)):
        string+=str(chr(ord(stmt[j])+1))
        d[i]=string

#adding keys and valuse to the dictionary
d={}
d["python"]=3.7
d["java"]=8
d["html"]=5
print(d)
n=int(input("enter how many key value pairs to add: "))
for i in range(n):
    key=input("enter a key :")
    value=input("entter a value :")
    d[key]=value
print(d)

#concatination of dictionaries
dict1={100:1,200:2,300:3,400:4,500:5}
dict2={10:1,20:2,30:3,40:4,50:5}
dict1.update(dict2)
print(dict1)

#iterating dictionary using for loop
d={'python': 3.7, 'java': 8, 'html': 5, 'pip': 8, 'mysql': 7}
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)

#removing an element from dictionary
d={'python': 3.7, 'java': 8, 'html': 5, 'pip': 8, 'mysql': 7}
print(d)
del d['pip']
print(d)
d.pop('mysql')
print(d)
d.popitem()
print(d)

