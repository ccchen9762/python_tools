import os
import shutil
import re

#directories
#dir_init = input("Input initial directory: ")
dir_init = "C:\\Users\\M100_2\\Desktop\\A"
#dir_des = input("Input destination directory: ")
dir_des = "C:\\Users\\M100_2\\Desktop\\B"

#open file
file_name = "re_rules.txt"
re_file = open(file_name, "r")
print("opening " + file_name + "\n")

#add new rules
pass
#name = ""
#re_rule = ""

#regex rules
lines = re_file.readlines()
regexes = {}
for line in lines:
	rules=[]
	pair = line.split(":")
	for rule in pair[1][0:-2].split(","):
		rules.append(re.compile(rule[0::]))
	regexes[line.split(":")[0]] = rules
	
#processing folders
folders = os.listdir(dir_init)
for folder in folders:
	author=""
	#extract all author names
	for regex in regexes:
		if author =="":
			for rule in regexes[regex]:
				match = re.search(rule, folder)
				if match:
					author = match.group(0)[1:-1]
				else:
					author=""
					break
	#moving folders
	if not author=="":
		print("Find author: "+author)
		if not os.path.isdir(dir_des+"\\"+author):
			print("New author, make folder " + dir_des + "\\" + author)
			os.mkdir(dir_des+"\\"+author)
		shutil.move(dir_init+"\\"+folder, dir_des+"\\"+author+"\\"+folder)
		print("moving \"" + dir_init+"\\"+folder + "\"to \"" + dir_des+"\\"+author+"\\"+folder+"\"\n")

#done
print("Done!")