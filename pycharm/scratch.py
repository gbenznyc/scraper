import csv

namesWithEmails = []


def noEmails(dict_list):
    clean_list = []
    for dicts in dict_list:
        # print(dicts)
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
    reader = csv.DictReader(open(path, encoding="utf8"))
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
    # print(len(info_list))
    for infos in info_list:
        for dicts in dict_list:
            if infos == dicts['info']:
                clean_list.append(dicts)
                break
    return clean_list


def newRemoveDuplicates(dict_list):
    clean_list = []
    for i in range(len(dict_list)):
        addIt = True
        for j in range(i + 1, len(dict_list)):
            if dict_list[i]['info'] == dict_list[j]['info']:
                if dict_list[i]['email'] == dict_list[j]['email']:
                    addIt = False
                    j = len(dict_list) + 10

        if (addIt == True):
            clean_list.append(dict_list[i])
            # print(dict_list[i])
    return clean_list

def newRemoveDuplicatesSameEmail(dict_list):
    clean_list = []
    for i in range(len(dict_list)):
        addIt = True
        for j in range(i + 1, len(dict_list)):
            # if dict_list[i]['info'] == dict_list[j]['info']:
                if dict_list[i]['email'] == dict_list[j]['email']:
                    addIt = False
                    j = len(dict_list) + 10

        if (addIt == True):
            clean_list.append(dict_list[i])
            # print(dict_list[i])
    return clean_list


def nameInEmailWithSplitChar(dict_list, splitChar):
    clean_list = []
    # splitChar = "."
    for dicts in dict_list:
        # print(dicts)
        if dicts['email'].split("@")[0].find(splitChar) > -1:
            # name = dicts['email'].split("@")[0].lower().split(splitChar)
            # wordsInName = re.findall(r"[\w']+", dicts['info'].lower())

            name = dicts['email'].split("@")[0]
            name = name.translate(str.maketrans(dict.fromkeys(',')))
            name = name.lower()
            name = name.split(splitChar)
            wordsInName = dicts['info'].lower().split()

            nameCount = 0;
            for i in range(len(name)):
                for j in range(len(wordsInName)):
                    if name[i] == wordsInName[j]:
                        nameCount = nameCount + 1
                        j = len(wordsInName) + 10
            if nameCount >= len(name):
                clean_list.append(dicts)
                # print(name, " ", dicts['email'])
                namesWithEmails.append(name)
    return clean_list


def nameInEmailSingleCharAndName(dict_list):
    clean_list = []
    # splitChar = "."
    for dicts in dict_list:
        # print(dicts)
        name = dicts['email'].split("@")[0]
        name = name.translate(str.maketrans(dict.fromkeys('0123456789.-_+,')))  # removes all numbers
        name = name.lower()
        lastLetter = name[len(name) - 1]
        firstLetter = name[0]
        nameFirst = name[0:len(name) - 1]
        nameLast = name[1:len(name)]

        # wordsInName = re.findall(r"[\w']+", dicts['info'].lower())
        wordsInName = dicts['info'].lower().split()

        for j in range(len(wordsInName)):
            if nameLast == wordsInName[j]:
                if j >= 1:
                    if firstLetter == wordsInName[j - 1][0]:
                        # print(nameLast, " ", wordsInName[j-1], " ", dicts['email'], dicts['info'])
                        namesWithEmails.append(nameLast.lower())
                        namesWithEmails.append(wordsInName[j - 1].lower())
                if j < len(wordsInName) - 1:
                    if firstLetter == wordsInName[j + 1][0]:
                        # print(nameLast, " ", wordsInName[j+1], " ", dicts['email'], dicts['info'])
                        namesWithEmails.append(nameLast.lower())
                        namesWithEmails.append(wordsInName[j + 1].lower())

            if nameFirst == wordsInName[j]:
                if j >= 1:
                    if lastLetter == wordsInName[j - 1][0]:
                        # print(nameFirst, " ", wordsInName[j-1], " ", dicts['email'], dicts['info'])
                        namesWithEmails.append(nameFirst.lower())
                        namesWithEmails.append(wordsInName[j - 1].lower())
                if j < len(wordsInName) - 1:
                    if lastLetter == wordsInName[j + 1][0]:
                        # print(nameFirst, " ", wordsInName[j+1], " ", dicts['email'], dicts['info'])
                        namesWithEmails.append(nameFirst.lower())
                        namesWithEmails.append(wordsInName[j + 1].lower())
    return clean_list


def splitNameFinder(dict_list):
    nameCountNumber = 0
    # splitChar = "."
    for dicts in dict_list:
        # print(dicts)
        name = dicts['email'].split("@")[0]
        name = name.translate(str.maketrans(dict.fromkeys('0123456789.-_+,')))  # removes all numbers
        name = name.lower()

        wordsInName = dicts['info'].lower().split()

        for i in range(len(name)):
            splitName1 = name[0:i + 1]
            splitName2 = name[i + 1:len(name)]
            # print(splitName1, " ", splitName2)
            for i in range(len(wordsInName)):
                if (splitName1 == wordsInName[i]):
                    sideName = getSideName(wordsInName, wordsInName[i], splitName2)
                    if len(sideName) > 0:
                        if checkValidName(wordsInName[i]) == True:
                            # if checkValidName(sideName)==True:
                            nameCountNumber = nameCountNumber + 1
                            print(wordsInName[i], " ", sideName, " ", dicts['email'])
                if (splitName2 == wordsInName[i]):
                    sideName = getSideName(wordsInName, wordsInName[i], splitName1)
                    if len(sideName) > 0:
                        if checkValidName(wordsInName[i]) == True:
                            # if checkValidName(sideName)==True:
                            nameCountNumber = nameCountNumber + 1
                            print(wordsInName[i], " ", sideName, " ", dicts['email'])
    # startswith for main name
    return nameCountNumber


