from customtkinter import *
from PIL import Image
import re, os


LOGINTEXTCOLOR = "#ff3055"
CONTRSTEXTCOLOR = "white"
BACKGNDCOLOR = "black"
LOGHOVCOLOR = "#4a1079"
LOGPLACEHOLDCOLOR = "#7A1729"
REGPLACEHOLDCOLOR = "#18664c"
CHECKICONCOLOR = "#107e10"
CANCELICONCOLOR = "#c42b1c"
CURRENTPATH = os.path.dirname(os.path.realpath(__file__))

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("CRUD 3.0")
        self.geometry("800x600")
        self.minsize(800, 600)

        self.login_frame = loginFrame(master=self)
        self.login_frame.pack(expand=True, fill=BOTH, anchor="center")

    @staticmethod
    def font(font="Dubai", size=15, weight="normal"):
        return CTkFont(family=font, size=size, weight=weight)
    
    @staticmethod
    def image(path, w, h):
        return CTkImage(Image.open(rf"{CURRENTPATH}\images\{path}"), size=(w, h))
    

    def background(self, path):
        self.backgroundImage = App.image(path, 400, 1080)

        self.image_frame = CTkFrame(self, bg_color="black")
        self.imageLabel = CTkLabel(self.image_frame, text=None,image=self.backgroundImage)
        self.image_frame.pack(side=LEFT)
        self.imageLabel.pack()



class loginFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="black")

        # Definindo o background
        App.background(master, path="loginWallpaper.png")

        # Criação e posicionamento dos Widgets
        self.user = StringVar()
        self.password = StringVar()
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


        widgets.textContainer(master=self.topFrame, text="Entre em sua conta.", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Bem vindo de volta!", fontSize=38, weight="bold", side=BOTTOM, fill=BOTH, padx=18)
        self.userInput = widgets.inputContainer(self.middleFrame, "Usuário", "Usuário", "Person-icon.png", show="", output=self.user, fill=X)
        self.passwordInput = widgets.inputContainer(self.middleFrame, "Senha", "Senha", "Lock-icon.png", show="*", output=self.password, fill=X)
        self.warning = widgets.textContainer(master=self.buttonFrame, text="", textColor=CONTRSTEXTCOLOR, side=BOTTOM)

        widgets.buttonContainer(self.buttonFrame, "Registrar", side=RIGHT, cmd=lambda : App.changeFrames(self), pady = 34)
        widgets.buttonContainer(self.buttonFrame, "Entrar", side=LEFT, cmd= lambda : widgets.login(self, "Usuário/Senha Incorretos!", self.warning, self.userInput, self.passwordInput), pady = 34)



class registerFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="black")
        self.background = App.background(self, path="registerWallpaper.png")

        self.name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.birthdate = StringVar()
        self.gender = StringVar()

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
        self.buttonFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)

        self.topFrame.pack(expand=True, fill=BOTH, pady=30)
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)
        self.buttonFrame.pack(fill=X, padx=18)
        self.bottomFrame.pack(expand=True, fill=BOTH)
    
        widgets.textContainer(master=self.topFrame, text="Preencha suas informações.", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Registre-se agora!", fontSize=38, weight="bold", side=BOTTOM, fill=BOTH, padx=18)
        self.nameInput = widgets.inputContainer(self.middleFrame, "Nome Completo*", "Exemplo: Paulo Vinicius Gomes da Silva","Name-icon.png", show="", output=self.name, fill=X)
        self.emailInput = widgets.inputContainer(self.middleFrame, "Email*", "example@gmail.com","Mail-icon.png", show="", output=self.email, fill=X)
        self.passwordInput = widgets.inputContainer(self.middleFrame, "Senha*", "Senha","GreenLock-icon.png", show="*", output=self.password, fill=X)
        self.warning = widgets.textContainer(master=self.buttonFrame, text="", textColor=CONTRSTEXTCOLOR, side=BOTTOM)

        widgets.personInfoContainer(self.middleFrame, birthAnswer=self.birthdate, genderAnswer=self.gender)
        widgets.buttonContainer(self.buttonFrame, "Registrar", side=LEFT, pady=28, cmd=lambda : widgets.registro(self, "Preencha os campos obrigatórios!", self.warning, self.nameInput, self.emailInput, self.passwordInput))
        widgets.buttonContainer(self.buttonFrame, "Voltar", side=RIGHT, cmd=lambda : App.changeFrames(self), pady=28)
  


class adminFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="black")



