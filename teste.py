import mysql.connector

cnx = mysql.connector.connect(user='PauloV', password='Paulov1732?',
                              host='localhost',
                              auth_plugin= 'mysql_native_password')
cnx.close()