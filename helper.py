def stopWordsGetter():
    stopwords = set()
    with open("stopwords.txt","r") as file:
        content = file.readlines()
        for word in content:
            stopwords.add(word.replace("\n",""))
    return stopwords