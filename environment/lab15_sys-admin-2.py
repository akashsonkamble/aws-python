import os
import subprocess

os.system("ls") #Exercise 1: Using os.system

#Exercise 2: Using subprocess.run
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
subprocess.run(["ls"]) 
subprocess.run(["ls","-l"]) #Exercise 3: Using subprocess.run with two arguments
subprocess.run(["ls","-l","README.md"]) #Exercise 4: Using subprocess.run with three arguments

# Exercise 5: Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Exercise 6: Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])