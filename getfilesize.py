#! python3
# iterate through all files in a directory
# return the sum total of all files

import os

totalSize = 0

#TODO Add Error Check for non-existing directory
directory = input('Enter the directory you want sized:\n')

#TODO Enable Sub-directory Sizing (Recursion?!)
# currently only sizes main folder
for filename in os.listdir(directory):
    totalSize += os.path.getsize(os.path.join(directory, filename))

print("Total Size = {}".format(totalSize))
