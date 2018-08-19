#!/usr/bin/env python3
# bigFileSearch - Finds files larger than a given size in a folder
# and returns to the paths to those files
# Usage: python3 bigFileSearch.py path/to/source <filesize (MB)>

import os
import shutil
import sys


def bigFileSearch(source, size):

    # Make source path an absolute path
    source = os.path.abspath(source)
    pathlist = []

    for foldername, subfolders, filenames in os.walk(source):
        print('Searching in %s...' % (foldername))
        for filename in filenames:
            filePath = os.path.join(foldername, filename)
            try:
                if (os.path.getsize(filePath)/1000000 > int(size)):
                    pathlist.append(filePath)
            except FileNotFoundError:
                continue

    print('The following files are over %sMB:' % (size))
    for path in pathlist:
        print('Path: ' + path)


bigFileSearch(sys.argv[1], sys.argv[2])
