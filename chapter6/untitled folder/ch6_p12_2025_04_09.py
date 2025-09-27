
word= input('insert a word: ')
incog=input('insert letter you want to find: ')
count= 0

for letter in word: 
    if letter == incog:
        count= count + 1
print(count)
