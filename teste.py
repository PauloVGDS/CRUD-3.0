from customtkinter import *
from PIL import Image

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
    def font(font="Dubai", size=15, weight="normal"):
        return CTkFont(family=font, size=size, weight=weight)
    
    @staticmethod
    def image(path, w, h):
        return CTkImage(Image.open(f"D:\Programas\Docs\Cursos\Python\CRUD 3.0\images\{path}"), size=(w, h))
    

    def background(self, path):
        self.backgroundImage = App.image(path, 400, 1080)

        self.image_frame = CTkFrame(self, bg_color="black")
        self.imageLabel = CTkLabel(self.image_frame, text=None,image=self.backgroundImage)
        self.image_frame.pack(side=LEFT)
        self.imageLabel.pack()
    
    def changeFrames(self):
        if str(self.__class__) in "<class '__main__.loginFrame'>":
            self.forget()
            currentFrame = registerFrame(self.master)
            currentFrame.pack(expand=True, fill=BOTH, anchor="center")
        else:
            self.forget()
            currentFrame = loginFrame(self.master)
            currentFrame.pack(expand=True, fill=BOTH, anchor="center")

class widgets(CTkBaseClass):

    def textContainer(master, text, fontSize=20, weight="normal", **kwargs):
        firsTextFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        firstText = CTkLabel(firsTextFrame, text=text, font=App.font(size=fontSize, weight=weight), text_color=CONTRSTEXTCOLOR)
        firstText.pack(side=LEFT)
        return firsTextFrame.pack(**kwargs)
    
    def inputContainer(master, text, placeholder, image, show, **kwargs):
        placeHolderColor = REGPLACEHOLDCOLOR
        borderColor = REGTEXTCOLOR
        if (str(master).startswith(".!loginframe") == True):
            placeHolderColor = LOGPLACEHOLDCOLOR
            borderColor = LOGTEXTCOLOR
        
        entryFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        entryTextFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        entryText = CTkLabel(entryTextFrame, text=text, font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        entry = CTkEntry(entryFrame, show=show,
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
        Button.pack()
        return buttonFrame.pack(**kwargs)

    def personInfoContainer():
        pass
class loginFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)

        # Definindo o background
        self.background = App.background(self, path="loginWallpaper.png")
        # Criação e posicionamento dos Widgets
        self.createWidgets()

    def createWidgets(self):
        # Main Frames
        self.topFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.middleFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.buttonFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)

        self.topFrame.pack(expand=True, fill=BOTH)
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)
        self.buttonFrame.pack(fill=X, padx=18)
        self.bottomFrame.pack(expand=True, fill=BOTH)


        widgets.textContainer(master=self.topFrame, text="Entre em sua conta.", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Bem vindo de volta!", fontSize=40, weight="bold", side=BOTTOM, fill=BOTH, padx=18, ipady=0)
        self.userinput = widgets.inputContainer(self.middleFrame, "Usuário", "Usuário", "Person-icon.png", show="", fill=X)
        self.passwordinput = widgets.inputContainer(self.middleFrame, "Senha", "Senha", "Lock-icon.png", show="*", fill=X)
        widgets.buttonContainer(self.buttonFrame, "Registrar",side=RIGHT, pady=5, cmd=lambda : App.changeFrames(self))
        widgets.buttonContainer(self.buttonFrame, "Entrar",side=LEFT, pady=5)




class registerFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)
        self.background = App.background(self, path="registerWallpaper.png")

        # Criação e posicionamento dos Widgets
        self.createWidgets()
        self.placeWidgets()


    def createWidgets(self):
        # Top Frame
        self.topFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.middleFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.buttonFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        self.buttonFrame.pack(fill=X, side=BOTTOM, pady=5)
    
        widgets.textContainer(master=self.topFrame, text="Preencha suas informações.", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Registre-se agora!", fontSize=40, weight="bold", side=BOTTOM, fill=BOTH, padx=18)

        self.nameInput = widgets.inputContainer(self.middleFrame, "Nome Completo", "Exemplo: Paulo Vinicius Gomes da Silva","Name-icon.png", show="", fill=X)
        self.emailInput = widgets.inputContainer(self.middleFrame, "Email", "example@gmail.com","Mail-icon.png", show="", fill=X)
        self.passwordInput = widgets.inputContainer(self.middleFrame, "Senha", "Senha","GreenLock-icon.png", show="*", fill=X)

        widgets.buttonContainer(self.buttonFrame, "Registrar", side=LEFT)
        widgets.buttonContainer(self.buttonFrame, "Voltar", side=RIGHT, cmd=lambda : App.changeFrames(self))

        # Informações pessoais
        self.personInfoFrame = CTkFrame(self.middleFrame, fg_color=BACKGNDCOLOR)
        # Data de nascimento
        self.bithdateEntryFrame = CTkFrame(self.personInfoFrame, fg_color=BACKGNDCOLOR)
        self.bithdateEntryTextFrame = CTkFrame(self.bithdateEntryFrame, fg_color=BACKGNDCOLOR)
        # Sexo
        self.genderEntryFrame = CTkFrame(self.personInfoFrame, fg_color=BACKGNDCOLOR)
        self.genderEntryTextFrame = CTkFrame(self.genderEntryFrame, fg_color=BACKGNDCOLOR)
        self.genderEntryContainer = CTkFrame(self.genderEntryFrame, 
                                             fg_color=BACKGNDCOLOR, border_color=REGTEXTCOLOR, border_width=2, 
                                             width=140, height=35)





        # Data de nascimento
        self.bithdateEntryText = CTkLabel(self.bithdateEntryTextFrame, text="Data de nascimento", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.bithdateEntry = CTkEntry(self.bithdateEntryFrame,
                                      font=App.font(weight="bold", size=12), placeholder_text="DD/MM/YYYY",
                                      fg_color='transparent', border_color=REGTEXTCOLOR,
                                      placeholder_text_color="#18664C")
        self.bithdateImage = CTkLabel(self.bithdateEntryTextFrame, text=None,image=App.image("Calendar-icon.png",25,30))
        
        # Gênero
        self.genderOptionText = CTkLabel(self.genderEntryTextFrame, text="Gênero", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        self.genderOption = CTkOptionMenu(self.genderEntryContainer, 
                                          dropdown_font=App.font(weight="bold", size=13), font=App.font(weight="bold"), 
                                          width=156, height=34, 
                                          fg_color=BACKGNDCOLOR, bg_color=REGTEXTCOLOR, text_color="#18664C",
                                          button_color=REGTEXTCOLOR, button_hover_color=REGHOVERCOLOR, 
                                          dropdown_fg_color=BACKGNDCOLOR, dropdown_text_color=REGTEXTCOLOR, dropdown_hover_color=REGHOVERCOLOR, 
                                          values=["Masculino", "Feminino", "Outro"])
        self.genderImage = CTkLabel(self.genderEntryTextFrame, text=None,image=App.image("Gender-icon.png",25,30))


        # Bottom Frame
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)


    def placeWidgets(self):

        self.topFrame.pack(expand=True, fill=BOTH, pady=5)
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)


        self.bithdateEntryTextFrame.pack(fill=X, pady=5)
        self.genderEntryTextFrame.pack(fill=X, pady=5)
        self.genderEntryContainer.pack(fill=X, ipady=2, ipadx=10)


        self.bithdateEntryFrame.pack(side=LEFT)
        self.genderEntryFrame.pack(side=RIGHT)
        self.personInfoFrame.pack(fill=X, pady=5)



        
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