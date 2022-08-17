import sqlite3
import numpy as np
from matplotlib import pyplot as plt

from datetime import date
from datetime import timedelta

#Funciones
def insertar():
	con = sqlite3.connect("corona.db") # change to 'sqlite:///your_filename.db'
	cur = con.cursor()
	cur.execute("SELECT * FROM t WHERE dia = (SELECT MAX(dia) FROM t);") # use your column names here
	row = cur.fetchall()
	#print(row)
	id1 = int(row[0][0])+1
	pais1 = row[0][1]
	latitud1 = row[0][2]
	longitud1 = row[0][3]
	date1 = input("Ingrese fecha: (AAAA-MM-DD): ")
	infectado1 = input("Ingrese acumulado de infectados del dia: ")
	infectadodia1 = int(infectado1) - int(row[0][5])
	muerte1 = input("Ingrese acumulado de muertes del dia: ")
	muertedia1 = int(muerte1) - int(row[0][7])
	todb = [id1, pais1, latitud1, longitud1, date1, infectado1, infectadodia1, muerte1, muertedia1]
	cur.execute("INSERT INTO t (id, pais, latitud, longitud, dia, infectacum, infectdia, muerteacum, muertedia) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", todb)
	con.commit()
	con.close()
	print("Datos insertados")
	
def borrar():
	borrar = input("ingrese la fecha del dato que desea borrar (AAAA-MM-DD): ")
	
	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM t WHERE dia = '" + borrar + "';")
	row = cur.fetchall()
	print("¿Desea eliminar la siguiente informaciòn?:")	
	print(row)
	pregunta = input("si - no: ")
	if pregunta == "si":
		cur.execute("DELETE FROM t WHERE dia = '" + borrar + "';")
	else:
		print("no eliminado")
	con.commit()
	con.close()
	
	

def leerdato():
	leer = input("ingrese la fecha del dato que desea leer (AAAA-MM-DD): ")
	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
	row = cur.fetchall()
	print(row)
	con.commit()
	con.close()

def actualizardato():
	con = sqlite3.connect("corona.db") # change to 'sqlite:///your_filename.db'
	cur = con.cursor()
	cur.execute("SELECT * FROM t WHERE dia = (SELECT MAX(dia) FROM t);") # use your column names here
	row = cur.fetchall()
	print(row)
	id1 = int(row[0][0])
	pais1 = row[0][1]
	latitud1 = row[0][2]
	longitud1 = row[0][3]
	date1 = input("Ingrese fecha: (AAAA-MM-DD): ")
	infectado1 = input("Ingrese acumulado de infectados del dia: ")
	infectadodia1 = int(infectado1) - int(row[0][5])
	muerte1 = input("Ingrese acumulado de muertes del dia: ")
	muertedia1 = int(muerte1) - int(row[0][7])
	todb = [id1, pais1, latitud1, longitud1, date1, infectado1, infectadodia1, muerte1, muertedia1]
	cur.execute("DELETE FROM t WHERE dia = '" + date1 + "';")
	cur.execute("INSERT INTO t (id, pais, latitud, longitud, dia, infectacum, infectdia, muerteacum, muertedia) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", todb)
	con.commit()
	con.close()
	print("Actualizar dato")

def graficaacumulada1():
    print("Gráfica frecuencia acumualada")

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
    plt.ylabel("Casos confirmados")

    plt.grid(True)

    t = np.arange(1,np.amax(x),0.1)
    plt.plot(x, y, 'bo--', markevery=3)
    plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    

    #plot
    plt.show()
    
def graficaacumulada2():
    print("Gráfica frecuencia acumualada")

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
    plt.ylabel("Muertes confirmadas")

    plt.grid(True)

    t = np.arange(1,np.amax(x),0.1)
    plt.plot(x, y2, 'ro--')
    plt.axes([0, np.amax(x), 0, np.amax(y)])

    #plot
    plt.show()

def graficadia1():
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
    plt.ylabel("Casos confirmados")

    plt.grid(True)

    t = np.arange(1,np.amax(x),0.1)
    plt.plot(x, y, 'bo--')
    plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
    plt.show()

def graficadia2():
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
    plt.ylabel("Muertes confirmadas")

    plt.grid(True)

    t = np.arange(1,np.amax(x),0.1)
    plt.plot(x, y2, 'ro--')
    plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
    plt.show()    


def minimoscuadrados():
	print("Mínimos cuadrados")

