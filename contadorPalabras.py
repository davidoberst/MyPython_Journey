#Contar cuantas veces aparece una palabra en un texto

def wordCount(text):
    words = text.split()
    countWords = {}
    for x in words:
        if x in countWords:
            countWords[x] += 1
        else:
            countWords[x] = 1
    print(countWords)

wordCount("hey muy buenas chavales muy buenas")
