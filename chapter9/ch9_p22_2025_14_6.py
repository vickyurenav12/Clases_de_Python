#especificar el camino que tiene q tomar, Path
archivo = open('chapter7/mbox-short.txt','r')
iniciar = dict()

i = 0
for line in archivo:
    #pro-contador en .py
    i += 1
    if line.startswith('From '):
        words= line.split()  
        #print(words[2])
        word = words[2]
        iniciar[word]= iniciar.get(word,0)+1
print('los dias que mas se envian correos son los:',iniciar)