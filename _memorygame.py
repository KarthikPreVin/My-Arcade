from tkinter import *
import tkinter.messagebox as mb

import random
import time
import _sql

class MemoryGame(Frame):
    def __init__(self, master,username,con):
        self.master=master
        self.username=username
        self.con=con
        super().__init__(master,width=700,height=500,bg='navy')
        self.game=Frame(self,width=418,height=418,relief='solid',
                        bd=10,bg='lawn green')
        self.game.place(x=141,y=15)
        
        self.open=[]
        
        self.buttons_text=['Q','D','S','G','B','Z','W','K','R','T','Q','D','S','G','B','Z','W','K','R','T']
        self.buttons=list()
        self.moves=0
        random.shuffle(self.buttons_text)
        for r in range(5):
            for c in range(4):
                l=Label(self.game,text=f'   ',width=3,bg='hot pink',fg='black',
                        relief='solid',
                        font=('Courier New',38,'bold'),pady=9)
                l.place(x=c*100,y=r*80)
                self.buttons.append(l)

        self.moves_label = Label(self,text=f'Moves : {self.moves}',
                                 font=('Comic Sans MS',19,'bold'),
                                 bg='navy',fg='hot pink',width=20,
                                 relief='solid',bd=5)

        #self.btn_exit=Button(self,command=self.end,bg='red2',font=('Broadway',24,'bold'),text='◀')
        self.btn_exit=Button(self,command=self.end,bg='red2',font=('Arial',20,'bold'),text='BACK')
        self.btn_exit.place(x=25,y=425)
        self.btn_restart=Button(self,command=self.restart,bg='hot pink',font=('Arial',16,'bold'),text='RESTART')
        self.btn_restart.place(x=550,y=440)
        
        self.moves_label.place(x=141,y=435)

        self.bind__()


    def new_high_score(self):
        prev_high=self.con.get('memorygame')

        if prev_high[1] == None:
            self.con.update('memorygame',self.username,self.moves)
            mb.showinfo('New high score!!',f'You set a new high score\nYour HighScore - {self.moves}')

        elif self.moves<prev_high[1]:
            self.con.update('memorygame',self.username,self.moves)
            mb.showinfo('New high score!!',f'You beat the previous highscore\nPrev HighScore - {prev_high[1]}\nYour HighScore - {self.moves}')

        self.master.do_task('memorygame')
            
    def on_click(self,event):
        if event.widget in self.buttons:
            if event.widget['text'].isspace():
                if len(self.open)%2==0:
                    if len(self.open)==2:
                        self.buttons[self.open[1]].config(text='   ')
                        self.buttons[self.open[0]].config(text='   ')
                        self.open.clear()
                    event.widget.config(text=f' {self.buttons_text[self.buttons.index(event.widget)]} ')
                    self.open.append(self.buttons.index(event.widget))
                else:
                    event.widget.config(text=f' {self.buttons_text[self.buttons.index(event.widget)]} ')
                    self.update()
                        
                    if event.widget['text']==self.buttons[self.open[0]]['text']:
                        self.buttons[self.buttons.index(event.widget)]=None
                        self.buttons[self.open[0]]=None
                        self.moves+=1
                        if not any(self.buttons):
                            self.moves_label.config(text=f'You won in {self.moves} Moves')
                            if self.username != 'DEV-BUILD':
                                self.new_high_score()
                        else:
                            self.moves_label.config(text=f'Moves : {self.moves}')
                        self.open.clear()
                    else:
                        self.open.append(self.buttons.index(event.widget))

                        self.moves+=1
                        self.moves_label.config(text=f'Moves : {self.moves}')
                        
              
        
    def end(self,event=None):
        del self.buttons
        self.destroy()

    def bind__(self):
        for i in self.buttons:
            i.bind('<ButtonRelease-1>',self.on_click)

    def unbind__(self):
        for i in self.buttons:
            i.unbind('<ButtonRelease-1>')

    def restart(self):
        self.game.destroy()
        self.destroy()
        self.update()
        x1=MemoryGame(self.master,self.username,self.con)
        x1.place(x=1,y=1)
"""
if __name__=='__main__':
    tk=Tk()
    x1=MemoryGame(tk,'DEV_BUILD',_sql.Connection())
    tk.geometry('702x502')
    x1.place(x=1,y=1)
    tk.mainloop()
"""
        
