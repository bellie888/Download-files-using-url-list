# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:22:35 2017

@author: Joseph

This script looks for url in a particular column of a csv table
and then downloads and saves the file.

It does this within the folder the script is sitting in.

Used to download 1000s of pdf's from the NT Gov Boreholes construction logs.
But can be adapted to other uses

"""

import urllib
import csv
import time

# open the list file
with open(r'C:\temp\pdfs\AliceBores.csv') as csvfile:
    url_file = csv.reader(csvfile, delimiter= "," , quotechar='|')
    # remove the header    
    next(url_file)
    
    # for each url
    for row in url_file:
        # one second delay
        time.sleep(1)
        
        #build a name for the saved file - these are pdfs
        fileName = row[2] + ".pdf"
        myURL = row[4]
        try:
            urllib.urlretrieve (myURL, fileName)
            
        except:
            # 10 second delay
            time.sleep(10)
            urllib.urlretrieve (myURL, fileName)
            
        
        # track progress
        print row[2] + "       " + row[4]



print 'finished'