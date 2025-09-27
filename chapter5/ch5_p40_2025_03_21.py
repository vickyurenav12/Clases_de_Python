"""
lasgest_so_far= -1
numbers= [9,8,56,23,45,98,72]
for num in numbers: 
    if num > lasgest_so_far: 
        lasgest_so_far = num 
    print(lasgest_so_far)
"""""
    
smallest_so_far= None
numbers= [9,8,56,23,1,-98,72]
for num in numbers: 
    if smallest_so_far == None:
        smallest_so_far=num
    elif num < smallest_so_far: 
        smallest_so_far = num 
    print(smallest_so_far)