import json

paths={
'ACCURACY_TEST_DIR':'/home/js/Documents/comp/emel/parkingLotCounter/classifiers/test/accuracy_tests'
}



def wfile(data, filename):

	with open(str(filename), "w") as outfile:
		try:
			json.dump(data, outfile)
		except:
			raise
			print ("\nErro de abertura do ficheiro: ",str(filename)," !")



def rfile(filename):

	with open(str(filename)) as infile:
		try:
			data = json.load(infile)
			return data
		except:
			print ("\nErro de leitura do ficheiro: ",str(filename)," !")
			return 0
