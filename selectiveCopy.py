#!/usr/bin/env python3
# selectiveCopy.py - walks through a folder and copies files of a given extension
# into a new folder
# Usage: selectiveCopy.py path/to/folder <extension> path/to/destination

import os, sys, shutil

def selectiveCopy(folder, extension, destination):

    #make sure folder path is absolute
    folder = os.path.abspath(folder)
    os.makedirs(destination)

    #walk through folder to find files
    for foldername, subfolders, filenames in os.walk(folder):
        print('Copying %s files in %s...' %(extension, foldername))

        #copy files to new destination
        for filename in filenames:
            if filename.endswith(extension): #check that files have correct extension befoer copying
                shutil.copy(os.path.join(foldername, filename), os.path.join(destination, filename))
                print('Copying %s...' %(filename))


selectiveCopy(sys.argv[1], sys.argv[2], sys.argv[3])
