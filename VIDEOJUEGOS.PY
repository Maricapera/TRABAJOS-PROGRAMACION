print(" bienvenido a la tienda mundo gamer")
email_cliente=input("¿cual es su correo electronico?")
juego_comprar=input("¿cual es el nombre del juego que va a comprar?")
juego_cantidad=int(input("¿cuantos juegos lleva con esa referencia?"))
juego_costo=float(input("¿cual es el precio de la referencia de ese juego?"))
dinero_billetera=float(input("¿cuanto dinero trae en su billetera?"))
juego_total=juego_cantidad*juego_costo
billetera=dinero_billetera-juego_total
print("si compra este juego su total seria de: ",juego_total, "y en su billetera quedaria un total de: ",billetera,)