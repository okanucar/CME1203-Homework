import requests
import operator
from bs4 import BeautifulSoup


# I wrote and applied the functions
def create_dictionary(allwords):
    word_count = {}

    for word in allwords:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def create_dictionary1(allwords1):
    word_count1 = {}

    for word in allwords1:
        if word in word_count1:
            word_count1[word] += 1
        else:
            word_count1[word] = 1

    return word_count1


def clean(allwords):
    cleared_words = []
    symbols =  "0123456789!:'^+%&/()=?_-*|\}][{½$#£\"><@.,;’"
    for word in allwords:
        for symbol in symbols:
            if symbol in word:
                word = word.replace(symbol, "")

        if(len(word) > 1):
            cleared_words.append(word)
    return cleared_words


# I tried to remove unnecessary words

def clean2(allwords):
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    cleared_words2 = []

    for word in allwords:
        for stop in stop_words:
            if (stop == word):
                word = word.replace(stop, "")
        if(len(word) > 0):
            cleared_words2.append(word)

    return cleared_words2

# I assigned the links of the sites to the url variable
user_url = str(input("Please Enter Book1 Name (Please Substitute '_' For Spaces) :"))
c = str(input("Do you want to enter word number? Please press ('Y'(Yes) or 'N'(No)) :"))
if (c =="Y" or c == "y") :
    a = int(input("Please enter how many words would you like to print for Book1 :"))
url = "https://en.wikibooks.org/wiki/" + user_url + "/Print_version"

user_url1 = str(input("Please Enter Book2 Name (Please Substitute '_' For Spaces) :"))
d = str(input("Do you want to enter word number? Please press ('Y'(Yes) or 'N'(No)) :"))
if (d =="Y" or d == "y") :
    b = int(input("Please enter how many words would you like to print for Book2 :"))
url1 = "https://en.wikibooks.org/wiki/" + user_url1 + "/Print_version"

# I defined a list
allwords = []
allwords1 = []

# I got and edit the url using "request" and "beautiful soup"
r = requests.get(url)
r1 = requests.get(url1)

soup = BeautifulSoup(r.content,"html.parser")
soup1 = BeautifulSoup(r1.content,"html.parser")

# I got the words from "body"
for wordgroups in soup.find_all("body"):
    content = wordgroups.text
    words = content.lower().split()

    for word in words:
         allwords.append(word)

for wordgroups1 in soup1.find_all("body"):
    content1 = wordgroups1.text
    words1 = content1.lower().split()

    for word1 in words1:
         allwords1.append(word1)

# I defined a lists
allwords = clean(allwords)
allwords = clean2(allwords)
word_count = create_dictionary(allwords)

allwords1 = clean(allwords1)
allwords1 = clean2(allwords1)
word_count1 = create_dictionary1(allwords1)

x = 0
y = 0

result = []
result1 = []

resultcal = []
resultcal1 = []


# I assigned the words to the list one by one
for specialkey,value in sorted(word_count.items(), key = operator.itemgetter(1), reverse =True):
    result.append(specialkey)
    resultcal.append(value)

for specialkey1,value1 in sorted(word_count1.items(),key = operator.itemgetter(1), reverse=True):
    result1.append(specialkey1)
    resultcal1.append(value1)

# I opened a file
file = open("book1.txt", "w", encoding="utf-8")
file.close()

file1 = open("book2.txt", "w", encoding="utf-8")
file1.close()

# I printed the "book1"
print("FREQ_1")
print("------")
for specialkey,value in sorted(word_count.items(), key = operator.itemgetter(1), reverse =True):
    if (c =="Y" or c == "y") :
        if(a == x ):
            break
        else:
            x += 1
            print(str(x) + ') ' + specialkey, value)
            file = open("book1.txt", "a", encoding="utf-8")
            file.write(str(x) + ') ' + specialkey + "      ")
            file.write(str(value) + "\n")
    else:
        if(x == 20):
            break
        else:
            x += 1
            print(str(x) + ') ' + specialkey, value)
            file = open("book1.txt", "a", encoding="utf-8")
            file.write(str(x) + ') ' + specialkey + "      ")
            file.write(str(value) + "\n")

# I printed the "book2"
print("|||||||||||||||***************************************************||||||||||||||")
print("FREQ_2")
print("------")
for specialkey1,value1 in sorted(word_count1.items(),key = operator.itemgetter(1), reverse=True):
    if (d == "Y" or d == "y"):
        if (b == y):
            break
        else:
            y += 1
            print(str(y) + ') ' + specialkey1, value1)
            file1 = open("book2.txt", "a", encoding="utf-8")
            file1.write(str(y) + ') ' + specialkey1 + "      ")
            file1.write(str(value1) + "\n")

    else:
        if (y == 20):
            break
        else:
            y += 1
            print(str(y) + ') ' + specialkey1, value1)
            file1 = open("book2.txt", "a", encoding="utf-8")
            file1.write(str(y) + ') ' + specialkey1 + "      ")
            file1.write(str(value1) + "\n")


# I summed up the common words of "book1" and "book2"
m = 0
k = 0
print("|||||||||||||||***************************************************||||||||||||||")
print("COMMON WORDS")
print("------------")
print("NO WORD" + "     " + "FREQ_1" + "   " + "FREQ_2" + "   " + "FREQ_SUM")
for i in result:
    k += 1
    if i in result1:
        t = result1.index(i)
        if (d == "Y" or d == "y"):
            if (b == m):
                break
            else:
                m += 1
                print(str(m) + ') ' + result[k - 1] + "      |" + str(resultcal[k - 1]) + "|     |" + str(resultcal1[t]) + "|      |" + str(resultcal[k - 1] + resultcal1[t]) + "|")
        else:
            if (m == 20):
                break
            else:
                m += 1
                print(str(m) + ') ' + result[k - 1] + "      |" + str(resultcal[k - 1]) + "|     |" + str(resultcal1[t]) + "|      |" + str(
                    resultcal[k - 1] + resultcal1[t]) + "|")


# Words that are in "book1" but not in "book2"
print("|||||||||||||||***************************************************||||||||||||||")
print("DISTINCT WORDS: FREQ_1")
print("----------------------")
m = 0
z = 0
for i in result:
    z += 1
    if i in result1:
        continue
    else:
        if (d == "Y" or d == "y"):
            if (b == m):
                break
            else:
                m += 1
                print(str(m) + ') ' + result[z - 1] + "        " + "|" + str(resultcal[z-1]) + "|")
        else:
            if (m == 20):
                break
            else:
                m += 1
                print(str(m) + ') ' + result[z - 1] + "        " + "|" + str(resultcal[z - 1]) + "|")


# Words that are in "book2" but not in "book1"
print("|||||||||||||||***************************************************||||||||||||||")
print("DISTINCT WORDS: FREQ_2")
print("----------------------")
m = 0
h = 0
for i in result1:
    h += 1
    if i in result:
        continue
    else:
        if (d == "Y" or d == "y"):
            if (b == m):
                break
            else:
                m += 1
                print(str(m) + ') ' + result1[h - 1] + "        " + "|" + str(resultcal1[h - 1]) + "|")
        else:
            if (m == 20):
                break
            else:
                m += 1
                print(str(m) + ') ' + result1[h - 1] + "        " + "|" + str(resultcal1[h - 1]) + "|")











