import os
import time
import shutil

"""
This script can be used to copy files from subfolders to new folder. Usable 
for example when you copy group assignments from Moodle and receive them in a
zip that contains folders which contain the proper assignments. In such
situations it might be frustrating to go through the folders one by one when
you can simply use this script to copy files from each folder to a destination
folder.

This script also takes into consideration whether the assignment has been 
submitted as a group. In this case Moodle export zip contains as many copies
of the assignment as there are group members. This script copies each unique
file(name) only once.


By Iikka Pietilä 2018
"""

# Dir is the directory path that supposedly includes folders that include
# the assignments. Dest is the directory path where you want the copies to be
# saved in.

dir = (r"C:\Users\pietilai\KAKOPER_LOCAL_TEMP")

# Please note that destination folder needs to exist before execution
dest = (r"C:\Users\pietilai\KAKOPER_LOCAL_TEMP\output")

def list_files(dir):
    print("dir = ", dir)
    print()
    directory_listing = os.listdir(dir)
    filenamelist = []

    # filename list happens here (only for counting purposes)
    counter = 0
    for row in directory_listing:
        subdir_listing = os.listdir(dir + "/" + row)
        counter = counter + 1

        for row in subdir_listing:
            if row not in filenamelist:
                filenamelist.append(row)

    # copier itself starts here
    uniquedir_list = []
    for row in directory_listing:
        folder = row
        eachdirlist = os.listdir(dir + "/" + row)

        for row in eachdirlist:
            if row not in uniquedir_list:
                uniquedir_list.append(row)
                shutil.copy2(dir + "/" + folder + "/" + row, dest + "/" + row)

                print()
                print("file name:", row)
                print("from dir: ", dir)
                print("to dir: ", dest)
                print("destination filename: ", row)
                i = 0
                x = 0
                y = 5

                while i <= 5:
                    print("#" * x, "." * y)
                    x = x + 1
                    y = y - 1
                    i = i + 1
                    time.sleep(0.1)

                print()
                print("done")
                print()

    #this tells the number of files with unique filename
    print("filenamelist len = ", len(filenamelist))

list_files(dir)