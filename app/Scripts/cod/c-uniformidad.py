import sqlite3
acu = 0
conexion =sqlite3.connect("bbdd")
cursor=conexion.cursor()
#cursor.execute("CREATE TABLE DATOS(LATERAL INTEGER,GOTERO INTEGER,CAUDAL FLOAT)")
#cursor.execute("INSERT INTO DATOS VALUES('1','1','0')")
cursor.execute("SELECT * FROM DATOS")
tds_datos = cursor.fetchall()

def coef_uniformidad(Q):
    
    
    
    print(puntos)
    

for registro in tds_datos:
    a.replace(registro[2],'.')
    coef_uniformidad(registro[2])
    












conexion.close()