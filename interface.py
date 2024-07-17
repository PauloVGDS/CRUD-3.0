from customtkinter import *
from PIL import Image
import re, os



BACKGNDCOLOR = "black"
CONTRSTEXTCOLOR = "white"
WARNINGCOLOR = "#f4da01"
WARNINGHOVERCOLOR = "#a79500"
LOGTEXTCOLOR = "#ff3055"
REGTEXTCOLOR = "#33dba3"
ADMTEXTCOLOR = "#0f9b0f"
LOGHOVERCOLOR = "#4a1079"
REGHOVERCOLOR = "#3160ac"
ADMHOVERCOLOR = "#032203"
LOGPLACEHOLDCOLOR = "#7A1729"
REGPLACEHOLDCOLOR = "#18664c"
CHECKICONCOLOR = "#107e10"
CANCELICONCOLOR = "#c42b1c"
CANCELHOVERCOLOR = "#501111"
CURRENTPATH = os.path.dirname(os.path.realpath(__file__))

class App(CTk):
    def __init__(self, master=None):
        super().__init__()
        self.title("CRUD 3.0")
        self.geometry("800x600")
        self.maxsize(800, 600)
        self.minsize(800, 600)
        
        self.currentFrame = adminFrame(master=self)
        self.currentFrame.pack(expand=True, fill=BOTH, anchor="center")

    @staticmethod
    def font(font="Titillium Web", size=15, weight="normal"):
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

    def changeFrames(self, adm=False):
        if adm:
            self.forget()
            currentFrame = adminFrame(self.master)
            return currentFrame.pack(expand=True, fill=BOTH, anchor="center")
        if str(self.__class__) == "<class '__main__.adminFrame'>":
            self.forget()
            currentFrame = loginFrame(self.master)
            return currentFrame.pack(expand=True, fill=BOTH, anchor="center")
        if str(self.__class__) == "<class '__main__.loginFrame'>":
            self.forget()
            currentFrame = registerFrame(self.master)
            return currentFrame.pack(expand=True, fill=BOTH, anchor="center")

        self.forget()
        currentFrame = loginFrame(self.master)
        return currentFrame.pack(expand=True, fill=BOTH, anchor="center")


    
class loginFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="black")

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
        self.buttonFrame.pack(fill=X, padx=18, ipady=6)
        self.bottomFrame.pack(expand=True, fill=BOTH)


        widgets.textContainer(master=self.topFrame, text="Entre em sua conta.", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Bem vindo de volta!", fontSize=38, weight="bold", side=BOTTOM, fill=BOTH, padx=18)
        self.userInput = widgets.inputContainer(self.middleFrame, "Usuário", "Person-icon.png", output=self.user, fill=X)
        self.passwordInput = widgets.submitContainer(self.middleFrame, "Senha", "Lock-icon.png", show="*", output=self.password, fill=X)
        self.warning = widgets.textContainer(master=self.buttonFrame, text="", textColor=CONTRSTEXTCOLOR, side=BOTTOM)

        widgets.buttonContainer(self.buttonFrame, "Registrar", side=LEFT, cmd=lambda : App.changeFrames(self), pady = 34)
        widgets.buttonContainer(self.buttonFrame, "Entrar", side=RIGHT, cmd= lambda : widgets.login(self, "Usuário/Senha Incorretos!", self.warning, self.userInput, self.passwordInput), pady = 34)



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
        self.nameInput = widgets.inputContainer(self.middleFrame, "Nome Completo*", "Name-icon.png", output=self.name, fill=X)
        self.emailInput = widgets.inputContainer(self.middleFrame, "Email*", "Mail-icon.png", output=self.email, fill=X)
        self.passwordInput = widgets.submitContainer(self.middleFrame, "Senha*", "GreenLock-icon.png", show="*", output=self.password, fill=X)
        self.warning = widgets.textContainer(master=self.buttonFrame, text="", textColor=CONTRSTEXTCOLOR, side=BOTTOM)

        widgets.personInfoContainer(self.middleFrame, birthAnswer=self.birthdate, genderAnswer=self.gender)
        widgets.buttonContainer(self.buttonFrame, "Registrar", side=RIGHT, pady=28, cmd=lambda : widgets.registro(self, "Preencha os campos obrigatórios!", self.warning, self.nameInput, self.emailInput, self.passwordInput))
        widgets.buttonContainer(self.buttonFrame, "Voltar", side=LEFT, cmd=lambda : App.changeFrames(self), pady=28)
  


class adminFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="black")
        self.search = StringVar()
        self.updateOption = StringVar()
        self.updateOutput = StringVar()
        self.background = App.background(self, path="adminWallpaper.png")
        self.createWidgets()

    def createWidgets(self):
        # Main Frames
        self.topFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.middleFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)
        self.bottomFrame = CTkFrame(self, fg_color=BACKGNDCOLOR)

        widgets.textContainer(master=self.topFrame, text="Somente pessoas autorizadas!", side=BOTTOM, fill=BOTH, padx=18)
        widgets.textContainer(master=self.topFrame, text="Administação", fontSize=38, side=BOTTOM, fill=BOTH, padx=18)
        self.entry = widgets.submitContainer(master=self.middleFrame, text="Pesquisar", image="Search_icon.png", output=self.search, self=self, fill=X)
        self.warning = widgets.textContainer(master=self.bottomFrame, text="", textColor=CONTRSTEXTCOLOR, side=BOTTOM, pady=18)

        self.tabview = CTkTabview(self.middleFrame, height=314,
                                  segmented_button_fg_color=BACKGNDCOLOR, segmented_button_selected_color=BACKGNDCOLOR, segmented_button_selected_hover_color=BACKGNDCOLOR, segmented_button_unselected_hover_color=BACKGNDCOLOR, segmented_button_unselected_color=BACKGNDCOLOR, 
                                  text_color=BACKGNDCOLOR, state=DISABLED, text_color_disabled=BACKGNDCOLOR, border_color=ADMTEXTCOLOR, border_width=2, fg_color=BACKGNDCOLOR)
        self.tabview.add("0")
        widgets.textContainer(master=self.tabview.tab("0"), text="Read", fontSize=22, textColor=ADMTEXTCOLOR)
        self.nome = widgets.textContainer(master=self.tabview.tab("0"), text="Nome:", fontSize=16, textColor=CONTRSTEXTCOLOR, fill=X, padx=8)
        self.email = widgets.textContainer(master=self.tabview.tab("0"), text="Email:", fontSize=16, textColor=CONTRSTEXTCOLOR, fill=X, padx=8)
        self.password = widgets.textContainer(master=self.tabview.tab("0"), text="Senha:", fontSize=16, textColor=CONTRSTEXTCOLOR, fill=X, padx=8)
        self.birth = widgets.textContainer(master=self.tabview.tab("0"), text="Data de Nascimento:", fontSize=16, textColor=CONTRSTEXTCOLOR, fill=X, padx=8)
        self.gender = widgets.textContainer(master=self.tabview.tab("0"), text="Gênero:", fontSize=16, textColor=CONTRSTEXTCOLOR, fill=X, padx=8)
        
        self.tabview.add("1")    
        widgets.textContainer(master=self.tabview.tab("1"), text="Update", fontSize=22, textColor=ADMTEXTCOLOR)
        self.updateCont = widgets.updateContainer(self.tabview .tab("1"), text="Opções:", image="personEdit_icon.png", option=self.updateOption, output=self.updateOutput)
        widgets.textContainer(master=self.tabview.tab("1"), text="Selecione a opção que deseja alterar!", fontSize=18, textColor=CONTRSTEXTCOLOR)

        self.tabview.add("2")
        widgets.textContainer(master=self.tabview.tab("2"), text="Delete", fontSize=22, textColor=ADMTEXTCOLOR)
        widgets.textContainer(master=self.tabview.tab("2"), text="Usuários deletados não podem ser restaurados!", fontSize=16, textColor=CONTRSTEXTCOLOR)
        widgets.textContainer(master=self.tabview.tab("2"), text="Você tem certeza que deseja deletar o usuário:", fontSize=16, textColor=CONTRSTEXTCOLOR)
        self.nome = widgets.textContainer(master=self.tabview.tab("0"), text="", fontSize=16, textColor=CONTRSTEXTCOLOR, fill=X, padx=8)
        
        
        for c in range(0,3):
            buttonFrame = CTkFrame(self.tabview.tab(f"{c}"), fg_color=BACKGNDCOLOR)
            buttonFrame.pack(fill=X, padx=35, pady=14, side=BOTTOM)
            widgets.buttonContainer(master=buttonFrame, text="", cmd=lambda : self.tabview.set(f"{0 if (self.tabview.index(f"{self.tabview.get()}")+1) > 2 else (self.tabview.index(f"{self.tabview.get()}")+1)}"), side=RIGHT).configure(width=50, fg_color='transparent', border_color=ADMTEXTCOLOR, border_width=2, image=App.image("arrowRight_icon.png", 20, 20))
            widgets.buttonContainer(master=buttonFrame, text="", cmd=lambda : self.tabview.set(f"{2 if (self.tabview.index(f"{self.tabview.get()}")-1) < 0 else (self.tabview.index(f"{self.tabview.get()}")-1)}"), side=LEFT).configure(width=50, fg_color='transparent', border_color=ADMTEXTCOLOR, border_width=2, image=App.image("arrowLeft_icon.png", 20, 20))
            if c == 0:
                widgets.buttonContainer(master=buttonFrame, text="", cmd=lambda : App.changeFrames(self)).configure(width=50, fg_color='transparent', border_color=WARNINGCOLOR, hover_color=WARNINGHOVERCOLOR,border_width=2, image=App.image("Exit_icon.png", 20, 20))
            elif c == 1:
                widgets.buttonContainer(master=buttonFrame, text="", cmd=lambda : widgets.admin(self, "Preencha corretamente as opções!", self.warning, self.updateCont)).configure(width=50, fg_color='transparent', border_color=ADMTEXTCOLOR, border_width=2, image=App.image("personEdit_icon.png", 20, 20))
            elif c == 2:
                widgets.buttonContainer(master=buttonFrame, text="", cmd=lambda : widgets.admin(self, "Pesquise um usuário primeiro!", (self.warning))).configure(width=50, fg_color='transparent', border_color=CANCELICONCOLOR, border_width=2, image=App.image("personRemove_icon.png", 20, 20), hover_color=CANCELHOVERCOLOR)
            
        self.tabview.pack(fill=X)
        self.topFrame.pack(expand=True, fill=BOTH, pady=30)
        self.middleFrame.pack(expand=True, fill=BOTH, padx=18)
        self.bottomFrame.pack(expand=True, fill=BOTH)


