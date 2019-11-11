import random


def check_username(username):
	fr=open("randompassword.txt","r")
	lines=fr.readlines()
	names=[]
	for i in lines:
		names.append((i.split('-')[0]).rstrip())
	if username in names:
		return 1
	else:
		return 0


def gen_char(n):
	opstr=''
	letters_small=[chr(i) for i in range(ord("a"),(ord("z")+1))]
	letters_big=[chr(i) for i in range(ord("A"),(ord("Z")+1))]
	letters_small.extend(letters_big)
	for i in range(n):
		opstr+=random.choice(letters_small)
	return opstr


def gen_nums(m):
	opnums=''
	for i in range(m):
		opnums+=str(random.randint(0,9))
	return opnums

def gen_randompassword():
	password=''
	pw_pattern=int(input("enter pw pattern : "))
		
	for i in range(2):
		chars=gen_char(pw_pattern)
		nums=gen_nums(pw_pattern)
		password+=chars+nums
	
	return password


	

def write_password_to_file():

	fw=open("randompassword.txt","a")
	username=input("enter the username :")
	if check_username(username) is 1:
		print('username already exists')
	else:
		random_password=gen_randompassword()
		fw.write(f'{username}		-		{random_password} \n')

	fw.close()


write_password_to_file()


