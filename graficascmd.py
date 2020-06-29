import sqlite3
import numpy as np
from matplotlib import pyplot as plt


#Funciones

def insertar():
    print("Insertar")

def borrar():
    print("Borrar")

def leerdato():
    print("Leer dato")

def actualizardato():
    print("Actualizar dato")

def graficaacumulada():
    print("Gráfica acumualada")

    y = np.array([])
    y2 = np.array([])
    label = np.array([])

    conn = sqlite3.connect("corona.db")
    c = conn.cursor()
    myquery = ("SELECT * FROM t;")
    c.execute(myquery)

    rows=c.fetchall()
    for row in rows:
        y = np.append(y,int(row[5]))
        y2 = np.append(y2, int(row[7]))
        label = np.append(label,row[4])
        #print(row[4],row[5],row[7])

    x = np.arange(1,len(y)+1,1)



    plt.title("Covid19 México (Freq. Acumulada)")
    plt.xticks(x,label,rotation='vertical')
    plt.xlabel("Dias desde Feb 28 - 2020")
    plt.ylabel("Casos confirmados(azul) muertos(rojo)")

    plt.grid(True)

    t = np.arange(1,np.amax(x),0.1)
    plt.plot(x, y, 'bo--',x,y2,'rD--')
    plt.axes([0, np.amax(x), 0, np.amax(y)])

    #plot
    plt.show()
    
    

def graficadia():
    print("Gráfica por día")
    y = np.array([])
    y2 = np.array([])
    label = np.array([])

    conn = sqlite3.connect("corona.db")
    c = conn.cursor()
    myquery = ("SELECT * FROM t;")
    c.execute(myquery)

    rows=c.fetchall()
    for row in rows:
        y = np.append(y,int(row[6]))
        y2 = np.append(y2, int(row[8]))
        label = np.append(label,row[4])
        #print(row[4],row[5],row[7])

    x = np.arange(1,len(y)+1,1)



    plt.title("Covid19 México (Casos diarios)")
    plt.xticks(x,label,rotation='vertical')
    plt.xlabel("Dias desde Feb 28 - 2020")
    plt.ylabel("Casos confirmados(azul) muertos(rojo)")

    plt.grid(True)

    t = np.arange(1,np.amax(x),0.1)
    plt.plot(x, y, 'bo--',x,y2,'rD--')
    plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
    plt.show()
    


def mínimoscuadrados():
    print("Mínimos cuadrados")

def mostrardata():
    conn = sqlite3.connect("corona.db")
    c = conn.cursor()
    myquery = ("SELECT * FROM t;")
    c.execute(myquery)

    rows=c.fetchall()
    for row in rows:
        print(row)


    print(type(rows))
    print(rows[0][0])




print("Bienvenido al análisis de datos de Covid19 en México \n")

#Menú principal
while True:
    #Menu
    print("1.- Agregar nuevo dato")
    print("2.- Borrar dato")
    print("3.- Leer dato")
    print("4.- Actualizar dato")
    print("5.- Gráfica acumulada")
    print("6.- Gráfica por día")
    print("7.- Mínimos cuadrados")
    print("8.- ????")
    print("9.- Mostrar todos los datos")
    print("10.- Salir")
    
    #entrada
    eleccion = input("Ingrese la opción deseada 1-10:")
    
    if(eleccion.isnumeric()):
        if( int(eleccion) < 11 and int(eleccion) > 0):
            if(int(eleccion)==1):
               insertar()
               
            if(int(eleccion)==2):
                borrar()

            if(int(eleccion)==3):
                leerdato()

            if(int(eleccion)==4):
                actualizardato()

            if(int(eleccion)==5):
                graficaacumulada()

            if(int(eleccion)==6):
                graficadia()

            if(int(eleccion)==7):
                mínimoscuadrados()

            if(int(eleccion)==8):
                print("?????")

            if(int(eleccion)==9):
                mostrardata()

            if(int(eleccion)==10):
                print("Adios")
                break
        else:
            print("Opcion inválida")
    else:
        print("Opción inválida")





