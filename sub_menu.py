#!/usr/bin/env python3.5
import subprocess
subprocess.call('clear',shell=True)

def menu():
    print(20 * '-')
    print("  Start and Stop ")
    print(15 * '-')
    print("1. Start Libreoffice")
    print("2. Stop Libreoffice")
    print("3. Start FIREFOX")
    print("4. Stop Firefox")
    print("5. Back")
    print("6. Exit")
    print(20 * '-')

menu()
# Get input #
choice = input('Enter your choice [1-6] : ')

# Convert string to int type #
choice = int(choice)

if choice == 1:
    subprocess.call('nohup libreoffice --calc &', shell=True)
    subprocess.call('clear', shell=True)
    exec(open("./sub_menu.py").read())
elif choice == 2:
    subprocess.call('killall oosplash',shell=True)
    exec(open("./sub_menu.py").read())
elif choice == 3:
    subprocess.call('nohup firefox &',shell=True)
    subprocess.call('clear',shell=True)
    exec(open("./sub_menu.py").read())
elif choice == 4:
    subprocess.call('killall firefox',shell=True)
    exec(open("./sub_menu.py").read())
elif choice == 5:
    exec(open("./rom.py").read())
elif choice ==6:
    print("exit")
    subprocess.call('clear',shell=True)
else:
    print("what you doing man :-) ")