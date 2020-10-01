import tkinter
import webbrowser


def edit_content():
    giventext=textfield.get('1.0','end-1c')

    f = open('helloworld.html','wb')

    message = """<html>
    <head><style>
    body {
      color: blue;
      background-color: grey;
    }

    h1 {
      color: red;
      font-family: calibri;
      font-size: 300%;
    }
    h2 {
      font-family: calibri;
    }5
    </style></head>
    <body>
    <center><p><h1>   Giventext  </h1></p></center>
    <center><p><h2> your text is converted...</h2></p></center>
    </body>
    </html>"""

    f.write(message.encode())
    f.close()

    webbrowser.open_new_tab('helloworld.html')



window=tkinter.Tk()
window.title("create webpage")
tkinter.Label(window,text='Text to Html Generator',font=("arail",15), justify=tkinter.LEFT,padx = 10).pack()
scroll=tkinter.Scrollbar(window)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
textfield=tkinter.Text(window,height=2,width=35)
textfield.pack(side=tkinter.LEFT,fill=tkinter.Y)
scroll.config(command=textfield.yview)
textfield.config(yscrollcommand=scroll.set)
button=tkinter.Button(window,text='Convert',bd=2,font=("arail",15),padx=10,command=edit_content)
button.pack()
label=tkinter.Label(window,text='create webpage',font=("arial",15), justify=tkinter.LEFT,padx=20,pady=60)
label.pack()
window.geometry("600x500")
window.mainloop()