def newSplitNameFinder(dict_list):
    emailWithNames=[]

    nameCountNumber = 0
    for dicts in dict_list:
        name = dicts['email'].split("@")[0]
        name = name.translate(str.maketrans(dict.fromkeys('0123456789.-_+,')))  # removes all numbers
        name = name.lower()

        wordsInName = dicts['info'].lower().split()
        for i in range(len(name)):
            splitName1 = name[0:i + 1]
            splitName2 = name[i + 1:len(name)]
            for i in range(len(wordsInName)):
                if wordsInName[i].startswith(splitName1):
                    if checkValidName(wordsInName[i]) == True:
                        sideName = getSideNameNew(wordsInName, i, splitName2)
                        if len(sideName) > 0:
                            # if checkValidName(sideName)==True:
                            nameCountNumber = nameCountNumber + 1
                            tempArray = []
                            print(dicts['email'], " ", wordsInName[i], " ", sideName, " ")
                            tempArray.append(dicts['email'])
                            tempArray.append(wordsInName[i])
                            tempArray.append(sideName)
                            emailWithNames.append(tempArray)
    print(nameCountNumber)
    return emailWithNames


def splitNameFinderStartsWith(dict_list):
    nameCountNumber = 0
    # splitChar = "."
    for dicts in dict_list:
        # print(dicts)
        name = dicts['email'].split("@")[0]
        name = name.translate(str.maketrans(dict.fromkeys('0123456789.-_+,')))  # removes all numbers
        name = name.lower()

        wordsInName = dicts['info'].lower().split()

        for i in range(len(name)):
            splitName1 = name[0:i + 1]
            splitName2 = name[i + 1:len(name)]
            # print(splitName1, " ", splitName2)
            for i in range(len(wordsInName)):
                if (wordsInName[i].startswith(splitName1)):
                    sideName = getSideName(wordsInName, splitName1, splitName2)
                    # if len(sideName)>0:
                    if checkValidName(wordsInName[i]) == True:
                        # if checkValidName(sideName)==True:
                        nameCountNumber = nameCountNumber + 1
                        print(wordsInName[i], " ", sideName, " ", dicts['email'])
                if (wordsInName[i].startswith(splitName2)):
                    sideName = getSideName(wordsInName, splitName2, splitName1)
                    # if len(sideName)>0:
                    if checkValidName(wordsInName[i]) == True:
                        # if checkValidName(sideName)==True:
                        nameCountNumber = nameCountNumber + 1
                        print(wordsInName[i], " ", sideName, " ", dicts['email'])
    # startswith for main name
    # single names dont work
    # if email is in info it dupilcates
    # needs to remove slashes
    # solar   uc   rwinston@ucmerced.edu
    # ruh   adam   aruh@vwu.edu
    # english   in   aruh@vwu.edu
    return nameCountNumber


def checkValidName(theName):
    validName = False
    if len(theName) > 0:
        for p in range(len(array)):
            if theName == array[p]:
                validName = True
        if validName == True:
            # print(theName)
            return True
    return False

def getSideNameNew(wordsInName, spot, sideName):
            if spot >= 1:
                if wordsInName[spot - 1].startswith(sideName):
                    if len(wordsInName[spot - 1]) > 0:
                        if checkValidName(wordsInName[spot - 1]) == True:
                            return wordsInName[spot - 1]
            if spot < len(wordsInName) - 1:
                if wordsInName[spot + 1].startswith(sideName):
                    if len(wordsInName[spot + 1]) > 0:
                        if checkValidName(wordsInName[spot + 1]) == True:
                            return wordsInName[spot + 1]
            return ""



def getSideName(wordsInName, name, sideName):
    for j in range(len(wordsInName)):
        if wordsInName[j].startswith(name):
            if j >= 1:
                if wordsInName[j - 1].startswith(sideName):
                    if len(wordsInName[j - 1]) > 0:
                        if checkValidName(wordsInName[j - 1]) == True:
                            return wordsInName[j - 1]
            if j < len(wordsInName) - 1:
                if wordsInName[j + 1].startswith(sideName):
                    if len(wordsInName[j + 1]) > 0:
                        if checkValidName(wordsInName[j + 1]) == True:
                            return wordsInName[j + 1]
    return ""


def main():
    CSVDict = CSVReader('heads.csv')
    # print(len(CSVDict))

    CSVDict = noEmails(CSVDict)
    # print(len(CSVDict))

    # CSVDict = keywordMatcher(CSVDict, ['Chair'])
    # print(len(CSVDict))
    CSVDict = newRemoveDuplicatesSameEmail(CSVDict)
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

    # print(splitNameFinder(CSVDict))
    # print(splitNameFinderStartsWith(CSVDict))
    emailsNames = newSplitNameFinder(CSVDict)

    # print(newSplitNameFinder(CSVDict))

    myFile = open('emailandnames.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(emailsNames)

    print("Writing complete")


array = []
with open("names.txt", "r") as ins:
    for line in ins:
        array.append(line.lower())
for l in range(len(array)):
    array[l] = array[l].strip('\n')

main()


