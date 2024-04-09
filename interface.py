from customtkinter import *
from PIL import Image

LOGINTEXTCOLOR = "#ff3055"
CONTRSTEXTCOLOR = "white"
BACKGNDCOLOR = "black"
LOGHOVCOLOR = "#4a1079"
LOGPLACEHOLDCOLOR = "#7A1729"
REGISTERTEXTCOLOR = "#33dba3"
REGHOVERCOLOR = "#3160ac"


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("CRUD 3.0")
        self.geometry("800x600")
        self.minsize(800, 600)

        self.login_frame = loginFrame(master=self)
        self.login_frame.pack(expand=True, fill=BOTH, anchor="center")

    @staticmethod
    def font(font="Titillium Web Semibold", size=15, weight="normal"):
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



class loginFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)
        # Definindo o background
        App.background(master, path="loginWallpaper.png")

        # Criação e posicionamento dos Widgets
        self.createWidgets()
        self.placeWidgets()

    def createWidgets(self):
        # Top Frame
        self.topFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.firsTextFrame = CTkFrame(self.topFrame, fg_color=BACKGNDCOLOR)
        self.secondTextFrame = CTkFrame(self.topFrame, fg_color=BACKGNDCOLOR)
        self.firstText = CTkLabel(self.firsTextFrame, 
                                    text="Bem vindo de volta!", font=App.font(size=40, weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.secondText = CTkLabel(self.secondTextFrame, 
                                    text="Entre em sua conta.", font=App.font(size= 20), text_color=CONTRSTEXTCOLOR)

        # Middle Frame
        self.middleFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.userEntryFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        self.userEntryTextFrame = CTkFrame(self.userEntryFrame, fg_color=BACKGNDCOLOR)
        self.passwordEntryFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        self.passwordEntryTextFrame = CTkFrame(self.passwordEntryFrame, fg_color=BACKGNDCOLOR)
        self.buttonFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)

        # Widgets do frame do meio
        self.userEntryText = CTkLabel(self.userEntryTextFrame, 
                                      text="Usuário", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.userEntry = CTkEntry(self.userEntryFrame, 
                                  fg_color='transparent', border_color=LOGINTEXTCOLOR,
                                  placeholder_text="Usuário", placeholder_text_color=LOGPLACEHOLDCOLOR)
        self.userImage = App.image("Person-icon.png",25,30)
        self.userLabel = CTkLabel(self.userEntryTextFrame, 
                                  text=None, image=self.userImage)
        self.passwordImage = App.image("Lock-icon.png",25,30)
        self.passwordLabel = CTkLabel(self.passwordEntryTextFrame, 
                                      text=None, image=self.passwordImage)
        self.passwordEntryText = CTkLabel(self.passwordEntryTextFrame, 
                                          text="Senha", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.passwordEntry = CTkEntry(self.passwordEntryFrame, 
                                      fg_color='transparent', border_color=LOGINTEXTCOLOR,
                                      placeholder_text="Senha", placeholder_text_color=LOGPLACEHOLDCOLOR)
        self.loginButton = CTkButton(self.middleFrame, 
                                     text="Entrar", font=App.font(weight="bold"), 
                                     fg_color=LOGINTEXTCOLOR, hover_color=LOGHOVCOLOR)
        self.registerButton = CTkButton(self.middleFrame, 
                                        text="Registrar", font=App.font(weight="bold"), 
                                        fg_color=LOGINTEXTCOLOR, hover_color=LOGHOVCOLOR)

        # Bottom Frame
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)

    def placeWidgets(self):
        # Posicionando os frames do topo
        self.topFrame.pack(expand=True, fill=BOTH)
        self.secondTextFrame.pack(side=BOTTOM, fill=BOTH, padx=18)
        self.firsTextFrame.pack(side=BOTTOM, fill=BOTH, padx=18, ipady=0)
        self.firstText.pack(side=LEFT)
        self.secondText.pack(side=LEFT)

        # Posicionando os frames do meio
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)
        self.userEntryFrame.pack(fill=X)
        self.passwordEntryFrame.pack(fill=X)
        self.userEntryTextFrame.pack(fill=X, pady=5)
        self.passwordEntryTextFrame.pack(fill=X, pady=5)
        
        # Posicionando os widgets nos frames
        self.registerButton.pack(side=LEFT, pady=5)
        self.loginButton.pack(side=RIGHT, pady=5)
        self.passwordLabel.pack(side=LEFT)
        self.passwordEntryText.pack(side=LEFT, padx=5)
        self.userLabel.pack(side=LEFT)
        self.passwordEntry.pack(fill=X, ipady=5)
        self.userEntryText.pack(side=LEFT, padx=5)
        self.userEntry.pack(fill=X, ipady=5)
        
        # Posicionando o frame do fundo
        self.bottomFrame.pack(expand=True, fill=BOTH)



class registerFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)

        # Constantes
        
        
        App.background(master, path="registerWallpaper.png")

        # Criação e posicionamento dos Widgets
        self.createWidgets()
        self.placeWidgets()


    def createWidgets(self):
        # Top Frame
        self.topFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.firsTextFrame = CTkFrame(self.topFrame, fg_color=BACKGNDCOLOR)
        self.secondTextFrame = CTkFrame(self.topFrame, fg_color=BACKGNDCOLOR)
        self.firstText = CTkLabel(self.firsTextFrame, 
                                  text="Registre-se agora!", font=App.font(size=40, weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.secondText = CTkLabel(self.secondTextFrame, 
                                   text="Preencha suas informações.", font=App.font(size= 20), text_color=CONTRSTEXTCOLOR)

        # Middle Frame
        self.middleFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        # Nome
        self.nameEntryFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        self.nameEntryTextFrame = CTkFrame(self.nameEntryFrame, fg_color=BACKGNDCOLOR)
        # Email
        self.emailEntryFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        self.emailEntryTextFrame = CTkFrame(self.emailEntryFrame, fg_color=BACKGNDCOLOR)
        # Senha
        self.passwordEntryFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        self.passwordEntryTextFrame = CTkFrame(self.passwordEntryFrame, fg_color=BACKGNDCOLOR)
        # Informações da pessoais
        self.personInfoFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        # Data de nascimento
        self.bithdateEntryFrame = CTkFrame(self.personInfoFrame, fg_color=BACKGNDCOLOR)
        self.bithdateEntryTextFrame = CTkFrame(self.bithdateEntryFrame, fg_color=BACKGNDCOLOR)
        # Sexo
        self.genderEntryFrame = CTkFrame(self.personInfoFrame, fg_color=BACKGNDCOLOR)
        self.genderEntryTextFrame = CTkFrame(self.genderEntryFrame, fg_color=BACKGNDCOLOR)
        self.genderEntryContainer = CTkFrame(self.genderEntryFrame, 
                                             fg_color=BACKGNDCOLOR, border_color=REGISTERTEXTCOLOR, border_width=2, 
                                             width=140, height=35)

        # Botão
        self.buttonFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)

        # Widgets do frame do meio
        # Nome
        self.nameEntryText = CTkLabel(self.nameEntryTextFrame, text="Nome Completo", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.nameEntry = CTkEntry(self.nameEntryFrame, 
                                  placeholder_text="Exemplo: Paulo Vinicius Gomes Silva", placeholder_text_color="#18664C", 
                                  fg_color='transparent', border_color=REGISTERTEXTCOLOR)
        self.nameImage = CTkLabel(self.nameEntryTextFrame, text=None,image=App.image("Name-icon.png",25,30))
        # Email
        self.emailEntryText = CTkLabel(self.emailEntryTextFrame, text="Email", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.emailEntry = CTkEntry(self.emailEntryFrame,
                                   placeholder_text="example@gmail.com", placeholder_text_color="#18664C", 
                                   fg_color='transparent', border_color=REGISTERTEXTCOLOR)
        self.emailImage = CTkLabel(self.emailEntryTextFrame, text=None, image=App.image("Mail-icon.png",25,30))
        # Senha
        self.passwordEntryText = CTkLabel(self.passwordEntryTextFrame, text="Senha", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.passwordEntry = CTkEntry(self.passwordEntryFrame, 
                                      show="*", placeholder_text="Senha", placeholder_text_color="#18664C",
                                      fg_color='transparent', border_color=REGISTERTEXTCOLOR)
        self.passwordImage = CTkLabel(self.passwordEntryTextFrame, text=None,image=App.image("GreenLock-icon.png",25,30))

        # Data de nascimento
        self.bithdateEntryText = CTkLabel(self.bithdateEntryTextFrame, text="Data de nascimento", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.bithdateEntry = CTkEntry(self.bithdateEntryFrame,
                                      font=App.font(weight="bold", size=12), placeholder_text="DD/MM/YYYY",
                                      fg_color='transparent', border_color=REGISTERTEXTCOLOR,
                                      placeholder_text_color="#18664C")
        self.bithdateImage = CTkLabel(self.bithdateEntryTextFrame, text=None,image=App.image("Calendar-icon.png",25,30))
        
        # Gênero
        self.genderOptionText = CTkLabel(self.genderEntryTextFrame, text="Gênero", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.genderOption = CTkOptionMenu(self.genderEntryContainer, 
                                          dropdown_font=App.font(weight="bold", size=13), font=App.font(weight="bold"), 
                                          width=156, height=34, 
                                          fg_color=BACKGNDCOLOR, bg_color=REGISTERTEXTCOLOR, text_color="#18664C",
                                          button_color=REGISTERTEXTCOLOR, button_hover_color=REGHOVERCOLOR, 
                                          dropdown_fg_color=BACKGNDCOLOR, dropdown_text_color=REGISTERTEXTCOLOR, dropdown_hover_color=REGHOVERCOLOR, 
                                          values=["Masculino", "Feminino", "Outro"])
        self.genderImage = CTkLabel(self.genderEntryTextFrame, text=None,image=App.image("Gender-icon.png",25,30))




        # Botões
        self.loginButton = CTkButton(self.buttonFrame, 
                                     font=App.font(weight="bold"), text="Voltar", 
                                     fg_color=REGISTERTEXTCOLOR, hover_color=REGHOVERCOLOR, text_color="black")
        self.registerButton = CTkButton(self.buttonFrame, 
                                        font=App.font(weight="bold"), text="Registrar", 
                                        fg_color=REGISTERTEXTCOLOR, hover_color=REGHOVERCOLOR, text_color="black")

        # Bottom Frame
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)


    def placeWidgets(self):
        # Posicionando os frames do topo
        self.topFrame.pack(expand=True, fill=BOTH, pady=5)
        self.secondTextFrame.pack(side=BOTTOM, fill=BOTH, padx=18)
        self.firsTextFrame.pack(side=BOTTOM, fill=BOTH, padx=18)
        self.firstText.pack(side=LEFT)
        self.secondText.pack(side=LEFT)

        # Posicionando os frames do meio
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)
        self.nameEntryTextFrame.pack(fill=X, pady=5)
        self.emailEntryTextFrame.pack(fill=X, pady=5)
        self.passwordEntryTextFrame.pack(fill=X, pady=5)
        self.bithdateEntryTextFrame.pack(fill=X, pady=5)
        self.genderEntryTextFrame.pack(fill=X, pady=5)
        self.genderEntryContainer.pack(fill=X, ipady=2, ipadx=10)

        self.nameEntryFrame.pack(fill=X)
        self.emailEntryFrame.pack(fill=X)
        self.passwordEntryFrame.pack(fill=X)
        self.bithdateEntryFrame.pack(side=LEFT)
        self.genderEntryFrame.pack(side=RIGHT)
        self.personInfoFrame.pack(fill=X, pady=5)
        self.buttonFrame.pack(fill=X, pady=5)

        # Posicionando os widgets nos frames
        self.loginButton.pack(side=LEFT, pady=15)
        self.registerButton.pack(side=RIGHT, pady=15)

        self.nameImage.pack(side=LEFT)
        self.nameEntryText.pack(side=LEFT, padx=5)
        self.nameEntry.pack(fill=X, ipady=5)

        self.emailImage.pack(side=LEFT)
        self.emailEntryText.pack(side=LEFT, padx=5)
        self.emailEntry.pack(fill=X, ipady=5)

        self.passwordImage.pack(side=LEFT)
        self.passwordEntryText.pack(side=LEFT, padx=5)
        self.passwordEntry.pack(fill=X, ipady=5)
        
        self.bithdateImage.pack(side=LEFT)
        self.bithdateEntryText.pack(side=LEFT, padx=5)
        self.bithdateEntry.pack(fill=X, ipady=5)
        
        self.genderImage.pack(side=LEFT)
        self.genderOptionText.pack(side=LEFT)
        self.genderOption.place(x=2, y=2)
        # Posicionando o frame do fundo
        self.bottomFrame.pack(expand=True, fill=BOTH)




  


app = App()
app.mainloop()