print("este es un programa en el cual su objetivo es ayudar a que usted sepa cuanto necesita para aprobar el año escolar") 
nom_institucion=input("¿cual es el nombre de la institucion en la que estudia?")
periodos_ya=int(input("¿cual es el numero de periodos que usted ya ha cursado?"))
nota_meta=float(input("¿cual es la nota que se necesita para aprobar el año final?"))
nota_periodo_1=float(input("¿cual fue su nota en el periodo 1?"))
nota_periodo_2=float(input("¿cual fue su nota en el periodo 2?"))
nota_periodo_3=nota_meta-(nota_periodo_1+nota_periodo_2)
print("su nota en el 3 periodo debe ser mayor de: ",nota_periodo_3)

