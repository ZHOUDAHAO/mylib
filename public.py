from datetime import date,timedelta
import shutil
import os,gzip
import urllib2
import io
import sys,random,string

date_num = lambda x:x.isoformat().replace('-','')
num_date = lambda x:date(int(x[0:4]),int(x[4:6]),int(x[6:8]))

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def change_encoding(file1,file2,encoding1,encoding2):
	try:
		with io.open(file1,'r+',encoding = encoding1) as f:
			data = f.read()
			with io.open(file2,'w',encoding = encoding2) as w:
				w.write(data)
	except UnicodeDecodeError:
		pass
	else:
		try:
			os.rename(file2,file1)
		except OSError:
			os.remove(file1)
			os.rename(file2,file1)

def change_all_encoding(path,encoding1,encoding2):
	for f in os.listdir(path):
		fname = os.path.join(path,f)
		change_encoding(fname,'dummy',encoding1,encoding2)

def safe_make_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def abs_path(name):
	Dir = os.path.dirname(os.path.abspath(__file__))
	return os.path.join(Dir,name)

'''generate random length string
mode = 0:lowercase only
mode = 1:lowercase & uppercase
mode = 2:lowercase & uppercase & digits'''

def random_string(length,mode = 0):
	if mode == 0:
		return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
	elif mode == 1:
		return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(length))
	elif mode == 2:
		return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))
	else:
		raise Exception("Wrong mode number " + mode)

def print_rand_str():
	length = int(sys.argv[1])
	mode = int(sys.argv[2])
	print(random_string(length,mode))

def iter_file(root,func):
	for node in os.listdir(root):
		node_path = os.path.join(root,node)
		if os.path.isdir(node_path):
			iter_file(node_path,func)
		else:
			func(node_path)

def check_size(data,value):
	if len(data) >= value:
		return True
	else:
		 return False

def gzip_replace(filepath):
	if filepath.endswith('.gz'):
		return
	with open(filepath,'rb') as f_in:
		with gzip.open(filepath + '.gz','wb') as f_out:
			shutil.copyfileobj(f_in,f_out)
	os.remove(filepath)