def diasmaximos():
	print("Dìas de contagios màximos:")
	conn = sqlite3.connect("corona.db")
	c = conn.cursor()
	myquery = ("SELECT * FROM t ORDER BY infectdia DESC LIMIT 5;")
	c.execute(myquery)
	rows=c.fetchall()
	i = 0
	print("dia\tfecha     \tacum\tdiario")
	for row in rows:
		print(str(rows[i][0])+"\t"+str(rows[i][4])+"\t"+str(rows[i][5])+"\t"+str(rows[i][6]))
		i = i + 1
	print("")
	print("Dìas de muertes màximos:")
	conn = sqlite3.connect("corona.db")
	c = conn.cursor()
	myquery = ("SELECT * FROM t ORDER BY muertedia DESC LIMIT 5;")
	c.execute(myquery)

	rows=c.fetchall()
	i = 0
	print("dia\tfecha     \tacum\tdiario")
	for row in rows:
		print(str(rows[i][0])+"\t"+str(rows[i][4])+"\t"+str(rows[i][7])+"\t"+str(rows[i][8]))
		i = i + 1


def datosMes():
	print("La fecha màs antigua es febrero 2020.")
	anno = input("Ingrese año:")
	mes = input("ingrese mes:")
	conn = sqlite3.connect("corona.db")
	c = conn.cursor()
	myquery = ("SELECT *, strftime('%Y',dia) as 'Anno', strftime('%m',dia) as 'mes' FROM t;")
	c.execute(myquery)

	rows = c.fetchall()
	rowinfectado = []

	i = 0
	for row in rows:
		if(int(rows[i][9]) == int(anno) and int(rows[i][10]) == int(mes)):
			#print(row)
			rowinfectado.append(row)

		i = i + 1

	#print(rowinfectado)


	y = np.array([])
	y2 = np.array([])
	label = np.array([])

	for row in rowinfectado:
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

	y3 = np.array([])
	y4 = np.array([])
	label1 = np.array([])
	for row in rowinfectado:
		y3 = np.append(y3,int(row[6]))
		y4 = np.append(y4, int(row[8]))
		label1 = np.append(label1,row[4])
		#print(row[4],row[5],row[7])

	x2 = np.arange(1,len(y3)+1,1)

	plt.title("Covid19 México (Casos diarios)")
	plt.xticks(x2,label1,rotation='vertical')
	plt.xlabel("Dias desde Feb 28 - 2020")
	plt.ylabel("Casos confirmados(azul) muertos(rojo)")

	plt.grid(True)

	t = np.arange(1,np.amax(x2),0.1)
	plt.plot(x2, y3, 'bo--',x2,y4,'rD--')
	plt.axes([0, np.amax(x2), 0, np.amax(y3)])
    
	#plot
	plt.show()

	print("Dìas de contagios màximos:")
	conn = sqlite3.connect("corona.db")
	c = conn.cursor()
	myquery = ("SELECT *, strftime('%Y',dia) as 'Anno', strftime('%m',dia) as 'mes' FROM t ORDER BY infectdia DESC;")
	c.execute(myquery)
	rows=c.fetchall()
	i = 0
	j = 0
	print("dia\tfecha     \tacum\tdiario")
	for row in rows:
		if(int(rows[i][9]) == int(anno) and int(rows[i][10]) == int(mes)):
			print(str(rows[i][0])+"\t"+str(rows[i][4])+"\t"+str(rows[i][5])+"\t"+str(rows[i][6]))
			j = j + 1
		if(int(j)>5):
			break
		i = i + 1
	print("")
	print("Dìas de muertes màximos:")
	conn = sqlite3.connect("corona.db")
	c = conn.cursor()
	myquery = ("SELECT *, strftime('%Y',dia) as 'Anno', strftime('%m',dia) as 'mes' FROM t ORDER BY muertedia DESC;")
	c.execute(myquery)

	rows=c.fetchall()
	i = 0
	j = 0
	print("dia\tfecha     \tacum\tdiario")
	for row in rows:
		if(int(rows[i][9]) == int(anno) and int(rows[i][10]) == int(mes)):
			print(str(rows[i][0])+"\t"+str(rows[i][4])+"\t"+str(rows[i][7])+"\t"+str(rows[i][8]))
			j = j + 1
		if(int(j)>5):
			break
		i = i + 1







def mostrardata():
    conn = sqlite3.connect("corona.db")
    c = conn.cursor()
    myquery = ("SELECT * FROM t;")
    c.execute(myquery)

    rows=c.fetchall()
    for row in rows:
        print(row)




def anualcontagioacumulado():
	print("Anual:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	

	
	y = np.array([])
	label = np.array([])


	for i in years:
		
		if(i != yearcurrent):
			leer = str(i)+"-"+str(12)+"-"+str(31)
			cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][5]))
			label = np.append(label,rows[0][4])
			
			
			con.commit()
		else:
			cur.execute("SELECT * FROM t ORDER BY id DESC LIMIT 1;")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][5]))
			label = np.append(label,rows[0][4])
			
			con.commit()


	x = np.arange(1,len(y)+1,1)
	
	plt.title("Covid19 México Contagio Acumulado Anual")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Contagios confirmados")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y, 'bo--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  

	

	con.close()

