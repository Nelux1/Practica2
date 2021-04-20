heterograma= input("""ingrese una palabra o frase que sea heterograma!\n""")
[]
heterograma= heterograma.replace(" ","")
true=1
for n in range (len(heterograma)):
    for a in range (n + 1,len(heterograma)):
      if heterograma[n] == heterograma[a]:
         true=0
if true == 1:
  print(f'FELICITACIONES!! LA PALABRA ES UN HETEROGRAMA!!')         
else: 
  print(" Esa frase o palabra no es un heterograma!!")         

