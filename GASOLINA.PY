print("este programa esta diseñado para poder contabilizar la gasolina gastada, total motos y clientes")
atendio=input("¿quien estaba a cargo de tender ese dia?")
gasolina_mañana=float(input("¿cuantos galones de gasolina se gasto en la mañana?"))
gasolina_tarde=float(input("¿cuantos galones de gasolina se gasto en la tarde?"))
motos=int(input("¿cuantas motos se atendieron ese dia?"))
clientes=int(input("¿cuantos clientes se atendieron ese dia?"))
total_gasolina=gasolina_mañana+gasolina_tarde
gasolina_moto=total_gasolina/motos
print("el total de gasolina que se gasto ese dia fue de: ",total_gasolina, "galones")
print("el total de gasolina que se gasto por cada moto fue de: ",gasolina_moto, "galones")