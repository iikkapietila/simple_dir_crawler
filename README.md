# simple_dir_crawler
This simple directory crawler copies files from sub directories to new directory. Can be for instance used in copying Moodle learning platform .zip export folder files into single folder. Copies only one copy per unique filename to destination.

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
