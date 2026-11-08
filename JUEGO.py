print("este programa esta hecho para contabilizar las partidas y horas que les dedican a los juegos")
juego1=input("¿cual es el nombre del juego que usted mas juega?")
juego2=input("¿cual es el nombre de el juego que usted juega en segundo lugar?")
juego_1=float(input("¿cuantas horas de: " + juego1 + " jugo?")) 
juego_2=float(input("¿cuantas horas de : " + juego2 + " jugo?"))
partidas1=int(input("¿cuantas partidas de: " + juego1 + " jugo?"))
partidas2=int(input("¿cuantas partidas de: " + juego2 + " jugo?"))
total_horas=juego_1+juego_2
total_partidas=partidas1+partidas2
print("el total de horas que usted dedico a los juegos es de: ",total_horas)
print("el total de partidas que usted jugo es de: ",total_partidas)
