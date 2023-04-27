from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
class chatty:
    def __init__(self,root):
        self.root=root
        self.root.title("Chatzy")
        self.root.geometry("750x640+0+0")
        self.root.bind('<Return>',self.enter)
        
        main_frame=Frame(self.root,bd=4,bg='green',width=620)
        main_frame.pack()
        
        img=Image.open('chat logo.jpg')
        img=img.resize((150, 90),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        Title_lab=Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT, image=self.photoimg, text="LET'S CHAT", font=('arial',34,'bold'), fg='blue',bg='white')
        Title_lab.pack(side=TOP)
        self.scroll_y=ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text=Text(main_frame, width=65, height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn=Frame(self.root,bd=4,bg='white',width=730)
        btn.pack()
        
        lab=Label(btn,text="Type here: ",font=('arial',14,'bold'), fg='medium blue',bg='white')
        lab.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn,width=40,textvariable=self.entry,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send=Button(btn,text="SEND",command=self.send, font=('arial',15,'bold'),width=8,bg='light green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn,command=self.clear,text="Clear Data",font=('arial',12,'bold'),width=8,bg='pink',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=""
        self.lab1=Label(btn,text=self.msg,font=('arial',14,'bold'), fg='red',bg='white')
        self.lab1.grid(row=1,column=1,padx=5,sticky=W)
        
    def enter(self, event):
          self.send.invoke()
          self.entry.set('')
          
    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+"You: "+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        
        if (self.entry.get()==""):
            self.msg="Oops! Please type something"
            self.lab1.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.lab1.config(text=self.msg,fg='red')
            
            if (self.entry.get()=='hi' or self.entry.get()=='hello' or self.entry.get()=='hey'):
                self.text.insert(END,'\n\n'+'Chatzy: Hey there! Ask me a question.')
            elif (self.entry.get()=="Tell me a joke" or self.entry.get()=="tell me a joke"):
                self.text.insert(END,"\n\n"+'Chatzy: What do you call a rose that wants to go the moon?\n Gulab Ja Moon')
            elif (self.entry.get()=="Who is your friend?" or self.entry.get()=="who is your friend?" or self.entry.get()=="Who is your friend" or self.entry.get()=='who is your friend'):
                self.text.insert(END,'\n\n'+'Chatzy: Considering you are talking to me now, you are my friend :)')
            elif (self.entry.get()=="Are you real?" or self.entry.get()=="are you real?" or self.entry.get()=="Are you real" or self.entry.get()=='are you real'):
                self.text.insert(END,'\n\n'+'Chatzy: Yes! I am a real chatbot made by Shatakshi, Debdeep and Soujit')
            elif (self.entry.get()=="Tell me a fun fact" or self.entry.get()=="tell me a fun fact"):
                self.text.insert(END,'\n\n'+'Chatzy: Depending on the temperature, the height of the Eiffel Tower \ncan vary by 7 inches!')
            elif (self.entry.get()=="Bye" or self.entry.get()=="bye" or self.entry.get()=="byebye" or self.entry.get()=="goodbye"):
                self.text.insert(END,'\n\n'+'Chatzy: Byeeee! Hope to chat with you soon')
            else:
                self.text.insert(END,'\n\n'+"Chatzy: umm.. sorry, don't know the answer to that :(")


if __name__=='__main__':
    root=Tk()
    ob=chatty(root)
    root.mainloop()


