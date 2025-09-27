#especificar el camino que tiene q tomar, Path
archivo = open('chapter7/mbox-short.txt','r')
"""count = 0
for line in archivo:
    count= count + 1
print(count)
"""
for line in archivo: 
    if line.startswith('From:'):
        #print(line)  
        position1 = line.find('@')
        position2 = line.find('.', position1 + 1)
        uni = ((line[position1+1:position2]))
        if uni == 'media': 
            new2 = line.find('.', position2+1)
            uni2=((line[position2+1:new2]))
            print(uni2)
            continue
        print(uni)