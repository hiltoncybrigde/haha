import subprocess
import os

you =input("what you want bruh??? ")

robot_do = "cd /var/www"



if "make folder" in you:
	subprocess.Popen(robot_do, shell=True, stdout=subprocess.PIPE).stdout.read()
	robot_brain = "nice \"First commit\""
	print (robot_brain)
	project_name = input("what yours project name bruh??? ")
	robot_do_2 = "cd "+project_name
	path = '../'+project_name
	if os.path.exists(path):
		getVersion =  subprocess.Popen(robot_do, shell=True, stdout=subprocess.PIPE).stdout.read()
		folder_name = input("what do you want yours folder name bruh??? ")
		robot_do_3 = "mkdir ../"+project_name+"/"+folder_name
		subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()
	else:
		folder_name = input("what do you want yours new folder name bruh??? ")
		robot_do_3 = "mkdir ../"+folder_name
		subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()
		robot_brain = "done yours new folder is "+folder_name
		print (robot_brain)
elif "git" in you:
	subprocess.Popen(robot_do, shell=True, stdout=subprocess.PIPE).stdout.read()
	robot_brain = "nice"
	print (robot_brain)
	project_name = input("what yours project name bruh??? ")
	robot_do_2 = "cd ../"+project_name
	path = '../'+project_name
	if os.path.exists(path):
		git_already = input("git yet?[y/n] ")
		if git_already == "y":
			commit = input("what yours commit name bruh??? ")
			robot_do_3 = "cd ../"+project_name+"\n"+"git add ."+"\n"+"git commit -m \""+commit+"\""+"\n"+"git push -u origin master"+"\n"
			subprocess.Popen(robot_do_3, shell=True, stdout=subprocess.PIPE).stdout.read()			
			robot_brain = "done"
			print (robot_brain)

elif you == "":
	robot_brain = "bye bro"	


