import subprocess


subprocess.call('g++ simple.cpp', shell=True)
output = subprocess.check_output('a.exe',shell = True)
s = output.decode()
f = open('puri.txt','w')

f.write(s)
f.close()