class widgets:

    def textContainer(master, text, fontSize=20, weight="normal", textColor = CONTRSTEXTCOLOR, image=None,  **kwargs):
        firsTextFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        firstText = CTkLabel(firsTextFrame, text=text, font=App.font(size=fontSize, weight=weight), image=image, text_color=textColor, corner_radius=5)
        firstText.pack(side=LEFT)
        firsTextFrame.pack(**kwargs)
        return firstText
    
    def inputContainer(master, text, image, show="", output=None, **kwargs):
        borderColor = REGTEXTCOLOR
        if (str(master).startswith(".!loginframe") == True):
            borderColor = LOGTEXTCOLOR
        entryFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        entryTextFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        entryText = CTkLabel(entryTextFrame, text=text, font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        imageLabel = CTkLabel(entryTextFrame, text=None)
        entry = CTkEntry(entryFrame, show=show, textvariable=output, fg_color='transparent', border_color=borderColor)
        textLabel = CTkLabel(entryTextFrame, text=None, image=App.image(image, 25, 30))

        entryTextFrame.pack(fill=X, pady=5)
        textLabel.pack(side=LEFT)
        entryText.pack(side=LEFT, padx=5)
        entry.pack(fill=X, ipady=5)
        imageLabel.pack(side=RIGHT)
        entryFrame.pack(**kwargs)
        return imageLabel

    def submitContainer(master, text, image, show="", output=None, self=None, **kwargs):
        showKeyImage = "regVisibilityOn_icon.png"
        hoverColor = REGPLACEHOLDCOLOR
        borderColor = REGTEXTCOLOR
        if (str(master).startswith(".!loginframe") == True):
            showKeyImage = "loginVisibilityOn_icon.png"
            hoverColor = LOGPLACEHOLDCOLOR
            borderColor = LOGTEXTCOLOR
        elif (str(master).startswith(".!adminframe") == True):
            showKeyImage = "admVisibilityOn_icon.png"
            hoverColor = ADMHOVERCOLOR
            borderColor = ADMTEXTCOLOR

        if show == "*":
            submitFrame = CTkFrame(master, fg_color=BACKGNDCOLOR) 
            entryFrame = CTkFrame(submitFrame, fg_color=BACKGNDCOLOR)
            entryTextFrame = CTkFrame(submitFrame, fg_color=BACKGNDCOLOR)
            entryText = CTkLabel(entryTextFrame, text=text, font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
            textLabel = CTkLabel(entryTextFrame, text="", image=App.image(image, 22, 22))
            imageLabel = CTkLabel(entryTextFrame, text=None)
            entry = CTkEntry(entryFrame, show=show, textvariable=output, width=300, fg_color='transparent', border_color=borderColor)
            btn = CTkButton(submitFrame, image=App.image(showKeyImage, 22, 22), text="", font=App.font(weight="bold"), command=lambda: widgets.showKey(btn, entry), 
                            fg_color="transparent", hover_color=hoverColor, text_color="black",
                            border_color=borderColor, border_width=2, 
                            width=50, height=35)
        
            submitFrame.pack(**kwargs)
            entryTextFrame.pack(fill=X, pady=5)
            entryFrame.pack(fill=BOTH, side=LEFT)
            textLabel.pack(side=LEFT)
            entryText.pack(side=LEFT, padx=5)
            entry.pack(ipady=5, side=LEFT)
            imageLabel.pack(side=RIGHT)
            btn.pack(side=RIGHT, ipady=2)
            return imageLabel

        submitFrame = CTkFrame(master, fg_color=BACKGNDCOLOR) 
        entryFrame = CTkFrame(submitFrame, fg_color=BACKGNDCOLOR)
        entryTextFrame = CTkFrame(submitFrame, fg_color=BACKGNDCOLOR)
        entryText = CTkLabel(entryTextFrame, text=text, font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        textLabel = CTkLabel(entryTextFrame, text="", image=App.image("Search_icon.png", 25, 25))
        imageLabel = CTkLabel(entryTextFrame, text=None)
        entry = CTkEntry(entryFrame, show=show, textvariable=output, width=300, fg_color='transparent', border_color=ADMTEXTCOLOR)
        btn = CTkButton(submitFrame, image=App.image("Search_icon.png", 22, 22), text="", font=App.font(weight="bold"), command=lambda: widgets.admin(self, "Busque um email primeiramente!", self.warning, self.entry), 
                           fg_color="transparent", hover_color=ADMHOVERCOLOR, text_color="black",
                           border_color=ADMTEXTCOLOR, border_width=2, 
                           width=50, height=35)

        submitFrame.pack(**kwargs)
        entryTextFrame.pack(fill=X, pady=5)
        entryFrame.pack(fill=BOTH, side=LEFT)
        textLabel.pack(side=LEFT)
        entryText.pack(side=LEFT, padx=5)
        entry.pack(ipady=5, side=LEFT)
        imageLabel.pack(side=RIGHT)
        btn.pack(side=RIGHT, ipady=2)
        return imageLabel

    def buttonContainer(master, text, cmd=None, **kwargs):
        fgColor = LOGTEXTCOLOR
        hoverColor = LOGHOVERCOLOR
        textColor = "white"
        if (str(master).startswith(".!registerframe") == True):
            fgColor = REGTEXTCOLOR
            hoverColor = REGHOVERCOLOR
            textColor = "black"
        elif (str(master).startswith(".!adminframe") == True):
            fgColor = ADMTEXTCOLOR
            hoverColor = ADMHOVERCOLOR

        buttonFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        Button = CTkButton(buttonFrame, text=text, font=App.font(weight="bold"), fg_color=fgColor, hover_color=hoverColor, text_color=textColor, command=cmd)
        Button.pack(ipady=2)
        buttonFrame.pack(**kwargs)
        return Button

    def personInfoContainer(master, genderAnswer, birthAnswer):
        # Widget exclusivo da janela de registro
        personInfoFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)
        birthdateEntryFrame = CTkFrame(personInfoFrame, fg_color=BACKGNDCOLOR)
        birthdateEntryTextFrame = CTkFrame(birthdateEntryFrame, fg_color=BACKGNDCOLOR)
        genderEntryFrame = CTkFrame(personInfoFrame, fg_color=BACKGNDCOLOR)
        genderEntryTextFrame = CTkFrame(genderEntryFrame, fg_color=BACKGNDCOLOR)


        birthdateEntryText = CTkLabel(birthdateEntryTextFrame, text="Data de nascimento", font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        birthdateEntry = CTkEntry(birthdateEntryFrame,
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

    def updateContainer(master, text, image=None, option=None, output=None):
        hoverColor = REGPLACEHOLDCOLOR
        borderColor = REGTEXTCOLOR
        if (str(master).startswith(".!loginframe") == True):
            hoverColor = LOGPLACEHOLDCOLOR
            borderColor = LOGTEXTCOLOR
        elif (str(master).startswith(".!adminframe") == True):
            hoverColor = ADMHOVERCOLOR
            borderColor = ADMTEXTCOLOR


        personInfoFrame = CTkFrame(master, fg_color=BACKGNDCOLOR)

        menuEntryFrame = CTkFrame(personInfoFrame, fg_color=BACKGNDCOLOR)
        menuEntryTextFrame = CTkFrame(menuEntryFrame, fg_color=BACKGNDCOLOR)
        menuOptionText = CTkLabel(menuEntryTextFrame, text=text, font=App.font(weight="bold"), text_color=CONTRSTEXTCOLOR)
        menuImage = CTkLabel(menuEntryTextFrame, text=None,image=App.image(image, 25, 25))
        menuEntryContainer = CTkFrame(menuEntryFrame, 
                                             fg_color=BACKGNDCOLOR, border_color=borderColor, border_width=2, 
                                             width=108, height=35)
        imageLabel = CTkLabel(menuEntryTextFrame, text=None)
        entry = CTkEntry(personInfoFrame, show="", textvariable=output, width=260, fg_color='transparent', border_color=borderColor)
        menuOption = CTkOptionMenu(menuEntryContainer, 
                                          dropdown_font=App.font(weight="bold", size=13), font=App.font(weight="bold"), 
                                          width=125, height=34, 
                                          fg_color=BACKGNDCOLOR, bg_color=borderColor, text_color=hoverColor,
                                          button_color=borderColor, button_hover_color=hoverColor, 
                                          dropdown_fg_color=BACKGNDCOLOR, dropdown_text_color=borderColor, dropdown_hover_color=hoverColor, 
                                          values=["Nome", "Email", "Senha", "Nascimento", "Gênero"], variable=option)


        personInfoFrame.pack(fill=X, pady=5)
        menuEntryFrame.pack(side=LEFT)
        menuEntryTextFrame.pack(fill=X, pady=5)
        menuImage.pack(ipadx=3, side=LEFT)
        menuOptionText.pack(side=LEFT)
        menuEntryContainer.pack(fill=X, ipady=2, ipadx=10)
        imageLabel.pack(side=RIGHT)
        menuOption.place(x=2, y=2)
        entry.pack(ipady=5, pady=1, side=BOTTOM)
        return imageLabel

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
        if (master.user.get() == "admin") and (master.password.get() == "admin"):
            App.changeFrames(master, True)
        
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

    def admin(master, texto="", var=None, *args):
        # Var = Mensagem de erro
        # Args = Imagem de X nas entrys
        
        if master.search.get() == "" : # or master.search.get() not in DATABASE:
            for el in args:
                el.configure(image=App.image("Cancel_icon.png", 25, 25))  
            var.configure(fg_color=CANCELICONCOLOR)
            var.configure(text_color = CONTRSTEXTCOLOR)
            # if master.search.get() not in DATABASE:
                #var.configure(text = "Usuário não encontrado!")
            var.configure(text = texto)
            return master.update()
        
        if master.updateOutput.get() == "" or master.updateOption.get() == "":
            for el in args:
                el.configure(image=App.image("Cancel_icon.png", 25, 25))  
            var.configure(fg_color=CANCELICONCOLOR)
            var.configure(text_color = CONTRSTEXTCOLOR)
            var.configure(text = texto)
            

        for el in args:
            el.configure(image=App.image("Check_icon.png", 25, 25))
        var.configure(fg_color=CHECKICONCOLOR)
        var.configure(text_color = CONTRSTEXTCOLOR)
        var.configure(text = "Usuário encontrado!")

    def showKey(btn, entry):
        entry.configure(show= "") if (entry.cget("show") == "*") else entry.configure(show= "*")
        if entry.cget("border_color") == LOGTEXTCOLOR:
            return btn.configure(image=App.image("loginVisibilityOn_icon.png", 22, 22) if entry.cget("show") == "*" else App.image("loginVisibilityOff_icon.png", 22, 22))
        if entry.cget("border_color") == REGTEXTCOLOR:
            return btn.configure(image=App.image("regVisibilityOn_icon.png", 22, 22) if entry.cget("show") == "*" else App.image("regVisibilityOff_icon.png", 22, 22))    
        
        return btn.configure(image=App.image("admVisibilityOn_icon.png", 22, 22) if entry.cget("show") == "*" else App.image("adminVisibilityOff_icon.png", 22, 22))

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