#Script Name    :fileinfo.py
#Author         :zhengxu
#Created        :24th March 2020
#Last Modified  :
#Version        :1.0
#Modifications  :

#Description    :show files information for a given file

from ___future___ import print_function

import os
import stat
import sys
import time

if sys.version_info >=(3 , 0):
	raw_input = input

file_name =	raw_input("Enter a file name: ")
count = 0
t_char = 0
try:
	with open(file_name) as f:
		line = f.readline()
		t_char += len(line)
		while line:
			count += 1
			line = f.readline()
			t_char +=len(line)
except FileNotFoundError as e:
	print(e)
	sys.exit()
# When open item is a directory (python2)
except IOError:
    pass
# When open item is a directory (python3)
except IsADirectoryError:
    pass

file_stats = os.stat(file_name)
# create a dictionary to hold file info
file_info = {
    'fname': file_name,
    'fsize': file_stats[stat.ST_SIZE],
    'f_lm': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_MTIME])),
    'f_la': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_ATIME])),
    'f_ct': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_CTIME])),
    'no_of_lines': count,
    't_char': t_char
}
# print out the file info
