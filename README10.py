valor1=["A","E","I","O","U","L","N","R","S","T"]
valor2= ["D","G"]
valor3=["B","M","C","P"]
valor4=["F","H","V","W","Y"]
valor5=["K"]
valor8=["J","X"]
valor10=["Q","Z"]


def Leerpalabra (palabra,*valores):
  puntos=0
  for n in range (len(palabra)):
      for a in range (len(valor1)):
         if palabra[n] == valor1[a]:
             puntos+= 1
      for b in range (len(valor2)):   
         if palabra[n] == valor2[b]: 
              puntos+= 2
      for m in range (len(valor3)):
         if palabra[n] == valor3[m]:
              puntos+= 3
      for g in range (len(valor4)):    
          if palabra[n] == valor4[g]:
             puntos+= 4
      for f in range (len(valor5)):    
         if palabra[n] == valor5[f]:
             puntos+= 5
      for j in range (len(valor8)):    
         if palabra[n] == valor8[j]:
             puntos+= 8
      for x in range (len(valor10)): 
          if palabra[n] == valor10[x]: 
             puntos+= 10
  print("sus puntos sumados son: ", puntos)


palabra= input("ingrese una palabra para sumar sus puntos!\n")
palabra=palabra.upper()

Leerpalabra(palabra,valor1,valor2,valor3,valor4,valor5,valor8,valor10)