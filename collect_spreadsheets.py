# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:55:08 2016
Script to join together Numbers & CSV files into a single long one.

@author: ejetzer
"""

''' Note to self: Fuck Apple's file formats.'''
#import zipfile # To open Numbers files downloaded from iCloud on Ubuntu
import csv # To open text files written up in Drafts on iPad
#import plistlib # Manipulate the contents of Numbers files
import pathlib # To easily go through the directory and keep track of files
import sys # To get command line arguments

def main(loc, folder):
    lines = []
    files = folder.glob('*.csv')
    for f in files:
        with f.open(newline='') as f:
            lines += list(csv.reader(f))
    with loc.open('w', newline='') as f:
        ss = csv.writer(f)
        ss.writerows(lines)

if __name__ == '__main__':
    loc, folder = 'total.csv', '.'
    if '-o' in sys.argv:
        i = sys.argv.index('-o') + 1
        loc = pathlib.Path(sys.argv[i])
    if '-i' in sys.argv:
        i = sys.argv.index('-i') + 1
        folder = pathlib.Path(sys.argv[i])
    main(loc, folder)
    print('Done.')