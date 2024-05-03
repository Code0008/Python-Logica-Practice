def clear(string, url):

    retur =  []
    for i in string:
        a = i.split(url)
        x = "".join(a)
        retur.append(x)
    ñ = "".join(retur)
    return f'{ñ}'

leer= input('Ingrese archivo a leer: ')
url =  input('ingrese la url para limpiar: ')


try:
    arch = open(leer,'r', encoding='utf8')
    e=arch.readlines()
except  Exception as r:
    print(f'ocurrio ul error {r} por favor verificar')


try:
    al = clear(e, url)
except Exception as r:
    print(f'por favor reinicie el proceso')

try:
    arch2 = open('limpio.txt','w', encoding='utf8' )
    arch2.write(al)
except Exception as r:
    print(f'ocurrio una falla en la matix xd')
finally:    
    arch2.close()

print(f'el archivo {leer} fue "limpiado" correctamente. ')
