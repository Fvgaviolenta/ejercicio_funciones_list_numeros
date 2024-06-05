lista_num = []
lista_num_str = []
num_pares = []
num_impares = []

def validar_lista_numeros():
    while True:
        numeros_usuario = input("Ingrese una secuencia de numeros enteros separado por espacio: ")
        
        lista_num_str = (numeros_usuario.split())
        
        try:
            for numero in lista_num_str:
                numero = int(numero)
                lista_num.append(numero)
            print(f"Lista de numeros completa: {lista_num}")
            return lista_num
        except:
            print("Todos los numeros deben ser numeros enteros, porfavor intentalo nuevamente")


validar_lista_numeros()
for numero in lista_num:
    numero = int(numero)
    if numero % 2 ==0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)


print(f"Aqui esta la lista de numeros pares: {num_pares}")
print(f"Aqui esta la lista de numeros impares: {num_impares}")