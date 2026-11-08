print("este programa ayuda a calcular el area y el perimetro de un salon en metros")
salon=input("¿cual es el numero del salon que usted desea calcular?")
institucion=input("¿cual es el nombre de la institucion en el que esta el salon?")
largo=int(input("¿cual es el largo del salon en metros?"))
ancho=float(input("¿cual es el ancho del salon en metros?"))
operacion_area=largo*ancho
operacion_perimetro_1=largo+ancho
operacion_perimetro_2=operacion_perimetro_1*2 
print("el area del salon: ",salon, "de la institucion: ",institucion, "es de: ",operacion_area, "metros cuadrados")
print("el perimetro del salon: ",salon, "de la institucion: ",institucion, "es de: ",operacion_perimetro_2, "metros")