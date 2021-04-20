import csv

archivo= open('/home/nelux/facu/bgg_db_1806.csv', 'r')
csvreader = csv.reader(archivo, delimiter=',')

encabezado = next(csvreader)
print(encabezado)
print("=" * 50)


for linea in csvreader:
  if (int(linea[5]) < 3) and (linea[17] == "Card Game"):
    print(linea[3])
archivo.close()