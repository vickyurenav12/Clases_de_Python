#count letras
#lower 
#upper
# vocals -> u 
#backwards 
# print cada step 

country = input('Insert the name of your country: ')
count = 0 
for letter in country: 
    count = count + 1 
print (count)

print(len(country))

country_lower = country.lower()
print(country_lower) 

country_upper = country.upper()
print(country_upper)

vocales = country.replace('a','u').replace('e','u').replace('i','u').replace('o','u')
print(vocales)

country_backwards = country[::-1]
print(country_backwards)

vocales = country.replace('na','xx').replace('la','xx').replace('el','xx')
print(vocales)