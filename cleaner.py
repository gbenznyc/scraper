import csv

namesWithEmails = []

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
        # print(name, " ", dicts['email'])
        namesWithEmails.append(name)
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
            # print(nameLast, " ", wordsInName[j-1], " ", dicts['email'], dicts['info'])
            namesWithEmails.append(nameLast.lower())
            namesWithEmails.append(wordsInName[j-1].lower())
        if j<len(wordsInName)-1:
          if firstLetter == wordsInName[j+1][0]:
            # print(nameLast, " ", wordsInName[j+1], " ", dicts['email'], dicts['info'])
            namesWithEmails.append(nameLast.lower())
            namesWithEmails.append(wordsInName[j+1].lower())

      if nameFirst == wordsInName[j]:
        if j>=1:
          if lastLetter == wordsInName[j-1][0]:
            # print(nameFirst, " ", wordsInName[j-1], " ", dicts['email'], dicts['info'])
            namesWithEmails.append(nameFirst.lower())
            namesWithEmails.append(wordsInName[j-1].lower())
        if j<len(wordsInName)-1:
          if lastLetter == wordsInName[j+1][0]:
            # print(nameFirst, " ", wordsInName[j+1], " ", dicts['email'], dicts['info'])
            namesWithEmails.append(nameFirst.lower())
            namesWithEmails.append(wordsInName[j+1].lower())
  return clean_list



def splitNameFinder(dict_list):
  nameCountNumber=0
  clean_list = []
  # splitChar = "."
  for dicts in dict_list:
    #print(dicts)
    name = dicts['email'].split("@")[0]
    name=name.translate(str.maketrans(dict.fromkeys('0123456789.-_+,')))#removes all numbers
    name=name.lower()



    wordsInName = dicts['info'].lower().split()

    for i in range(len(name)):
      splitName1=name[0:i+1]
      splitName2=name[i+1:len(name)]
      # print(splitName1, " ", splitName2)
      testName = ""
      for i in range(len(wordsInName)):
        if(splitName1==wordsInName[i]):
          if checkValidName(splitName1)==True:
            sideName = getSideName(wordsInName, splitName1, splitName2)
            if len(sideName)>0:
               if checkValidName(sideName)==True:
                 nameCountNumber = nameCountNumber+1
                #  print(splitName1, " ", sideName, " ", dicts['email'])
        if(splitName2==wordsInName[i]):
          if checkValidName(splitName2)==True:
            sideName = getSideName(wordsInName, splitName2, splitName1)
            if len(sideName)>0:
               if checkValidName(sideName)==True:
                 nameCountNumber = nameCountNumber+1
                #  print(splitName2, " ", sideName, " ", dicts['email'])
# startswith for main name
  return nameCountNumber
    
    


def checkValidName(theName):
  validName = False
  for p in range(len(array)):
    if theName==array[p]:
      validName = True
  if validName == True:
    # print(theName)
    return True
  return False

def getSideName(wordsInName,  name, sideName):
  for j in range(len(wordsInName)):
    if name == wordsInName[j]:
          if j>=1:
            if wordsInName[j-1].startswith(sideName):
              return wordsInName[j-1]
          if j<len(wordsInName)-1:
            if wordsInName[j+1].startswith(sideName):
              return wordsInName[j-1]
  return ""






	
def main():
	CSVDict = CSVReader('heads.csv')
	# print(len(CSVDict))
	
	CSVDict = noEmails(CSVDict)
	# print(len(CSVDict))
	
	# CSVDict = keywordMatcher(CSVDict, ['Chair'])
	# print(len(CSVDict))
	CSVDict = removeDuplicates(CSVDict)
	print(len(CSVDict))

	# nameInEmailWithSplitChar(CSVDict, ".")
	# nameInEmailWithSplitChar(CSVDict, print"-")
	# nameInEmailWithSplitChar(CSVDict, "_")
	# nameInEmailSingleCharAndName(CSVDict)

	


	# for i in range(len(namesWithEmails)):
	# 	validName = False
	# 	for j in range(len(array)):
	# 		if namesWithEmails[i]==array[j]:
	# 			validName = True
	# 	if validName == True:
	# 		print(namesWithEmails[i])
	print(splitNameFinder(CSVDict))
	


array = []
with open("names.txt", "r") as ins:
  for line in ins:
    array.append(line.lower())
for i in range(len(array)):
  array[i] = array[i].strip('\n')

main()



