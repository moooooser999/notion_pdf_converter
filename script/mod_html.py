import sys
import os
from os import listdir
from os.path import isfile, join

from tqdm import tqdm
from pyquery import PyQuery as pq
import codecs
from bs4 import BeautifulSoup

mypath = os.getcwd()
os.chdir(mypath+"/html")
mypath = os.getcwd()
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-5:] == '.html']
str1_ = """	body {
                margin: 2em auto;
                max-width: 700px;
                color: rgb(55, 53, 47);
        }\n"""
str2_ = """	overflow:hidden;\n"""
print("Preprocessing HTML FILE to Decent Format ...")
for file_path in tqdm(files):
    print(file_path)
    flag_1 = 0
    flag_2 = 0
    with open(file_path, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('@media only print {'):   # find a pattern so that we can add next to that line
                flag_1 = 1
                lines[i] = lines[i]+str1_
            if line.startswith('.bookmark-href {'):
                flag_2 = 1
                lines[i] = lines[i]+str2_
            if flag_1 and flag_2:
                break

        f.truncate()
        f.seek(0)                                           # rewrite into the file
        for line in lines:
            f.write(line)

print('Finish!')
