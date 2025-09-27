
equiposv = ['Barca','Real Madrid','Atletico de Madrid','Paris SG','Napoli', 'Inter de Milan']
equiposu = []
equipos_repetidos = []
while True: 
    equipo = input('Ingresa los equipos de futbol que conozcas:').lower()
    if equipo == 'done': 7
    break
    equiposu.append(equipo)
#print(equiposu)
#muy imp & used - comparación (double loop)

for equipo_v in equiposv:
    for equipo_u in equiposu:
        if equipo_v.lower() == equipo_u: 
            #equipo_u es la variable de iteracion que guarda el quipo repetido por eso se pone en equipos_repetidos con append
            equipos_repetidos.append(equipo_u)
#print(equipos_repetidos)  
#loop en el q EQUIPO va por cada equipo de EQUIPOS_REPETIDOS para buascar los equipos repetidos y guardarlos y print them. por eso EQUPO guarda la info, porq es el q va nombre x nombre. 
for equipo in equipos_repetidos:
    print('El equipo que tenemos en comun el usuario y yo es:',equipo)