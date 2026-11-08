print("este es un registro en el cual su objetivo es saber cual es el valor en el que usted paga semanalmete en el uso transporte publico")
motivo=input("¿cual es el motivo por el cual usted toma el transporte publico?")
ruta=input("¿cual es la ruta que usted toma del transporte publico?")
dias=int(input("¿cuantos dias a la semana usted toma el transporte publico?"))
costo=float(input("¿cual es el costo del transporte publico que usted toma?"))
total_transporte=dias*2
total_pagar=total_transporte*costo
print("su total a pagar semanalmete en transporte publico es de: ", total_pagar)
print("usted monta en transporte publico", total_transporte, "de veces semanalmente")