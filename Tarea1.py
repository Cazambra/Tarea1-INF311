from datetime import datetime

arc = open("logs.txt","a")

now = datetime.now()
now = str(now)
def compareStrings(a,b):
    if ((type(b) is not str) and (type(a) is not str)):
        return ("Error: Ambas cadenas no son String")
    elif (type(a) is not str):
        return ("Error: Cadena A no es un String")
    elif (type(b) is not str):
        return ("Error: Cadena B no es un String")
    else:
        if (len(a) > len(b)):
            return("Cadena A más larga que cadena B")
        elif (len(a) < len(b)):
            return("Cadena B más larga que cadena A")
        else:
            return("Ambas cadenas son del mismo largo")
#Aquí cambiar inputs
a = "hola mundo"
b = "hola mu"
res = compareStrings(a, b)
print(res)

arc.write("Fecha: "+now+" Cadena A: "+str(a)+" Cadena B: "+str(b)+" Resultado: "+res + "\n")

arc.close()


    
