#https://github.com/ONETAPL3G3ND
import os
for entry in os.scandir("/home/user/Desktop"):
	print(entry.name, entry.is_dir(), entry.is_file())
