#!/bin/bash/env python3

def main():
        x= input("[+]Ingrese la contraseña: ")
        with open("dicctionary.txt", 'r', encoding='utf-8') as cred:
            for line in cred:                
                if x in line.split(":")[1]:
                     print("Contraseña correcta ")
                else:
                     print("Contraseña incorrecta ")
if __name__ == '__main__':
    main()