def anualcontagio():
	print("Anual:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	

	
	y = np.array([])
	y2 = np.array([])
	label = np.array([])


	for i in years:
		
		if(i != yearcurrent):
			leer = str(i)+"-"+str(12)+"-"+str(31)
			cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][5]))
			label = np.append(label,rows[0][4])
			
			
			con.commit()
		else:
			cur.execute("SELECT * FROM t ORDER BY id DESC LIMIT 1;")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][5]))
			label = np.append(label,rows[0][4])
			
			con.commit()

	x = np.arange(1,len(y)+1,1)
	y = np.hstack([0,y])
	y2 = np.diff(y)
	plt.title("Covid19 México Contagio Anual")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Contagios confirmados")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y2, 'bo--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  

	

	con.close()


def anualmuerteacumulado():
	print("Anual:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	
	y = np.array([])
	label = np.array([])


	for i in years:
		
		if(i != yearcurrent):
			leer = str(i)+"-"+str(12)+"-"+str(31)
			cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][7]))
			label = np.append(label,rows[0][4])
			
			con.commit()
		else:
			cur.execute("SELECT * FROM t ORDER BY id DESC LIMIT 1;")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][7]))
			label = np.append(label,rows[0][4])

			con.commit()


	x = np.arange(1,len(y)+1,1)
	
	plt.title("Covid19 México Muertes Acumulado Anual")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Muertes confirmadas")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y, 'ro--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  
	con.close()



def anualmuerte():
	print("Anual:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	

	
	y = np.array([])
	y2 = np.array([])
	label = np.array([])


	for i in years:
		
		if(i != yearcurrent):
			leer = str(i)+"-"+str(12)+"-"+str(31)
			cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][7]))
			label = np.append(label,rows[0][4])
			
			
			con.commit()
		else:
			cur.execute("SELECT * FROM t ORDER BY id DESC LIMIT 1;")
			rows = cur.fetchall()
			y = np.append(y,int(rows[0][7]))
			label = np.append(label,rows[0][4])
			
			con.commit()

	x = np.arange(1,len(y)+1,1)
	y = np.hstack([0,y])
	y2 = np.diff(y)
	plt.title("Covid19 México Contagio Anual")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Contagios confirmados")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y2, 'ro--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  
	con.close()

