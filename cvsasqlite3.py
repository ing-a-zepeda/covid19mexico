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
import csv, sqlite3, os

# Remove old db file
os.remove("corona.db")


# Create connection object to SQLite3 DB
con = sqlite3.connect("corona.db") # change to 'sqlite:///your_filename.db'
# Create cursor object
cur = con.cursor()
# Create Table t
cur.execute("CREATE TABLE t (id INTEGER PRYMARY KEY, pais, latitud, longitud, dia, infectacum INTEGER, infectdia INTEGER, muerteacum INTEGER, muertedia INTEGER);") # use your column names here

# Insert data from CSV file
with open('corona.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ID'], i['Pais'], i['Latitud'], i['Longitud'], i['Date'], i['InfectadosAcumulado'], i['InfectadosDia'], i['MuertesAcumulado'], i['MuertesDia']) for i in dr]

cur.executemany("INSERT INTO t (id, pais, latitud, longitud, dia, infectacum, infectdia, muerteacum, muertedia) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()



os.system("pause")
