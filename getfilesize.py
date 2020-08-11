#! python3
# iterate through all files in a directory
# return the sum total of all files

import os

totalSize = 0

directory = input('Enter the directory you want sized:\n')

for filename in os.listdir(directory):
    totalSize += os.path.getsize(os.path.join(directory, filename))

print("Total Size = {}".format(totalSize))
