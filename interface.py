from customtkinter import *
from PIL import Image

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title="CRUD"
        self.geometry("1000x600")

        self.login_frame = loginFrame(master=self)
        self.login_frame.pack(side="right", expand=True, fill="both")
        self.image_frame = imageFrame(master=self)
        self.image_frame.pack(side="left")
      

class loginFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="black", **kwargs)
        self.firstFrame = CTkFrame(self, fg_color="black", corner_radius=None)
        self.firstText = CTkLabel(self.firstFrame, text="Bem vindo de volta!")
        self.secondText = CTkLabel(self.firstFrame, text="Entre em sua conta.")

        self.firstFrame.pack(expand=True, fill="both")
        self.firstText.pack()
        self.secondText.pack()


        self.secondFrame = CTkFrame(self, fg_color="black", corner_radius=None)
        self.userEntry = CTkEntry(self.secondFrame, fg_color='transparent', border_color="#ff3055")
        self.passwordEntry = CTkEntry(self.secondFrame, fg_color='transparent', border_color="#ff3055")
        self.button = CTkButton(self.secondFrame, text="Submit", fg_color="#ff3055", hover_color="#4a1079")

        self.secondFrame.pack(expand=True, fill="both")
        self.button.pack(side="bottom", ipady=5, padx=20)
        self.passwordEntry.pack(side="bottom", ipady=5, padx=20, pady=10, fill='x')
        self.userEntry.pack(side="bottom", ipady=5, padx=20, fill='x')



        self.thirdFrame = CTkFrame(self, fg_color="black", corner_radius=None)
        self.thirdFrame.pack(expand=True, fill="both")


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
        self.background = CTkImage(light_image=Image.open("D:\Programas\Docs\Cursos\Python\CRUD 3.0\wallpaper.png"), size=(600, 600))
        self.imageLabel = CTkLabel(self, text=None,image=self.background)
        loginFrame.put(self.imageLabel)


  


app = App()
app.mainloop()