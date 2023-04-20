print("************************************************************************************************************************************************************\n")
print("                                                                parcial 2 programa que servira para algo                                                    \n")
print("*************************************************************************************************************************************************************\n")

while True:
    try:
        n = int(input("Ingresa un número entero positivo: "))
        if n <= 0:
            raise ValueError("El número debe ser positivo")
        break
    except ValueError as e:
        print("Error: " + str(e))
        
sumatoria = 0
for i in range(1, n+1):
    sumatoria += (1/i)
    
print("La suma de la serie es:", sumatoria)

print("*************************************************************************************************************************************************************\n")

print("                                                                           Fin parcial                                                                       \n")

print("*************************************************************************************************************************************************************\n")