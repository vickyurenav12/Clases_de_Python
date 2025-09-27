count = dict()
line = int(input('enter a phrase:'))
words = line.split()

for word in words:
    count[word]= count.get(word,0)+1
print(count)
