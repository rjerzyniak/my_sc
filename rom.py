#!/usr/bin/env python3.5
import subprocess
subprocess.call('clear',shell=True)

def menu():
    print(20 * '-')
    print("   Menu   ")
    print(15 * '-')
    print("1. Start Work")
    print("2. Stop Work")
    print("3. Sub_Menu")
    print("4. Exit")
    print(20 * '-')

menu()
# Get input #
choice = input('Enter your choice [1-3] : ')

# Convert string to int type #
choice = int(choice)

# Take action as per selected menu-option #
if choice == 1:
    #import webbrowser
    #webbrowser.register('firefox', None, webbrowser.GenericBrowser('firefox'), 1)
    #webbrowser.get('firefox').open('--browser')
    subprocess.call('nohup firefox &',shell=True)
    subprocess.call('nohup libreoffice --calc &',shell=True)
    subprocess.call('clear', shell=True)
    exec(open("./rom.py").read())
elif choice == 2:
    subprocess.call('killall firefox',shell=True)
    subprocess.call('killall oosplash',shell=True)
    exec(open("./rom.py").read())
elif choice == 3:
    exec(open("./sub_menu.py").read())
elif choice == 4:
    print("exit")
    subprocess.call("clear",shell=True)
else:
    print ("Wrong way please select another option")