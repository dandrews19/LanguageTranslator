# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Assignment 9
# Description:
# This program translates wors from one language to another using a spreadsheet with translations and creates
# a file with the results


# creates a list of languages user is able to translate to
def getLanguages(fileName = "languages.csv"):
    fileIn = open(fileName, "r")
    languageString = fileIn.readline()
    languageList = languageString.strip().lower().split(",")
    fileIn.close()

    return languageList

# gets the language the user wants to translate from English to
def getSecondLanguage(langlist):
    print("Language Translator\nTranslate English words to one of the following languages:\n"
          "\tDanish Dutch Finnish French German Indonesian Italian\n "
          "\tJapanese Latin Norwegian Portuguese Spanish Swahili Swedish")
    userLanguage = input("Enter a language: ")
    userLanguage = userLanguage.strip().lower()
    while userLanguage not in langlist:
        print("This program does not support", userLanguage)
        userLanguage = input("Enter a language: ")
        userLanguage = userLanguage.strip().lower()


    return userLanguage


# creates a list of the words in the language specified by the user
def readFile(langList, langStr = "english", fileName = "languages.csv"):
    fileIn = open(fileName, "r")
    header = fileIn.readline()
    index = langList.index(langStr)
    foreignWordsList = []
    for line in fileIn:
        newLine = line.strip().split(",")
        foreignWordsList.append(newLine[index])
    fileIn.close()

    return foreignWordsList

# creates a results file where all the translations are put
def createResultsFile(language, resultsFile):
    language = language.capitalize()
    fileOut = open(resultsFile + ".txt", "w")
    print("Words translated from English to", language, file=fileOut)
    fileOut.close()


# prompts user for word to translate, continues to do so until user wants it to stop, and adds translations to
# a separate text file
def translateWords(englishList, secondList, resultsFile):
    fileOut = open(resultsFile + ".txt", "a")
    cont = "y"
    while cont == "Y" or cont == "y":
        word = input("Enter a word to translate: ")
        word = word.lower().strip()
        if word not in englishList:
            print(word, "is not in the English list")
        if word in englishList:
            translated = secondList[englishList.index(word)]
            if translated == "-":
                print(word, "did not have a translation")
            else:
                print(word, "is translated to", translated)
                print(word + " = " + translated, file=fileOut)
        cont = input("Another word (y or n)? ")
        while cont != "Y" and cont != "y" and cont != "N" and cont != "n":
            cont = input("Another word (y or n)? ")
    fileOut.close()
    print("Translated words have been saved to "+ resultsFile + ".txt")


# calls appropriate functions, asks user for file name,
def main():
    langList = getLanguages()
    userLanguage = getSecondLanguage(langList)
    words = readFile(langList=langList, langStr=userLanguage)
    englishList = readFile(langList)
    userLanguage = userLanguage.capitalize()
    resultsFile = input("Enter a name for the results file (return key for " + userLanguage + ".txt): ")
    resultsFile = resultsFile.strip()
    if resultsFile == "":
        resultsFile = userLanguage
    createResultsFile(userLanguage, resultsFile)
    translateWords(englishList, words, resultsFile)


main()