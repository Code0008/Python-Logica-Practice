user_data = 'root:84-61-E3-9A-61-61:Bolivia'

opciones = """

->[1] Obtener Direccion MAC
->[2] Obtener 'USUARIO'
->[3] Obtener Lugar

"""

print(user_data)
print(opciones)
pedir = int(input("Por Favor elija una opcion [+] "))
def MAC():
    direct_MAC = user_data[5:18]
    print('USER MAC' )
    print(direct_MAC)

def USUARIO():
    user = user_data[0:5]
    print('USER')
    print(user)
def LUGAR():
    date = user_data[-7:-1]
    print('LUGAR')
    print(date)

if pedir == 1:
    MAC()
elif pedir == 2:
    USUARIO()
elif pedir ==3:
    LUGAR()
else:
    print("Incorrect option")    