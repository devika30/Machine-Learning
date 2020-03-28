import pickle as p
import os
from sklearn import *
from collections import Counter

import pickle 
def load(clf_file):
    with open(clf_file,"rb") as fp:
        clf = p.load(fp)
    return clf



def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)

    for email in emails:
        f = open(email,"r",encoding="utf8", errors='ignore')
        blob = f.read()
        # print(type(blob))
        
        words += blob.split()


    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)


clf = load("text-classifier.mdl")
print("model loaded")
d = make_dict()

def predict_with_text(text):
    print("============================")
    print(text)
    print("============================")
    features = []
    inp = text.split()
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    resdir = {"0":"Ham","1":"Spam"}
    print(res)
    print(resdir.get(str(res[0])))

while True:
    inp = input(">").split()
    if inp[0] == "exit":
        clf.close()
        break
    with open(inp[0],"r") as inputfile:
        data = inputfile.read()
        predict_with_text(data)
        
        
#File to checked as spam/ham should be in file.txt format and provide the path after model loads 
