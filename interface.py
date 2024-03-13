from customtkinter import *
from PIL import Image

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title="CRUD"
        self.geometry("800x600")
        self.minsize(400, 400)
        self.maxsize(800, 600)


        self.login_frame = loginFrame(master=self)
        self.login_frame.pack(side="right", expand=True, fill="both")
        self.image_frame = imageFrame(master=self)
        self.image_frame.pack(side="left")
      

class loginFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)
        self.topFrame = CTkFrame(self, fg_color="black")
        self.firsTextFrame = CTkFrame(self.topFrame, fg_color="black")
        self.secondTextFrame = CTkFrame(self.topFrame, fg_color="black")
        self.firstText = CTkLabel(self.firsTextFrame, text="Bem vindo de volta!", font=CTkFont(family="Dubai", size=40, weight="bold"), text_color="#ff3055")
        self.secondText = CTkLabel(self.secondTextFrame, text="Entre em sua conta.", font=CTkFont(family="Dubai", size=20, weight="normal"), text_color="#ff3055")
        self.topFrame.pack(expand=True, fill="both")
        self.secondTextFrame.pack(side="bottom", fill="both", padx=18)
        self.firsTextFrame.pack(side="bottom", fill="both", padx=18)
        self.firstText.pack(side="left")
        self.secondText.pack(side="left")




        self.middleFrame = CTkFrame(self, fg_color="black")
        self.userEntryFrame = CTkFrame(self.middleFrame, fg_color="black")
        self.userEntryTextFrame = CTkFrame(self.userEntryFrame, fg_color="black")
        self.passwordEntryFrame = CTkFrame(self.middleFrame, fg_color="black")
        self.passwordEntryTextFrame = CTkFrame(self.passwordEntryFrame, fg_color="black")
        self.buttonFrame = CTkFrame(self.middleFrame, fg_color="black")


        self.userEntryText = CTkLabel(self.userEntryTextFrame, text="Usuário", font=CTkFont("Dubai", size=15, weight="bold"), text_color="#ff3055")
        self.userEntry = CTkEntry(self.userEntryFrame, fg_color='transparent', border_color="#ff3055")
        self.userImage = CTkImage(Image.open("D:\Programas\Docs\Cursos\Python\CRUD 3.0\Person-icon.png"), size=(22,22))
        self.userLabel = CTkLabel(self.userEntryTextFrame, text=None,image=self.userImage)
        self.passwordImage = CTkImage(Image.open("D:\Programas\Docs\Cursos\Python\CRUD 3.0\Lock-icon.png"), size=(22,22))
        self.passwordLabel = CTkLabel(self.passwordEntryTextFrame, text=None,image=self.passwordImage)
        self.passwordEntryText = CTkLabel(self.passwordEntryTextFrame, text="Senha", font=CTkFont("Dubai", size=15, weight="bold"), text_color="#ff3055")
        self.passwordEntry = CTkEntry(self.passwordEntryFrame, fg_color='transparent', border_color="#ff3055")
        self.loginButton = CTkButton(self.middleFrame, text="Entrar", fg_color="#ff3055", hover_color="#4a1079", font=CTkFont("Dubai", size=15, weight="bold"))
        self.registerButton = CTkButton(self.middleFrame, text="Registrar", fg_color="#ff3055", hover_color="#4a1079", font=CTkFont("Dubai", size=15, weight="bold"))

        self.middleFrame.pack(expand=True, fill="both", padx=18)
        self.userEntryFrame.pack(fill="x")
        self.passwordEntryFrame.pack(fill="x")
        self.userEntryTextFrame.pack(fill="x", pady=5)
        self.passwordEntryTextFrame.pack(fill="x", pady=5)
        
        self.registerButton.pack(side="left")
        self.loginButton.pack(side="right")
        self.passwordLabel.pack(side="left")
        self.passwordEntryText.pack(side="left", padx=5)
        self.userLabel.pack(side="left")
        self.passwordEntry.pack(fill="x", ipady=5)
        self.userEntryText.pack(side="left", padx=5)
        self.userEntry.pack(fill="x", ipady=5)



        self.bottomFrame = CTkFrame(self, fg_color="black")
        self.bottomFrame.pack(expand=True, fill="both")


        #self.grid_rowconfigure(0, weight=10) # Topo
        #self.grid_rowconfigure(1, weight=0) # Primeiro texto
        #self.grid_rowconfigure(2, weight=0) # Segundo texto
        #self.grid_rowconfigure(3, weight=3) # Primeira entry
        #self.grid_rowconfigure(4, weight=0) # Segunda entry
        #self.grid_rowconfigure(5, weight=3) # Botão
        #self.grid_rowconfigure(6, weight=10) # Fundo
        #self.put(self.firstFrame, self.secondFrame ,self.firstText, self.secondText, self.userEntry, self.passwordEntry, self.button)
        

    @staticmethod
    def put(*widgets):
        c = 0
        for widget in widgets:
            c += 1
            widget.grid(column=1, row=c)

class imageFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.background = CTkImage(light_image=Image.open("D:\Programas\Docs\Cursos\Python\CRUD 3.0\wallpaper.png"), size=(400, 600))
        self.imageLabel = CTkLabel(self, text=None,image=self.background)
        loginFrame.put(self.imageLabel)


  


app = App()
app.mainloop()