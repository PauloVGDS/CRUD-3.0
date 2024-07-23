import mysql.connector
import hmac, hashlib

#cnx = mysql.connector.connect(user='PauloV', password='Paulov1732', host='localhost', auth_plugin= 'mysql_native_password')
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
                                                  auth_plugin= self.auth_plugin, autocommit=True, database="crud")
        except mysql.connector.errors.Error as erro:
            print(f"A conexão falhou por causa: \t{erro}")
        finally:
            if self.connection.is_connected():
                print("Conexão realizada com sucesso!")
                return True
            return False

    def disconnect(self):
        try:
            self.connection.disconnect()
        except mysql.connector.errors.Error as erro:
            print(f"A desconexão falhou por causa: \n{erro}")
        finally:
            if not self.connection.is_connected():
                print("Desconectado com sucesso!")
                return True
            return False
        
    def create(self):
        try:
            if not self.connection.is_connected():
                print("Nenhum servidor encontrado!")
                return False
                
            cursor = self.connection.cursor()
            cursor.execute("""
                            CREATE TABLE usuarios(
                                id INT(5) PRIMARY KEY AUTO_INCREMENT, 
                                nome VARCHAR(30) NOT NULL, 
                                email VARCHAR(30) NOT NULL UNIQUE, 
                                senha VARCHAR(32) NOT NULL, 
                                birth DATE, 
                                genero ENUM('Masculino', 'Feminino'));
            """)
            print("Tabela criada com sucesso!")
            return True
        except mysql.connector.errors.Error as erro:
            print(f"Não foi possível criar a tabela: \t{erro}")
            return False

    def read(self, email):

        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s;", (email,))


    def update(self, email, option, answer):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE usuarios SET %s = %s WHERE email = %s;", (option, answer, email))
        return cursor

    def delete(self, email):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM usuarios WHERE email = %s", (email,))
        return cursor
    
    def insert(self, email):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        return cursor


db = dataControl("PauloV", "Paulov1732?", "localhost", "mysql_native_password")
db.connect()
db.create()
db.disconnect()




hashword = hmac.digest(key=b"Incansavel", msg=b"PauloVinicius", digest=hashlib.sha256)


password = hmac.digest(b"Incansavel", b"PauloV", hashlib.sha256)

if hmac.compare_digest(hashword , password):
    print(".")
else:
    print()
