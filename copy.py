import os, shutil, sys

sourcedirectory = sys.argv[1] 
destinationdirectory = sys.argv[2]
extension = sys.argv[3]

print "Usage : copy.py sourcedirname destinationdirname extension"

# For usage of os.walk refer https://www.geeksforgeeks.org/os-walk-python/ 

for root, dirs, files in os.walk(sourcedirectory):
    for file_ in files:
        if file_.endswith(extension):
            shutil.copy(os.path.join(root, file_), os.path.join(dstDir, file_))