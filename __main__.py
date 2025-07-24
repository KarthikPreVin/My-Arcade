import _mainpage
import _sql

from tkinter import * # type: ignore
import tkinter.messagebox as mb
from ctypes import windll
from PIL import Image as IMAGE_PIL,ImageTk as IMAGE_TK
import keyboard

size=windll.user32.GetSystemMetrics
#spring green,black,deep sky blue
class App(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False,False)
        w=702
        h=502
        x, y = size(0)//2-w//2, size(1)//2-h//2
        
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.title('MyArcade')

        self.eye1=IMAGE_TK.PhotoImage(IMAGE_PIL.open('eye.png').resize((42,42)))
        self.eye2=IMAGE_TK.PhotoImage(IMAGE_PIL.open('eyeslash.png').resize((42,42)))
        
        
        
        self.font=('Times New Roman',27,'bold')
        self.col1,self.col2,self.col3=('#F15412','#34B3F1','#000000')
        self.con=_sql.Connection()
        self.config(bg='white')
        #login FRAME
        self.FRAME=Frame(self,width=700,height=500,bg=self.col1)
        self.CREATE=Frame(self,width=700,height=500,bg=self.col1)
        ###components of login frame
        Label(self.FRAME,text='         Login         ',font=('Arial',30,'bold'),height=2,
              bg=self.col2,fg=self.col3,bd=10,relief='solid').place(x=183,y=30)
        
        self.l_username=Label(self.FRAME,text='Username',font=self.font,width=10,relief='solid',bd=3,fg=self.col3,bg=self.col2)
        self.l_password=Label(self.FRAME,text='Password',font=self.font,width=10,relief='solid',bd=3,fg=self.col3,bg=self.col2)

        self.e_username=Entry(self.FRAME,font=self.font,bd=3)
        self.e_password=Entry(self.FRAME,font=self.font,bd=3,show='*')

        self.b_show=Button(self.FRAME,command=self.show,fg=self.col3,bg=self.col2,font=('Courier New',18,'bold'),bd=3,image=self.eye1) # type: ignore
        self.b_login=Button(self.FRAME,command=self.login,font=('Times New Roman',20,'bold'),text='LOGIN',width=7,bd=5,fg=self.col3,bg=self.col2)
        self.b_create=Button(self.FRAME,command=self.create,font=('Times New Roman',20,'bold'),text='Create New Account!',width=20,bd=5,fg=self.col3,bg=self.col2)

        self.l_username.place(x=40,y=180)
        self.l_password.place(x=40,y=260)
        self.e_username.place(x=265,y=180)
        self.e_password.place(x=265,y=260)
        self.b_show.place(x=640,y=260)
        self.b_login.place(x=450,y=320)
        self.b_create.place(x=170,y=390)

        ###components of create new user frame
        Label(self.CREATE,text='     Create Account    ',font=('Arial',30,'bold'),height=2,
              bg=self.col2,fg=self.col3,bd=10,relief='solid').place(x=155,y=30)
        
        self.l_username_=Label(self.CREATE,text='Username',font=self.font,width=10,relief='solid',bd=3,fg=self.col3,bg=self.col2)
        self.l_password_=Label(self.CREATE,text='Password',font=self.font,width=10,relief='solid',bd=3,fg=self.col3,bg=self.col2)
        self.l_password2=Label(self.CREATE,text='Retype pwd',font=self.font,width=10,relief='solid',bd=3,fg=self.col3,bg=self.col2)

        self.e_username_=Entry(self.CREATE,font=self.font,bd=3)
        self.e_password_=Entry(self.CREATE,font=self.font,bd=3,show='*')
        self.e_password2=Entry(self.CREATE,font=self.font,bd=3,show='*')

        self.b_show_=Button(self.CREATE,command=self.show2,fg=self.col3,bg=self.col2,font=('Courier New',18,'bold'),bd=3,image=self.eye1) # type: ignore
        self.b_confirm=Button(self.CREATE,command=self.confirm,font=('Times New Roman',20,'bold'),text='SUBMIT',width=21,bd=5,fg=self.col3,bg=self.col2)
        self.b_back=Button(self.CREATE,command=self.back,font=('Times New Roman',20,'bold'),text='BACK',width=5,bd=5,fg=self.col3,bg=self.col2)
        
        self.l_username_.place(x=40,y=180)
        self.l_password_.place(x=40,y=260)
        self.l_password2.place(x=40,y=340)
        self.e_username_.place(x=265,y=180)
        self.e_password_.place(x=265,y=260)
        self.e_password2.place(x=265,y=340)
        self.b_show_.place(x=640,y=260)
        self.b_confirm.place(x=210,y=420)
        self.b_back.place(x=50,y=420)

        self.FRAME.place(x=1,y=1)
        self.CREATE.place(x=-1000,y=-1000)

        self.bind('<Return>',self.press_enter)

    def show(self):
        if self.e_password['show']=='':
            self.e_password.config(show='*')
            self.b_show.config(image=self.eye1)# type: ignore
            self.update()
        else:
            self.e_password.config(show='')
            self.b_show.config(image=self.eye2)# type: ignore
            self.update()

    def show2(self):
        if self.e_password_['show']=='':
            self.e_password_.config(show='*')
            self.b_show_.config(image=self.eye1)# type: ignore
            self.update()
        else:
            self.e_password_.config(show='')
            self.b_show_.config(image=self.eye2)# type: ignore
            self.update()

    def login(self):
        u=self.e_username.get().lower()
        p=self.e_password.get().lower()
        check = self.con.check(u,p)
        if check==False:
            userchoice=mb.askokcancel('new username detected','username doesnt exist\ncreate a new account?')
            if userchoice:
                self.create()

        elif check==None:
            mb.showwarning('Incorrect password','Password enter is incorrect')
        else:
            p=_mainpage.MainPage(self,u,self.con)
            self.FRAME.place(x=-1000,y=-1000)
            self.e_username.delete(0,END)
            self.e_password.delete(0,END)
            self.e_username_.delete(0,END)
            self.e_password_.delete(0,END)
            self.e_password2.delete(0,END)
            p.place(x=1,y=1)

    def create(self):
        self.CREATE.place_configure(x=1,y=1)
        self.e_username_.delete(0,END)
        self.e_password_.delete(0,END)
        self.e_password2.delete(0,END)
        self.e_password_.config(show='*')
        self.e_username_.focus()

    def confirm(self):
        u=self.e_username_.get().lower()
        p=self.e_password_.get().lower()
        q=self.e_password2.get().lower()
        
        if p!=q:
            self.e_password2.delete(0,END)
            return mb.showinfo('password incorrect!','retyped password is not same as typed password')
        if len(u)>20:
            return mb.showinfo('length too high!','username cannot contain *more than 20 letters* or less than 1 characters')
        
        if len(p)>20:
            return mb.showinfo('length too high!','password cannot contain *more than 20 letters* or less than 5 characters')    

        if len(u)<1:
            return mb.showinfo('length too low!','username cannot contain more than 20 letters or *less than 1 characters*')
        
        if len(p)<5:
            return mb.showinfo('length too low!','password cannot contain more than 20 letters or *less than 5 characters*')    

        check=self.con.add(u,p)
        if not check:
            self.e_username_.delete(0,END)
            mb.showinfo('repeated names','username already exists try a new username')
        else:
            mb.showinfo('Succesful!',f'Created a new account with username {u}')
            self.FRAME.place(x=-1000,y=-1000)
            self.CREATE.place(x=-1000,y=-1000)
            self.e_username.delete(0,END)
            self.e_password.delete(0,END)
            self.e_username_.delete(0,END)
            self.e_password_.delete(0,END)
            self.e_password2.delete(0,END)
            p=_mainpage.MainPage(self,u,self.con)
            p.place(x=1,y=1)

    def back(self):
        self.CREATE.place(x=-1000,y=-1000)
        self.FRAME.place(x=1,y=1)
        self.e_username.delete(0,END)
        self.e_password.delete(0,END)
        self.e_username_.delete(0,END)
        self.e_password_.delete(0,END)
        self.e_password2.delete(0,END)

    def press_enter(self,event):
        if self.CREATE.place_info()['x']=='1':
            self.confirm()
        elif self.FRAME.place_info()['x']=='1':
            self.login()



if __name__=='__main__':
    keyboard.press_and_release('win+m')
    app=App()
    app.iconify()
    app.update()
    app.deiconify()
    app.mainloop()
    del app
        
