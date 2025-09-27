total=0
count=0
while True:
    user_input = input('input an integer (done is the final step):')
    if user_input =='done':
        break
    try:
        user_input=int(user_input)
    except:
        print('invalid input. try again')
        continue
    total=total+1
    count=count+user_input
    print('correct numer input')
    
#average con valores finales
average=count/total

print(count)
print(total)
print(average)