'''
import csv

linea = []

with open("corona.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        print('line[{}] = {}'.format(i, line))
        linea.append(str(line)) 

f = open("corona2.csv", "a")
lineaa = (linea[0]+"\n").replace("[","")
lineaa = lineaa.replace("]","")
f.write(lineaa)
lineaa = (linea[1]+"\n").replace("[","")
lineaa = lineaa.replace("]","")
f.write(lineaa)



for counter in range(0,115):
    lineaa = (linea[117-counter]+"\n").replace("[","")
    lineaa = lineaa.replace("]","")
    f.write(lineaa)

f.close()

#open and read the file after the appending:
f = open("corona2.csv", "r")
print(f.read())
f.close()

'''


import csv, sqlite3

con = sqlite3.connect("corona.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE t (id, pais, latitud, longitud, dia, infectacum, infectdia, muerteacum, muertedia);") # use your column names here

with open('corona2.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ID'], i['País'], i['Latitud'], i['Longitud'], i['Date'], i['Infectados Acumulado'], i['Infectados Día'], i['Muertes Acumulado'], i['Muertes Día']) for i in dr]

cur.executemany("INSERT INTO t (id, pais, latitud, longitud, dia, infectacum, infectdia, muerteacum, muertedia) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

'''
# Importa el módulo sqlite3
import sqlite3

# Crea un objeto de conexión a la base de datos SQLite
con = sqlite3.connect("corona.db")

# Con la conexión, crea un objeto cursor
cur = con.cursor()

# El resultado de "cursor.execute" puede ser iterado por fila
for row in cur.execute('SELECT * FROM t;'):
    print(row)

# No te olvides de cerrar la conexión
con.close()
'''
