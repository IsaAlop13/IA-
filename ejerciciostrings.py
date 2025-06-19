texto = (input("Escriba un texto: "))
min = texto.lower()
sinespacios = min.strip()
tildes = sinespacios.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
palabras = tildes.split()
inv = palabras[::-1]
textofinal = "".join(inv)
print("Texto final: ",textofinal)