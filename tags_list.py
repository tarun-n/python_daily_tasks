x=[2,3,4,7,5,8,6,3,4,7,2,3,4]
sub=[]
big=[]

for i in range(0,len(x)-1):
	sub=[x[i],x[i+1]]
	big.append(sub)
	sub=[]

print(big)
	
for i in big:
	if i not in sub:
		sub.append(i)
for i in sub:
	print(f' the count of {i} in the list is {big.count(i)}')
	


# tags

stmt = "TNS is looking for a Sr software developer to join a team that is responsible for the development and maintenance of the TNSOnline and MMIS web portals. The TNS web portal is used by internal and external customers to monitor and report on transactions processed through the TNS network."
tags = ['B', 'O', 'O', 'O', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'O','O', 'B', 'O', 'B', 'B', 'B', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'B', 'B', 'B', 'B', 'O', 'B', 'O', 'B', 'O', 'B', 'B', 'O', 'O', 'B', 'B']
stmt=stmt.split()
l1=[]
opstr=''
for i in range(len(tags)):
   
    if tags[i] is 'B':
        if i==len(tags)-1:
            opstr=opstr+stmt[i]
            l1.append(opstr)
        elif tags[i+1] is 'B' :
            opstr=opstr+stmt[i]+' '
        else:
            opstr=opstr+stmt[i]
            
    elif opstr!="":
        l1.append(opstr)
        opstr=''
print(l1)