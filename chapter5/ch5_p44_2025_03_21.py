#notas: 60,78,80,93,95,67,88,85,56,80

notas=[60,78,80,93,95,67,88,85,56,80,98,100,45,30]
i=0
sum=0
for nota in notas: 
    i=i+1
    #sum es el numero inicial + la nota y asi sucesivamente
    sum=nota+sum
nota_final=sum/i
#contador
print(i) 
print(nota_final)




    