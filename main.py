from audioop import reverse


print("-----Verificador de mayoria de edad------")
edad = input("Ingrese su edad: ")
if int(edad) < 18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")    
print("-----Fin Validador de Edad- -----")

print("----------Validador de numeros pares----------")
numeroinicial :  int = int(input ("Ingrese un numero: "))
numerofinal: int = int(input ("Ingrese un segundo numero: "))
numerosimpares = []

while numerofinal <= numeroinicial:
    numerofinal = input("El segundo numero tiene que ser mayor. Ingrese otro numero: ")
    
for i in range(numeroinicial,numerofinal):
    if i % 2 != 0:
        numerosimpares.append(i) 
        
print(f"Lista de numeros impares entre  {numeroinicial} y {numerofinal}:")   
print(numerosimpares)       
print("-----Fin Validador de numeros pares- -----")

print("")
print("Invertir 100 numeros-------<<<<<<<<<<<<<")

numeros1a100 = range(0,100)

for i in reversed(numeros1a100):
    print(i)
    
