import numpy,scipy,sklearn,blosc,pandas,matplotlib
import iotop

def python_modules():
	A = numpy.array([[1,1],[0,1]])
	B = numpy.array([[2,0],[3,4]])
	C = numpy.dot(A,B)
	
	flag = numpy.array_equal(C,[[5,4],[3,4]])
	if flag==False:
		print('numpy failed')

	D = scipy.linalg.inv(A)
	flag = numpy.array_equal(D,[[1,-1],[0,1]])
	if flag==False:
		print('scipy failed')
	
	print("matplotlib:"+matplotlib.__file__)
	
	names = ['Bob','Jessica','Mary','John','Mel']
	births = [968, 155, 77, 578, 973]
	BabyDataSet = list(zip(names,births))
	df = pandas.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
	
	if df['Births'].max()!=973:
		print('pandas failed')

	input_bytes = b"abcdefghijklmnopqrstuvwxyz"
	zipstr = blosc.compress(input_bytes,typesize=1)
	if input_bytes != blosc.decompress(zipstr):
		print('blosc failed')

	print("sklearn:"+sklearn.__file__)

python_modules()
