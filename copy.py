import os, shutil, sys

sourcedirectory = sys.argv[1] 
destinationdirectory = sys.argv[2]
extension = sys.argv[3]

print "Copying file with extension", extension, "from", sourcedirectory, "to",destinationdirectory 

# For usage of os.walk refer https://www.geeksforgeeks.org/os-walk-python/ 

for root, dirs, files in os.walk(sourcedirectory):
    for file in files:
        if file.endswith(extension):
            shutil.copy(os.path.join(root, file), os.path.join(destinationdirectory, file))
