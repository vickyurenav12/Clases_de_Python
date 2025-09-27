#especificar el camino que tiene q tomar, Path
archivo = open('chapter7/mbox-short.txt','r')
"""count = 0
for line in archivo:
    count= count + 1
print(count)
"""
for line in archivo: 
    if line.startswith('From:'):
        print(line)