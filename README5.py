texto= input("""\ningrese una frase:\n""")

sacar= ".,\n"
for car in sacar:
   texto=texto.replace(car,"")
palabras= texto.lower().split(" ")
print (texto)
print (palabras)
pal= input ("""\ningrese palabra a buscar:\n""")
count= palabras.count(pal)
print (f"la palabra: {pal} se encuentra {count} vez/veces")
