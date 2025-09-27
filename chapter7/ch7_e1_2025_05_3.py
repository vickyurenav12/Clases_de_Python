
text = "X-DSPAM-Confidence: 0.8475"
position1 = text.find('0')
print(position1)

position2 = text.find('5')
print(position2)

num = float((text[position1:position2+1]))
print(num)

num2 = num*100
print(num2)