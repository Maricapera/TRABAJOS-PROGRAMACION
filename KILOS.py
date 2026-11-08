print(" este programa esta diseñado para que usted sepa cuanto debe pagar por el kilo de papas y para cuantas personas alcanza ")
tienda=input("¿cual es el nombre de la tienda en la que compro las papas?")
kilos=int(input("¿cuantos kilos de papas usted compro?"))
personas=int(input("¿para cuantas personas alcanza el kilo de papa?"))
valor=float(input("¿cual es el valor del kilo de papa?"))
pagar=kilos*valor
total_personas=kilos*personas
print("usted debe pagar: ",pagar," pesos a la tienda: ",tienda)
print("el kilo de papa alcanza para: ",total_personas," personas")