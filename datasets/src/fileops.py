import json
import os
paths={
'ACCURACY_TEST_DIR':'/home/js/Documents/comp/emel/parkingLotCounter/classifiers/test/accuracy_tests/'
}



def wfile(data, filename):

	with open(str(filename), "w") as outfile:
		try:
			json.dump(data, outfile)
		except:
			raise
			print ("\nErro de abertura do ficheiro: ",str(filename)," !")


def afile(data, filename):
    
	with open(str(filename), "a") as outfile:
		try:
			json.dump(data, outfile)
		except:
			raise
			print ("\nErro de abertura do ficheiro: ",str(filename)," !")


def aafile (data,fname):
	a = []
	if not os.path.isfile(fname):
		a.append(data)
		with open(fname, mode='w') as f:
			f.write(json.dumps([data], indent=2))
	else:
		with open(fname) as feedsjson:
			feeds = json.load(feedsjson)

		feeds.append(data)
		with open(fname, mode='w') as f:
			f.write(json.dumps(feeds, indent=2))


def rfile(filename):

	with open(str(filename)) as infile:
		try:
			data = json.load(infile)
			return data
		except:
			print ("\nErro de leitura do ficheiro: ",str(filename)," !")
			return 0