def semanalcontagioacumulado():
	print("Semanal:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	weeks = []

	y = np.array([])
	label = np.array([])


	for i in years:
		if(i != yearcurrent):
			for s in all_sundays(i):
				leer = str(s)
				
				cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
				rows = cur.fetchall()
				y = np.append(y,int(rows[0][5]))
				label = np.append(label,rows[0][4])
				con.commit()
		else:
			for s in all_sundays(yearcurrent):
				leer = str(s)
				try:
					cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
					rows = cur.fetchall()
					y = np.append(y,int(rows[0][5]))
					label = np.append(label,rows[0][4])
					con.commit()
				except:
					break

			


	x = np.arange(1,len(y)+1,1)
	
	plt.title("Covid19 México Casos Positivos Acumulado Semanal")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Muertes confirmadas")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y, 'bo--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  

	con.close()

def semanalmuerteacumulado():
	print("Semanal:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	weeks = []

	y = np.array([])
	label = np.array([])


	for i in years:
		if(i != yearcurrent):
			for s in all_sundays(i):
				leer = str(s)
				
				cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
				rows = cur.fetchall()
				y = np.append(y,int(rows[0][7]))
				label = np.append(label,rows[0][4])
				con.commit()
		else:
			for s in all_sundays(yearcurrent):
				leer = str(s)
				try:
					cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
					rows = cur.fetchall()
					y = np.append(y,int(rows[0][7]))
					label = np.append(label,rows[0][4])
					con.commit()
				except:
					break

			


	x = np.arange(1,len(y)+1,1)
	
	plt.title("Covid19 México Muertes Acumulado Semanal")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Muertes confirmadas")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y, 'ro--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  

	con.close()


def semanalcontagio():
	print("Semanal:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	weeks = []

	y = np.array([])
	label = np.array([])


	for i in years:
		if(i != yearcurrent):
			for s in all_sundays(i):
				leer = str(s)
				
				cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
				rows = cur.fetchall()
				y = np.append(y,int(rows[0][5]))
				label = np.append(label,rows[0][4])
				con.commit()
		else:
			for s in all_sundays(yearcurrent):
				leer = str(s)
				try:
					cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
					rows = cur.fetchall()
					y = np.append(y,int(rows[0][5]))
					label = np.append(label,rows[0][4])
					con.commit()
				except:
					break

			


	x = np.arange(1,len(y)+1,1)
	y = np.hstack([0,y])
	y2 = np.diff(y)
	plt.title("Covid19 México Contagio Semanal")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Contagios confirmados")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y2, 'bo--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  

	

	con.close()

def semanalmuerte():
	print("Semanal:")

	con = sqlite3.connect("corona.db")
	cur = con.cursor()
	year1 = 2020
	yearcurrent = date.today().year
	years = list(range(year1,yearcurrent+1))
	weeks = []

	y = np.array([])
	label = np.array([])


	for i in years:
		if(i != yearcurrent):
			for s in all_sundays(i):
				leer = str(s)
				
				cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
				rows = cur.fetchall()
				y = np.append(y,int(rows[0][7]))
				label = np.append(label,rows[0][4])
				con.commit()
		else:
			for s in all_sundays(yearcurrent):
				leer = str(s)
				try:
					cur.execute("SELECT * FROM t WHERE dia = '" + leer + "';")
					rows = cur.fetchall()
					y = np.append(y,int(rows[0][7]))
					label = np.append(label,rows[0][4])
					con.commit()
				except:
					break

			


	x = np.arange(1,len(y)+1,1)
	y = np.hstack([0,y])
	y2 = np.diff(y)
	plt.title("Covid19 México Contagio Semanal")
	plt.xticks(x,label,rotation='vertical')
	plt.xlabel("")
	plt.ylabel("Contagios confirmados")

	plt.grid(True)

	t = np.arange(1,np.amax(x),0.1)
	plt.plot(x, y2, 'ro--')
	plt.axes([0, np.amax(x), 0, np.amax(y)])
    
    #plot
	plt.show()  
	con.close()




def all_sundays(year):
    #January
    dt = date(year,1,1)

    #First Sunday of given year
    dt += timedelta(days=6-dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)

print("Bienvenido al análisis de datos de Covid19 en México \n")

#Menú principal
while True:
    #Menu
	print("1.- Agregar nuevo dato")
	print("2.- Borrar dato")
	print("3.- Leer dato")
	print("4.- Actualizar dato")
	print("-------")
	print("5.- Diario Gráfica acumulada casos positivos")
	print("6.- Diario Gráfica acumulada muertes")
	print("7.- Diario Gráfica por día casos positivos")
	print("8.- Diario Gráfica por día muertes")
	print("-------")
	print("9.- Semanal Gráfica acumulada casos positivos")
	print("10.- Semanal Gráfica acumulada muertes")
	print("11.- Semanal Gráfica casos positivos")
	print("12.- Semanal Gráfica muertes")
	print("-------")
	print("13.- Mensual Gráfica acumulada casos positivos")
	print("14.- Mensual Gráfica acumulada muertes")
	print("15.- Mensual Gráfica casos positivos")
	print("16.- Mensual Gráfica muertes")
	print("-------")
	print("17.- Anual Gráfica acumulada casos positivos")
	print("18.- Anual Gráfica acumulada muertes")
	print("19.- Anual Gráfica casos positivos")
	print("20.- Anual Gráfica muertes")
	print("-------")
	print("21.- Mínimos cuadrados")
	print("22.- Proyecciòn")	
	print("23.- Dìas Màximos")
	print("24.- Mostrar todos los datos")
	print("25.- Salir")
    
    #entrada
	eleccion = input("Ingrese la opción deseada 1-25:")
    
	if(eleccion.isnumeric()):
		if( int(eleccion) < 26 and int(eleccion) > 0):
			if(int(eleccion)==1):
				insertar()
               
			if(int(eleccion)==2):
				borrar()

			if(int(eleccion)==3):
				leerdato()

			if(int(eleccion)==4):
				actualizardato()

			if(int(eleccion)==5):
				graficaacumulada1()
            
			if(int(eleccion)==6):
				graficaacumulada2()

			if(int(eleccion)==7):
				graficadia1()
            
			if(int(eleccion)==8):
				graficadia2()

			if(int(eleccion)==9):
				semanalcontagioacumulado()

			if(int(eleccion)==10):
				semanalmuerteacumulado()
			
			if(int(eleccion)==11):
				semanalcontagio()
				
            
			if(int(eleccion)==12):
				semanalmuerte()

			if(int(eleccion)==17):
				anualcontagioacumulado()

			if(int(eleccion)==18):
				anualmuerteacumulado()
			
			if(int(eleccion)==19):
				anualcontagio()
            
			if(int(eleccion)==20):
				anualmuerte()

			if(int(eleccion)==21):
				print("minimos cuadrados")
                
			if(int(eleccion)==22):
				print("proyeccion")

			if(int(eleccion)==23):
				diasmaximos()
            
			if(int(eleccion)==24):
				mostrardata()
                
			if(int(eleccion)==25):
				print("Adios")
				break
		else:
			print("Opcion inválida")
	else:
		print("Opción inválida")

