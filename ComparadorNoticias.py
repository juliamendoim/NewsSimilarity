import nltk
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer

stop = set(stopwords.words('spanish'))
tokenizer = RegexpTokenizer(r'\w+')
Funciones

def Enlistador(nota):
    lista = []
    with codecs.open(nota,'r', encoding = 'utf-8', errors = 'ignore') as text:
        news1= text.read()
        token = tokenizer.tokenize(news1)
        for i in token:
            if i not in stop:
                lista.append(i)
    return lista
​
def LeeNoticia(nota):
    lista = []
    with open(nota, encoding = 'utf-8', errors = 'ignore' ) as f:
        for line in f:
            line = line.strip()
            lista.append(line)
    return lista
​
def cosine_sim(lista,vectorizer):
    tfidf = vectorizer.fit_transform(lista) # devuelve una matriz sparse, y una lista 
    return ((tfidf * tfidf.T).A)
​
def TresParrafos(nota, N):
    parrafos = []
    nota1 = LeeNoticia(nota)
    j = 0
    i = 1
    while i<(N+1)+j:
        if nota1[i] != '':
            parrafos.append(nota1[i])
            i += 1
        else: 
            j += 1
            i += 1
    return parrafos
​

keywords = []
​
keywords.append(Enlistador('cnn.txt'))
keywords.append(Enlistador('euronews.txt'))         
keywords.append(Enlistador('ElPais.txt'))
keywords.append(Enlistador('bbcTaiwan.txt'))
keywords.append(Enlistador('bbcCoreaviejo.txt'))
for j in range(len(keywords)):
    aux = ' '.join(keywords[j])
    keywords[j] = aux
    
    
​
vectorizer = TfidfVectorizer(keywords)
cosine_sim(keywords,vectorizer)
​
#cosine_sim(Text1, Text2, Text3, Text4, Text5)
​
​

Parrafos = []
N = 4 #numero de parrafos
Parrafos.append(TresParrafos('cnn.txt',N))
Parrafos.append(TresParrafos('euronews.txt',N))
Parrafos.append(TresParrafos('ElPais.txt',N))
​
​
​
todosParrafos = [j for i in Parrafos for j in i]
#print (Parrafos[0][0],Parrafos[1][1],Parrafos[2][1])

comPar = []
vectorizer = TfidfVectorizer( todosParrafos )
comPar = cosine_sim(todosParrafos , vectorizer)
print(comPar[0])
​

Nota = []
Nota.append(todosParrafos[4])
​
val, idx = min((val, idx) for (idx, val) in enumerate(comPar[1]))
print(val, idx)
val1, idx1 = min((val, idx) for (idx, val) in enumerate(comPar[idx]))
print(val1, idx1)
Nota.append(todosParrafos[idx1])
val2, idx2 = min((val, idx) for (idx, val) in enumerate(comPar[idx1]))
print(val2, idx2)
val3, idx3 = min((val, idx) for (idx, val) in enumerate(comPar[idx2]))
print(idx1,idx2,idx3)
Nota.append(todosParrafos[idx3])
​
​
