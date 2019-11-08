# fo=open("demo.txt","w")
# n=int(input("enter a number"))
# fo.write(str(n)+"\n")
# for i in range(n):
# 	fo.write(chr(ord("a")+i) + "\n")
# fo.close()

# def write_data():

# 	fw=open("users.txt","a")
# 	name=input("enter the name :")
# 	password=input("enter the password :")
# 	fw.write(f'{name}     -       {password} \n')
# 	fw.close()
# #write_data()



def checkpassword(password):
	a=0
	b=0
	c=0
	d=0
	
	for i in password:
		if ord(i)>=ord("a") and ord(i)<=ord("z"):
			a+=1
		elif ord(i)>=ord("A") and ord(i)<=ord("Z"):
			b+=1
		elif i is "@" or i is "#" or i is "$" or i is "&" or i is "*" or i is "-" or i is "!":
			c+=1
		elif i.isdigit():
			d+=1

	if a>0 and b>0 and c>0 and d>0:
		return 1
	else:
		print("password is invalid")
		return 0
				


# print(checkpassword("tarUn@1997"))				





def checkname():
	name=input("enter the name :")
	fr=open("users.txt","r")
	lines=fr.readlines()
	usernames=[]
	for i in lines:
		usernames.append((i.split("-")[0]).rstrip())
	if name  in usernames :
		print("user name exists")
												
	else:
		password=input("enter the password  :")
		password_strength=checkpassword(password)
		if password_strength ==1:
			fw=open("users.txt","a")
			fw.write(f'\n{name}    -      {password}\n')
checkname()



