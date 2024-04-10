from customtkinter import *
from PIL import Image
import sqlite3

BACKGNDCOLOR = "black"
CONTRSTEXTCOLOR = "white"
LOGTEXTCOLOR = "#ff3055"
REGTEXTCOLOR = "#33dba3"
LOGHOVERCOLOR = "#4a1079"
REGHOVERCOLOR = "#3160ac"
LOGPLACEHOLDCOLOR = "#7A1729"
REGPLACEHOLDCOLOR = "#18664c"


class App(CTk):
    def __init__(self, master=None):
        super().__init__()
        self.title("CRUD 3.0")
        self.geometry("800x600")
        self.minsize(800, 600)
        self.currentFrame = loginFrame(master=self)
        self.currentFrame.pack(expand=True, fill=BOTH, anchor="center")

    @staticmethod
    def font(font="Titillium Web", size=15, weight="normal"):
        return CTkFont(family=font, size=size, weight=weight)
    
    @staticmethod
    def image(path, w, h):
        return CTkImage(Image.open(fr"D:\Programas\Docs\Cursos\Python\CRUD 3.0\images\{path}"), size=(w, h))
    

    def background(self, path):
        self.backgroundImage = App.image(path, 400, 1080)

        self.image_frame = CTkFrame(self, bg_color="black")
        self.imageLabel = CTkLabel(self.image_frame, text=None,image=self.backgroundImage)
        self.image_frame.pack(side=LEFT)
        self.imageLabel.pack()
    
    def changeFrames(self):
        print(self.__class__)
        if str(self.__class__) == "<class '__main__.loginFrame'>":
            self.forget()
            currentFrame = registerFrame(self.master)
            currentFrame.pack(expand=True, fill=BOTH, anchor="center")

        self.forget()
        currentFrame = loginFrame(self.master)
        currentFrame.pack(expand=True, fill=BOTH, anchor="center")


    
class loginFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)

        # Definindo o background
        self.background = App.background(self, path="loginWallpaper.png")
        # Criação e posicionamento dos Widgets
        self.user = StringVar()
        self.password = StringVar()
        self.createWidgets()

    def createWidgets(self):
        # Main Frames
        self.topFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.middleFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.buttonFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)

        self.topFrame.pack(expand=True, fill=BOTH, pady=30)
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)
        self.buttonFrame.pack(fill=X, padx=18)
        self.bottomFrame.pack(expand=True, fill=BOTH)


        widgets.textContainer(master=self.topFrame, text="Entre em sua conta.", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Bem vindo de volta!", fontSize=38, weight="bold", side=BOTTOM, fill=BOTH, padx=18, ipady=0)
        widgets.inputContainer(self.middleFrame, "Usuário", "Usuário", "Person-icon.png", show="", output=self.user, fill=X)
        widgets.inputContainer(self.middleFrame, "Senha", "Senha", "Lock-icon.png", show="*", output=self.password, fill=X)
        widgets.buttonContainer(self.buttonFrame, "Registrar",side=RIGHT, pady=5, cmd=lambda : App.changeFrames(self))
        widgets.buttonContainer(self.buttonFrame, "Entrar",side=LEFT, pady=34)



class registerFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)
        self.background = App.background(self, path="registerWallpaper.png")

        self.name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.birthdate = StringVar()
        self.gender = StringVar()

        self.createWidgets()


    def createWidgets(self):
        # Top Frame
        self.topFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.middleFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.buttonFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)

        self.topFrame.pack(expand=True, fill=BOTH, pady=30)
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)
        self.buttonFrame.pack(fill=X, padx=18)
        self.bottomFrame.pack(expand=True, fill=BOTH)
    
        widgets.textContainer(master=self.topFrame, text="Preencha suas informações.", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Registre-se agora!", fontSize=38, weight="bold", side=BOTTOM, fill=BOTH, padx=18)
        self.nameInput = widgets.inputContainer(self.middleFrame, "Nome Completo", "Exemplo: Paulo Vinicius Gomes da Silva","Name-icon.png", show="", output=self.name, fill=X)
        self.emailInput = widgets.inputContainer(self.middleFrame, "Email", "example@gmail.com","Mail-icon.png", show="", output=self.email, fill=X)
        self.passwordInput = widgets.inputContainer(self.middleFrame, "Senha", "Senha","GreenLock-icon.png", show="*", output=self.password, fill=X)
        widgets.personInfoContainer(self.middleFrame, birthAnswer=self.birthdate, genderAnswer=self.gender)
        widgets.buttonContainer(self.buttonFrame, "Registrar", side=LEFT, pady=34)
        widgets.buttonContainer(self.buttonFrame, "Voltar", side=RIGHT, cmd=lambda : App.changeFrames(self), pady=10)

  

class widgets:

    def textContainer(master, text, fontSize=20, weight="normal", **kwargs):
        firsTextFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        firstText = CTkLabel(firsTextFrame, text=text, font=App.font(size=fontSize, weight=weight), text_color=CONTRSTEXTCOLOR)
        firstText.pack(side=LEFT)
        return firsTextFrame.pack(**kwargs)
    
    def inputContainer(master, text, placeholder, image, show, output=None, **kwargs):
        placeHolderColor = REGPLACEHOLDCOLOR
        borderColor = REGTEXTCOLOR
        if (str(master).startswith(".!loginframe") == True):
            placeHolderColor = LOGPLACEHOLDCOLOR
            borderColor = LOGTEXTCOLOR
        
        entryFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        entryTextFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        entryText = CTkLabel(entryTextFrame, text=text, font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        entry = CTkEntry(entryFrame, show=show, textvariable=output,
                                  fg_color='transparent', border_color=borderColor,
                                  placeholder_text=placeholder, placeholder_text_color=placeHolderColor)
        image = App.image(image, 25, 30)
        label = CTkLabel(entryTextFrame, text=None, image=image)

        entryTextFrame.pack(fill=X, pady=5)
        label.pack(side=LEFT)
        entryText.pack(side=LEFT, padx=5)
        entry.pack(fill=X, ipady=5)
        entryFrame.pack(**kwargs)

    def buttonContainer(master, text, cmd=None, **kwargs):
        fgColor = LOGTEXTCOLOR
        hoverColor = LOGHOVERCOLOR
        textColor = "white"
        if (str(master).startswith(".!registerframe") == True):
            fgColor = REGTEXTCOLOR
            hoverColor = REGHOVERCOLOR
            textColor = "black"
            
        buttonFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        Button = CTkButton(buttonFrame, text=text, font=App.font(weight="bold"), fg_color=fgColor, hover_color=hoverColor, text_color=textColor, command=cmd)
        Button.pack(ipady=2)
        return buttonFrame.pack(**kwargs)

    def personInfoContainer(master, genderAnswer, birthAnswer):
        # Widget exclusivo da janela de registro
        personInfoFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        birthdateEntryFrame = CTkFrame(personInfoFrame, fg_color=BACKGNDCOLOR)
        birthdateEntryTextFrame = CTkFrame(birthdateEntryFrame, fg_color=BACKGNDCOLOR)
        genderEntryFrame = CTkFrame(personInfoFrame, fg_color=BACKGNDCOLOR)
        genderEntryTextFrame = CTkFrame(genderEntryFrame, fg_color=BACKGNDCOLOR)
        genderEntryContainer = CTkFrame(genderEntryFrame, 
                                             fg_color=BACKGNDCOLOR, border_color=REGTEXTCOLOR, border_width=2, 
                                             width=140, height=35)

        birthdateEntryText = CTkLabel(birthdateEntryTextFrame, text="Data de nascimento", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        birthdateEntry = CTkEntry(birthdateEntryFrame,
                                      font=App.font(weight="bold", size=12), placeholder_text="DD/MM/YYYY",
                                      fg_color='transparent', border_color=REGTEXTCOLOR,
                                      placeholder_text_color="#18664C", textvariable=birthAnswer)
        birthdateImage = CTkLabel(birthdateEntryTextFrame, text=None,image=App.image("Calendar-icon.png",25,30))
        genderOptionText = CTkLabel(genderEntryTextFrame, text="Gênero", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        genderOption = CTkOptionMenu(genderEntryContainer, 
                                          dropdown_font=App.font(weight="bold", size=13), font=App.font(weight="bold"), 
                                          width=156, height=34, 
                                          fg_color=BACKGNDCOLOR, bg_color=REGTEXTCOLOR, text_color="#18664C",
                                          button_color=REGTEXTCOLOR, button_hover_color=REGHOVERCOLOR, 
                                          dropdown_fg_color=BACKGNDCOLOR, dropdown_text_color=REGTEXTCOLOR, dropdown_hover_color=REGHOVERCOLOR, 
                                          values=["Masculino", "Feminino", "Outro"], variable=genderAnswer)
        genderImage = CTkLabel(genderEntryTextFrame, text=None,image=App.image("Gender-icon.png",25,30))

        birthdateEntryTextFrame.pack(fill=X, pady=5)
        genderEntryTextFrame.pack(fill=X, pady=5)
        genderEntryContainer.pack(fill=X, ipady=2, ipadx=10)
        birthdateEntryFrame.pack(side=LEFT)
        genderEntryFrame.pack(side=RIGHT)
        personInfoFrame.pack(fill=X, pady=5)
        birthdateImage.pack(side=LEFT)
        birthdateEntryText.pack(side=LEFT, padx=5)
        birthdateEntry.pack(fill=X, ipady=5)
        genderImage.pack(side=LEFT)
        genderOptionText.pack(side=LEFT)
        genderOption.place(x=2, y=2)



class sqlControlClass:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            if not (self.conn.total_changes):
                print("Conexão bem sucedida!")
        except Exception as error:
            print(f"Erro em: {error}")

    def create(self):
        try:
            self.cursor.execute("CREATE TABLE cadastros (ID INT PRIMARY KEY, Nome VARCHAR(100), Nascionalidade VARCHAR(15), Cidade VARCHAR(50));")
        except Exception as error:
            print(f"Erro: {error}")

    def read(self):
        try:
            self.cursor.execute("SELECT * FROM cadastros")
        except Exception as error:
            print(f"Erro: {error}")
        finally:
            self.cursor.close()

    def delete(self, Id):
        try:
            self.cursor.execute("DELETE FROM cadastros WHERE ID = ?", (Id))
        except Exception as error:
            print(f"Erro: {error}")
        finally:
            self.cursor.close()

    def insert(self, nome, nascionalidade, cidade):
        try:
            self.cursor.execute("INSERT INTO Estudantes (ID, Nome, Nascionalidade, Cidade) VALUES (?, ?, ?);", (nome, nascionalidade, cidade))
        except Exception as error:
            print(f"Erro: {error}")
        finally:
            self.cursor.close()

sqlControlClass("database.db")


# app = App()
# app.mainloop()