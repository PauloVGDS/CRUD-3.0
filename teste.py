import mysql.connector

#cnx = mysql.connector.connect(user='PauloV', password='Paulov1732',
#                              host='localhost',
#                              auth_plugin= 'mysql_native_password')
#cnx.close()


class dataControl:
    def __init__(self, user, password, host, auth_plugin):
        self.user = user
        self.password = password
        self.host = host
        self.auth_plugin = auth_plugin

    def connect(self):
        try: 
            self.connection = mysql.connector.connect(user=self.user, 
                                                  password=self.password, 
                                                  host=self.host, 
                                                  auth_plugin= self.auth_plugin, autocommit=True)
            if self.connection.is_connected():
                print("Conexão realizada com sucesso!")
        except mysql.connector.errors.Error as erro:
            print(f"A conexão falhou por causa: \t{erro}")
        

    def disconnect(self):
        try:
            self.connection.disconnect()
            if not self.connection.is_connected():
                print("Desconectado com sucesso!")
        except mysql.connector.errors.Error as erro:
            print(f"A desconexão falhou por causa: \n{erro}")

    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def insert(self):
        pass


db = dataControl("PauloV", "Paulov1732?", "localhost", "mysql_native_password")
db.connect()
db.disconnect()