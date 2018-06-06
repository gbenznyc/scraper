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









	def nameInEmailWithSplitChar(dict_list, splitChar):
  clean_list = []
  # splitChar = "."
  for dicts in dict_list:
		#print(dicts)
    if dicts['email'].split("@")[0].find(splitChar) > -1:
      # name = dicts['email'].split("@")[0].lower().split(splitChar)
      # wordsInName = re.findall(r"[\w']+", dicts['info'].lower())

      name = dicts['email'].split("@")[0]
      name=name.translate(str.maketrans(dict.fromkeys(',')))
      name=name.lower()
      name=name.split(splitChar)
      wordsInName = dicts['info'].lower().split()
      
      nameCount = 0;
      for i in range(len(name)):   
        for j in range(len(wordsInName)):
          if name[i] == wordsInName[j]:
            nameCount = nameCount+1
            j =len(wordsInName)+10
      if nameCount >= len(name):
        clean_list.append(dicts)
        print(name, " ", dicts['email'])
  return clean_list


def nameInEmailSingleCharAndName(dict_list):
  clean_list = []
  # splitChar = "."
  for dicts in dict_list:
    #print(dicts)
    name = dicts['email'].split("@")[0]
    name=name.translate(str.maketrans(dict.fromkeys('0123456789.-_+,')))#removes all numbers
    name=name.lower()
    lastLetter=name[len(name)-1]
    firstLetter=name[0]
    nameFirst=name[0:len(name)-1]
    nameLast=name[1:len(name)]
    
    # wordsInName = re.findall(r"[\w']+", dicts['info'].lower())
    wordsInName = dicts['info'].lower().split()


    for j in range(len(wordsInName)):
      if nameLast == wordsInName[j]:
        if j>=1:
          if firstLetter == wordsInName[j-1][0]:
            print(nameLast, " ", wordsInName[j-1], " ", dicts['email'], dicts['info'])
        if j<len(wordsInName)-1:
          if firstLetter == wordsInName[j+1][0]:
            print(nameLast, " ", wordsInName[j+1], " ", dicts['email'], dicts['info'])

      if nameFirst == wordsInName[j]:
        if j>=1:
          if lastLetter == wordsInName[j-1][0]:
            print(nameFirst, " ", wordsInName[j-1], " ", dicts['email'], dicts['info'])
        if j<len(wordsInName)-1:
          if lastLetter == wordsInName[j+1][0]:
            print(nameFirst, " ", wordsInName[j+1], " ", dicts['email'], dicts['info'])
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