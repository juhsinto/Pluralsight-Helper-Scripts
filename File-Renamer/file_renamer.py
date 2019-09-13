import os

cwd = os.getcwd()

os.mkdir(cwd + "/dirs")

# all the video files should be numbered in the /input directory within cwd
path = cwd + "/input/"

f = open("toc.txt", "r")
for line in f:
	if "\t" in line:
		if "/" in line:
			line = line.replace("/", " ")
		renamed_file = line.replace("\t", "").replace("\n", "") + ".mp4"
		file_name = line.split("-")[0].replace("\t", "").strip() + ".mp4"
		print renamed_file
		is_file_to_check = path + file_name
		renamed_file = cwd + "/dirs/" + renamed_file
		if os.path.isfile(is_file_to_check):
			os.rename(is_file_to_check, renamed_file)
		# print "meh"
	else:
		if "/" in line:
			line = line.replace("/", " ")
		dir_name = line.replace("\n", "")
		os.mkdir(cwd + "/dirs/" + dir_name)
		# print "meh - directory ; dont do anything"
		
