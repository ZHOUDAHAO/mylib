import subprocess
subprocess.run('g++ --std=c++14 main.cpp -o main -lgtest -pthread',stdout=subprocess.PIPE,shell=True)
proc = subprocess.run('./main',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
out = proc.stdout.decode('utf-8').strip()
if out.find('FAILED')!=-1:
	print('C++ module tests FAILED!!!')
