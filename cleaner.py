import csv

def noEmails(dict_list):
	clean_list = []
	for dicts in dict_list:
		#print(dicts)
		if not dicts['email'] == 'No email element':
			clean_list.append(dicts)
	return clean_list

def keywordMatcher(dict_list, keywords):
	clean_list = []
	for dicts in dict_list:
		for words in keywords:
			if words in dicts['info']:
				clean_list.append(dicts)
	return clean_list

def CSVReader(path):
	reader = csv.DictReader(open(path))
	dict_list = []
	for row in reader:
		dict_list.append(row)
	return dict_list

def main():
	CSVDict = CSVReader('heads.csv')
	print(len(CSVDict))
	
	CSVDict = noEmails(CSVDict)
	print(len(CSVDict))
	
	CSVDict = keywordMatcher(CSVDict, ['Chair'])
	print(len(CSVDict))

	#print(CSVDict)

main()