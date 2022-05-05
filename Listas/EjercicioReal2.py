from colorama import *
MACS = ['root:19-B7-00-94-0C-B5:bolivia',
 'admin:9A-5F-A0-34-13-DC:Peru',
 'mychel:14-21-CB-78-D1-21:Peru',
  'edson:3F-C9-89-25-41-AD:Peru' ]

screen = """
Las direcciones de los usuarios de la empresa: 
"""
options = """
[+]1. ver todas las direcciones MAC
[+]2. ver usuarios
[+]3. ver ubicacion 
[+]4. imprimir completo alguna direccion MAC completa especifica 
"""


def pantalla():
    print(f'{Fore.GREEN} {options} {Fore.RESET}')
    peticion = int(input('[+]'))
    sep = 50 * '*'
    sep2 = 25 * '*'
    def mac():
        print(f'{Fore.LIGHTGREEN_EX} {MACS} {Fore.RESET}')

        print(f'{Fore.MAGENTA}{sep} MAC DIRECTION{sep} {Fore.RESET}')

    def USERS():
        users = MACS[0]
        users = users[0:5]
        print(f'{Fore.MAGENTA} {users} {Fore.RESET}')

    def ZONE():
        zone = MACS[1]
        zone = zone[-1:-7]
        print(f'{Fore.LIGHTGREEN_EX} {sep} {zone} {sep} {Fore.RESET}')
    
    def MAC():
        FirsUser = MACS[0]
        SecondUser = MACS[1]
        thirdUser = MACS[2]
        FourtUser = MACS[3]
        print(f'{Fore.LIGHTMAGENTA_EX} por favor ingrese el orden del usuario que quiera \n ver su direccion MAC.')
        select = int(input('[>]'))

        if select == 1:
            print(f'{Fore.LIGHTCYAN_EX} {sep2} FirsUser \n {sep2} {FirsUser} \n [>] Mac del primer usuario {Fore.RESET}')
        elif select == 2:
            print(f'{Fore.LIGHTCYAN_EX} {sep2} FirsUser \n {sep2} {SecondUser} \n [>] Mac del segundo usuario {Fore.RESET}')
        elif select == 3:
            print(f'{Fore.LIGHTCYAN_EX} {sep2} FirsUser \n {sep2} {thirdUser} \n [>] Mac del tercer usuario {Fore.RESET}')
        elif select == 4:
            print(f'{Fore.LIGHTCYAN_EX} {sep2} FirsUser \n {sep2} {FourtUser} \n [>] Mac del cuarto  usuario {Fore.RESET}')


    if peticion == 1:
        mac()

    elif peticion == 2:
        USERS()

    elif peticion == 3:
        ZONE()
    elif peticion == 4:
        MAC()

print(f'{Fore.RED} >>> Type run \n ')
pedir = input("[+] ")
if pedir == 'run' or 'RUN' or 'Run':
    pantalla()
