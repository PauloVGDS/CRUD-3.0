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