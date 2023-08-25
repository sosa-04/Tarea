try:
    hours= float(input("Introduzca la cantidad de horas: "))
    tarifa= float(input("Introduzca la tarifa por hora: "))

    if(hours>40):
        extra=hours-40
        tarifaextra=tarifa*1.5
        salarioextra=extra*tarifaextra
        salario=40*tarifa
        total=salarioextra+salario
        print("Salario: ",total)
    else:
        result=hours*tarifa
        print("Salario: ",result)
except:
    print("Por favor, introduzca un numero")