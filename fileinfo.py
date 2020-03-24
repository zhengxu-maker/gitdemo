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
file_info_keys = ('file name', 'file size', 'last modified', 'last accessed',
                  'creation time', 'Total number of lines are',
                  'Total number of characters are')
file_info_vales = (file_info['fname'], str(file_info['fsize']) + " bytes",
                   file_info['f_lm'], file_info['f_la'], file_info['f_ct'],
                   file_info['no_of_lines'], file_info['t_char'])

for f_key, f_value in zip(file_info_keys, file_info_vales):
    print(f_key, ' =', f_value)

# check the `file` is direcotry
# print out the file stats
if stat.S_ISDIR(file_stats[stat.ST_MODE]):
    print("This a directory.")
else:
    file_stats_fmt = ''
    print("\nThis is not a directory.")
    stats_keys = ("st_mode (protection bits)", "st_ino (inode number)",
                  "st_dev (device)", "st_nlink (number of hard links)",
                  "st_uid (user ID of owner)", "st_gid (group ID of owner)",
                  "st_size (file size bytes)",
                  "st_atime (last access time seconds since epoch)",
                  "st_mtime (last modification time)",
                  "st_ctime (time of creation Windows)")
    for s_key, s_value in zip(stats_keys, file_stats):
        print(s_key, ' =', s_value)
