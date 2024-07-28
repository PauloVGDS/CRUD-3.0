import mysql.connector
import hmac, hashlib


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
        try:
            cursor = self.connection.cursor(buffered=True)
            cursor.execute("SELECT * FROM usuarios WHERE email = %s;", (email,))
            answer = cursor.fetchone()
            if answer == None:
                raise mysql.connector.errors.Error
            return answer
        except mysql.connector.errors.Error as erro:
            print(f"Não foi possível concluir a operação: {erro}")
            return False

    def update(self, email, option, answer):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE usuarios SET %s = %s WHERE email = %s;", (option, answer, email))
            return True
        except mysql.connector.errors.Error as erro:
            print(f"Não foi possível concluir a operação: {erro}")
            return False


    def delete(self, email):
        try:
            erro = None
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM usuarios WHERE email = %s", (email,))
        except mysql.connector.errors.Error as erro:
            print(f"Não foi possível concluír a operação: {erro}")
            return False
        
        finally:
            if erro == None:
                return True
            return False
    
    def insert(self, nome, email, senha, birth="", genero=""):
        try:
            key = br"\x87\xcax\xd2\xa9\xc6\xad\xcc\xc6\xeds]\x8d\xdb>\x18\xa9]\xcd\xf3!\x00\xecM\xc6\xfb\xc4\xd4\xb3\xb0C\x1b"
            hashword = hmac.digest(key=key, msg=senha.encode(), digest=hashlib.sha256)
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email, senha, birth, genero) VALUES (%s, %s, %s, %s, %s);", (nome, email, hashword, birth, genero))

        except mysql.connector.errors.Error as erro:
            print(f"Não foi possível inserir os dados por causa: \t{erro}")
            return False
        finally:
            if erro == None:
                return True
            return False


db = dataControl("PauloV", "Paulov1732?", "localhost", "mysql_native_password")
db.connect()
#db.insert("Paulo Vinicius Gomes da Silva", "teste2@gmail.com", "PauloV123")
print(db.read(""))
db.disconnect()



teste = "Paulo"
hashword = hmac.digest(key=br"\x87\xcax\xd2\xa9\xc6\xad\xcc\xc6\xeds]\x8d\xdb>\x18\xa9]\xcd\xf3!\x00\xecM\xc6\xfb\xc4\xd4\xb3\xb0C\x1b", msg=teste.encode(), digest=hashlib.sha256)
password = hmac.digest(br"\x87\xcax\xd2\xa9\xc6\xad\xcc\xc6\xeds]\x8d\xdb>\x18\xa9]\xcd\xf3!\x00\xecM\xc6\xfb\xc4\xd4\xb3\xb0C\x1b", b"Paulo", hashlib.sha256)

#if hmac.compare_digest(hashword , password):
#    print(True)
#else:
#    print(False)


