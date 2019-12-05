import os
import shutil

path=input("enter the path :")
os.chdir(path)
def move_files(path):
	files=os.listdir(path)
	
	for i in files:
		file_path=path+'\\'+i
		if os.path.isfile(file_path):
			ext=os.path.splitext(file_path)[1]
			folder_name=f'{ext[1:]}s'
			if os.path.isdir(folder_name):
				shutil.move(i,folder_name)
			else:
				os.mkdir(f'{folder_name}')
				shutil.move(i,folder_name)

move_files(path)




