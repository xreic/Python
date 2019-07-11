#! python3

import os, requests, json

os.chdir(r'D:\Users\Amadeus\Desktop\Good\Testing')

charName = input("Enter character name: ")


## Get account name from one character.
print("Searching for account name...")
print()

reqLink = "https://api.poe.watch/accounts?character=" + charName
reqChr2Acc = requests.get(reqLink)

strChr2Acc = reqChr2Acc.text[1:-1]
dictChr2Acc = json.loads(strChr2Acc)

print("Account name found!")
print()


## Get characters from account name.
print("Searching for (all) characters in specified account...")
print()

reqLink = "https://api.poe.watch/characters?account=" + dictChr2Acc['account']
reqAcc2Chrs = requests.get(reqLink)

listAcc2Chrs = reqAcc2Chrs.text.split('},{')
dictListA2C = []
listChars = []

for i in range(len(listAcc2Chrs)):
    if i == 0:
        listAcc2Chrs[i] = listAcc2Chrs[i][1:] + "}"
    elif i == len(listAcc2Chrs) - 1:
        listAcc2Chrs[i] = "{" + listAcc2Chrs[i][:-1]
    else:
        listAcc2Chrs[i] = "{" + listAcc2Chrs[i] + "}"

for i in range(len(listAcc2Chrs)):
    dictListA2C.append(json.loads(listAcc2Chrs[i]))

print('All characters logged into after the creation of PoE Watch API')

for i in range(len(dictListA2C)):
    print('        ' + dictListA2C[i]['character'])    
    listChars.append(dictListA2C[i]['character'])


## Write data to file.
print("Writing data to file...")
print()

with open('Find Characters Function (Non-Function).txt', 'w', encoding='utf-8') as f:
    for item in listChars:
        f.write("%s\n" % item)

print("Writing complete.")
print("Exiting program.")
