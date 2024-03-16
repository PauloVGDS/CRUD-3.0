from customtkinter import *
from PIL import Image

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("CRUD 3.0")
        self.geometry("800x600")
        self.minsize(400, 400)
        self.maxsize(800, 600)

        self.login_frame = loginFrame(master=self)
        self.login_frame.pack(side=RIGHT, expand=True, fill=BOTH)
        self.image_frame = imageFrame(master=self)
        self.image_frame.pack(side=LEFT)
      

    @staticmethod
    def font(font="Dubai", size=15, weight="normal"):
        return CTkFont(family=font, size=size, weight=weight)
    
    @staticmethod
    def image(path, w, h):
        return CTkImage(Image.open(f"D:\Programas\Docs\Cursos\Python\CRUD 3.0\\{path}"), size=(w, h))



class loginFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)

        # Constantes
        self.TEXTCOLOR = "#ff3055"

        # Top Frame
        self.topFrame = CTkFrame(self, fg_color="black")
        self.firsTextFrame = CTkFrame(self.topFrame, fg_color="black")
        self.secondTextFrame = CTkFrame(self.topFrame, fg_color="black")
        self.firstText = CTkLabel(self.firsTextFrame, text="Bem vindo de volta!", font=App.font(size=40, weight="bold"), text_color=self.TEXTCOLOR)
        self.secondText = CTkLabel(self.secondTextFrame, text="Entre em sua conta.", font=App.font(size= 20), text_color=self.TEXTCOLOR)

        # Posicionando os frames do topo
        self.topFrame.pack(expand=True, fill=BOTH)
        self.secondTextFrame.pack(side=BOTTOM, fill=BOTH, padx=18)
        self.firsTextFrame.pack(side=BOTTOM, fill=BOTH, padx=18, ipady=0)
        self.firstText.pack(side=LEFT)
        self.secondText.pack(side=LEFT)


        # Middle Frame
        self.middleFrame = CTkFrame(self, fg_color="black")
        self.userEntryFrame = CTkFrame(self.middleFrame, fg_color="black")
        self.userEntryTextFrame = CTkFrame(self.userEntryFrame, fg_color="black")
        self.passwordEntryFrame = CTkFrame(self.middleFrame, fg_color="black")
        self.passwordEntryTextFrame = CTkFrame(self.passwordEntryFrame, fg_color="black")
        self.buttonFrame = CTkFrame(self.middleFrame, fg_color="black")

        # Widgets do frame do meio
        self.userEntryText = CTkLabel(self.userEntryTextFrame, text="Usuário", font=App.font(weight="bold"), text_color=self.TEXTCOLOR)
        self.userEntry = CTkEntry(self.userEntryFrame, fg_color='transparent', border_color=self.TEXTCOLOR)
        self.userImage = App.image("Person-icon.png",25,30)
        self.userLabel = CTkLabel(self.userEntryTextFrame, text=None,image=self.userImage)
        self.passwordImage = App.image("Lock-icon.png",25,30)
        self.passwordLabel = CTkLabel(self.passwordEntryTextFrame, text=None,image=self.passwordImage)
        self.passwordEntryText = CTkLabel(self.passwordEntryTextFrame, text="Senha", font=App.font(weight="bold"), text_color=self.TEXTCOLOR)
        self.passwordEntry = CTkEntry(self.passwordEntryFrame, fg_color='transparent', border_color=self.TEXTCOLOR)
        self.loginButton = CTkButton(self.middleFrame, text="Entrar", fg_color=self.TEXTCOLOR, hover_color="#4a1079", font=App.font(weight="bold"))
        self.registerButton = CTkButton(self.middleFrame, text="Registrar", fg_color=self.TEXTCOLOR, hover_color="#4a1079", font=App.font(weight="bold"))

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


        # Bottom Frame
        self.bottomFrame = CTkFrame(self, fg_color="black")

        # Posicionando o frame do fundo
        self.bottomFrame.pack(expand=True, fill=BOTH)



class imageFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.background = App.image("loginWallpaper.png", 400, 600)
        self.imageLabel = CTkLabel(self, text=None,image=self.background)
        self.imageLabel.pack()
    


  


app = App()
app.mainloop()