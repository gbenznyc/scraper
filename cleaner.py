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

def removeDuplicates(dict_list):
	clean_list = []
	info_list = []
	for dicts in dict_list:
		info_list.append(dicts['info'])
	info_list = list(set(info_list))
	#print(len(info_list))
	for infos in info_list:
		for dicts in dict_list:
			if infos == dicts['info']:
				clean_list.append(dicts)
				break
	return clean_list

	
def main():
	CSVDict = CSVReader('heads.csv')
	print(len(CSVDict))
	
	# CSVDict = noEmails(CSVDict)
	# print(len(CSVDict))
	
	# CSVDict = keywordMatcher(CSVDict, ['Chair'])
	# print(len(CSVDict))

	CSVDict = removeDuplicates(CSVDict)
	print(CSVDict)

main()