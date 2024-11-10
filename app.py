import mysql.connector
from urllib.parse import urlparse
password = "UCH_PASSWD"
dbc = urlparse("mysql://UCH_NOMBRE:UCH_PASSWD@localhost/UCH_BBDD")
connection=mysql.connector.connect (host=dbc.hostname,database=dbc.path.lstrip('/'),user=dbc.username,password=dbc.password)
cursor=connection.cursor()
Query="SHOW TABLES FROM UCH_BBDD"
cursor.execute(Query)
e=cursor.fetchall()
if len(e)<=0:
    Query="CREATE TABLE USUARIOS (NOMBRE TEXT NOT NULL, APELLIDO TEXT NOT NULL,EMAIL TEXT NOT NULL UNIQUE, PASSWORD TEXT NOT NULL, CARGO TEXT, AREA TEXT, EMPRESA TEXT, ROL TEXT NOT NULL);"
    cursor.execute(Query)
    Query="INSERT INTO USUARIOS(NOMBRE,APELLIDO,EMAIL,PASSWORD,ROL) VALUES ('TUNOMBRE','TUAPELLIDO','TUCORREO@TUDOMINIO.COM','TUPASSWD','Administrador')"
    cursor.execute(Query)
    connection.commit()
    cursor.close()
    connection.close()
Query="SHOW TABLES FROM UCH_BBDD"
cursor.execute(Query)
e=cursor.fetchall()
print(e)
cursor.close()
connection.close()  