class widgets:

    def textContainer(master, text, fontSize=20, weight="normal", textColor = CONTRSTEXTCOLOR, **kwargs):
        firsTextFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        firstText = CTkLabel(firsTextFrame, text=text, font=App.font(size=fontSize, weight=weight), text_color=textColor, corner_radius=5)
        firstText.pack(side=LEFT)
        firsTextFrame.pack(**kwargs)
        return firstText
    
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
        textLabel = CTkLabel(entryTextFrame, text=None, image=App.image(image, 25, 30))
        imageLabel = CTkLabel(entryTextFrame, text=None)

        entryTextFrame.pack(fill=X, pady=5)
        textLabel.pack(side=LEFT)
        entryText.pack(side=LEFT, padx=5)
        entry.pack(fill=X, ipady=5)
        imageLabel.pack(side=RIGHT)
        entryFrame.pack(**kwargs)
        return imageLabel

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
                                      fg_color='transparent', border_color=REGTEXTCOLOR,
                                      placeholder_text_color="#18664C", textvariable=birthAnswer)
        birthdateImage = CTkLabel(birthdateEntryTextFrame, text=None,image=App.image("Calendar-icon.png",25,30))

        genderOptionText = CTkLabel(genderEntryTextFrame, text="Gênero", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        genderOption = CTkComboBox(genderEntryFrame, 
                                          dropdown_font=App.font(weight="bold", size=13), font=App.font(weight="bold"), 
                                          width=160, height=39, 
                                          fg_color=BACKGNDCOLOR, text_color="#18664C", border_color=REGTEXTCOLOR,
                                          button_color=REGTEXTCOLOR, button_hover_color=REGHOVERCOLOR, 
                                          dropdown_fg_color=BACKGNDCOLOR, dropdown_text_color=REGTEXTCOLOR, dropdown_hover_color=REGHOVERCOLOR, 
                                          values=["Masculino", "Feminino", "Outro"], variable=genderAnswer)
        genderImage = CTkLabel(genderEntryTextFrame, text=None,image=App.image("Gender-icon.png",25,30))

        birthdateEntryTextFrame.pack(fill=X, pady=5)
        genderEntryTextFrame.pack(fill=X, pady=5)
        birthdateEntryFrame.pack(side=LEFT)
        genderEntryFrame.pack(side=RIGHT)
        personInfoFrame.pack(fill=X, pady=5)
        birthdateImage.pack(side=LEFT)
        birthdateEntryText.pack(side=LEFT, padx=5)
        birthdateEntry.pack(fill=X, ipady=5)
        genderImage.pack(side=LEFT)
        genderOptionText.pack(side=LEFT)
        genderOption.pack()

    def login(master, texto, var, *args):
        if (master.user.get() == "") or (master.password.get() == ""):  
            for el in args:
                el.configure(image=App.image("Cancel_icon.png", 25, 25))    

            var.configure(fg_color=CANCELICONCOLOR)
            var.configure(text_color = CONTRSTEXTCOLOR)
            var.configure(text = texto)
            return master.update()
        
        for el in args:
            el.configure(image=App.image("Check_icon.png", 25, 25))

        var.configure(fg_color=CHECKICONCOLOR)
        var.configure(text_color = CONTRSTEXTCOLOR)
        var.configure(text = "Conectado!")
        master.update()
        
    def registro(master, texto, var, *args):
            if (master.name.get() == "") or (master.email.get() == "") or (master.password.get() == ""):
                
                if re.search(r"^[A-Za-z]{,5}$", master.name.get()):
                    args[0].configure(image=App.image("Cancel_icon.png", 25, 25))    
                else:
                    args[0].configure(image=App.image("Check_icon.png", 25, 25))  

                if re.search(r"^[a-zA-Z0-9.-_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", master.email.get()):
                    args[1].configure(image=App.image("Check_icon.png", 25, 25))
                else:
                    args[1].configure(image=App.image("Cancel_icon.png", 25, 25))    
                
                if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*?~])[A-Za-z0-9!@#$%^&*?~]{8,}$", master.password.get()): # {mínimo, máximo}
                    args[2].configure(image=App.image("Check_icon.png", 25, 25))  
                else:
                    args[2].configure(image=App.image("Cancel_icon.png", 25, 25))  
                var.configure(fg_color=CANCELICONCOLOR)
                var.configure(text_color = CONTRSTEXTCOLOR)
                var.configure(text = texto)
                return master.update()
            
            # Data de nascimento formatada corretamente
            if re.search(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", master.birthdate.get()):
                pass

            for el in args:
                el.configure(image=App.image("Check_icon.png", 25, 25))
            var.configure(fg_color=CHECKICONCOLOR)
            var.configure(text_color = CONTRSTEXTCOLOR)
            var.configure(text = "Registrado!")
            print(f"Nome: {master.name.get()}\nEmail: {master.email.get()}\nSenha: {master.password.get()}\nData de Nascimento: {master.birthdate.get()}\nGênero: {master.gender.get()}")
            return master.update()


class dataControl:
    def __init__(self, db_name):
        pass
    
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


app = App()
app.mainloop()