from tkinter import *
import tkinter.messagebox as mb

from keyboard import is_pressed
import special_widgets as spl
from PIL import Image,ImageTk
import random
import _sql

class ColorShoot(Frame):
    def __init__(self,master,username,con):
        self.master=master
        self.username=username
        self.con=con
        
        super().__init__(self.master,width=700,height=500,bg='light cyan')
        self.game=Frame(self,bg='light cyan',width=300,height=490,bd=2,
                        relief='solid').place(x=200,y=5)
        self.wheel=spl.Colourwheel(self.game)
        self.wheel.place(x=260,y=16)
        Label(self,text='  Press  \n  Space  \n  To  \n  Shoot  ',justify=CENTER,font=('Courier New',20,'bold'),bd=2,relief=SOLID,bg='light cyan').place(x=520,y=270)
        # self.intro=Label

        self.moving=[]
        self.flagt=False
        
        self.r=Image.open(r'cannonr.png')
        self.g=Image.open(r'cannong.png')
        self.b=Image.open(r'cannonb.png')
        self.y=Image.open(r'cannony.png')
        self.br=Image.open(r'ballr.png').resize((35,35))
        self.bg=Image.open(r'ballg.png').resize((35,35))
        self.bb=Image.open(r'ballb.png').resize((35,35))
        self.by=Image.open(r'bally.png').resize((35,35))

        self.g_=ImageTk.PhotoImage(self.g)
        self.r_=ImageTk.PhotoImage(self.r)
        self.b_=ImageTk.PhotoImage(self.b)
        self.y_=ImageTk.PhotoImage(self.y)
        self.bg_=ImageTk.PhotoImage(self.bg)
        self.br_=ImageTk.PhotoImage(self.br)
        self.bb_=ImageTk.PhotoImage(self.bb)
        self.by_=ImageTk.PhotoImage(self.by)

        self.lr=Label(self.game,image=self.r_,bd=0)
        self.lg=Label(self.game,image=self.g_,bd=0)
        self.lb=Label(self.game,image=self.b_,bd=0)
        self.ly=Label(self.game,image=self.y_,bd=0)
        self.lbr=Label(self.game,image=self.br_,bd=0)
        self.lbg=Label(self.game,image=self.bg_,bd=0)
        self.lbb=Label(self.game,image=self.bb_,bd=0)
        self.lby=Label(self.game,image=self.by_,bd=0)

        self.comb=[['green' ,self.lg,self.lbg],
                   ['red'   ,self.lr,self.lbr],
                   ['blue'  ,self.lb,self.lbb],
                   ['yellow',self.ly,self.lby]]
        
        self.colour=random.choice(self.comb)
        
        self.lr.place(x=-1000,y=-1000)
        self.lg.place(x=-1000,y=-1000)
        self.lb.place(x=-1000,y=-1000)
        self.ly.place(x=-1000,y=-1000)
        self.lbr.place(x=-1000,y=-1000)
        self.lbg.place(x=-1000,y=-1000)
        self.lbb.place(x=-1000,y=-1000)
        self.lby.place(x=-1000,y=-1000)
        
        self.colour[1].place_configure(x=323,y=390)
        self.colour[2].place_configure(x=343,y=355)
        
        self.game_over=False
        self.score=0
        self.score_lab=Label(self,text='HITS : 0',font=('Comic Sans MS',15,'bold'),width=11,fg='cyan',bg='black')
        self.score_lab.place(x=10,y=100)
        #self.btn_exit=Button(self,command=self.end,bg='red2',font=('Broadway',24,'bold'),text='◀')
        self.btn_exit=Button(self,command=self.end,bg='red2',font=('Arial',20,'bold'),text='BACK')
        self.btn_exit.place(x=25,y=425)
        self.task=self.after(10,self.do_tasks)
        self.time=60000
        self.speed=15
        self.time_label=Label(self,width=12,text=f'Time left : {self.time//1000}',font=('Comic Sans MS',15,'bold'),relief='solid',bd=5,fg='cyan',bg='black')
        self.time_label.place(x=10,y=200)


    def do_tasks(self):
        try:
            self.after_cancel(self.task)
            if not self.game_over:
                self.wheel.rotate()
                if is_pressed('space') and len(self.moving)==0:
                    self.flagt=True
                    self.moving.clear()
                    self.moving.append([self.colour[2],355])
                
                if len(self.moving)==1:
                    self.moving[0][0].place_configure(x=343,y=self.moving[0][1]-10)
                    self.moving[0][1]-=10
                    if self.moving[0][1]-10<214:
                        self.moving.clear()
                        self.check()

                if self.time<=self.speed:
                    self.after_cancel(self.task)
                    self.game_over=True
                    self.gameover('Times UP!!')
                elif self.flagt:
                    self.time-=self.speed*1.9
                    self.time_label.config(text=f'Time left : {int(self.time//1000)}')
            
                self.task=self.after(self.speed,self.do_tasks)
        except:
            try:
                self.after_cancel(self.task)
            except:pass

    def new_high_score(self):
        prev_high=self.con.get('colour')
        if prev_high[1] == None:
            self.con.update('colour',self.username,self.score)
            
            mb.showinfo('New high score!!',f'You set a new high score\nYour HighScore - {self.score}')
        elif self.score>prev_high[1]:
            self.con.update('colour',self.username,self.score)
            
            mb.showinfo('New high score!!',f'You beat the previous highscore\nPrev HighScore - {prev_high[1]}\nYour HighScore - {self.score}')
        self.master.do_task('colour')
        
    def gameover(self,text):
        self._gameover=Frame(self.game,bg='navy',relief='solid')
        Label(self._gameover,bg='navy',text=f'{text}\nYour Score: {self.score}',font=('Comic Sans MS',18,'bold')).pack()
        Button(self._gameover,bg='hot pink',fg='navy',text='Restart',font=('Comic Sans MS',20,'bold'),command=self.restart).pack()
        self._gameover.place(x=505,y=70)
        if self.username != 'DEV-BUILD':
            self.new_high_score()        
                

    def check(self):
        if self.colour[0]==self.wheel.colour:
            self.colour[1].place_configure(x=-1000,y=-1000)
            self.colour[2].place_configure(x=-1000,y=-1000)
            self.colour=random.choice(self.comb)
            self.colour[1].place_configure(x=323,y=390)
            self.colour[2].place_configure(x=343,y=355)
            self.score+=1
            self.score_lab.config(text='HITS : {}'.format(self.score))
            
            return
            #self.moving.append([self.colour[2],355])
            

        else:
            self.after_cancel(self.task)
            self.game_over=True
            self.gameover('Oops!\nYou Missed')

        

    def end(self):
        try:
            self._gameover.destroy()
        except:
            pass
        self.wheel.destroy()
        self.lr.destroy()
        self.lbr.destroy()
        self.lg.destroy()
        self.lbg.destroy()
        self.lb.destroy()
        self.lbb.destroy()
        self.ly.destroy()
        self.lby.destroy()
        self.destroy()
        del self

    def restart(self):
        self._gameover.destroy()
        self.wheel.destroy()
        self.lr.destroy()
        self.lbr.destroy()
        self.lg.destroy()
        self.lbg.destroy()
        self.lb.destroy()
        self.lbb.destroy()
        self.ly.destroy()
        self.lby.destroy()
        self.destroy()
        ColorShoot(self.master,self.username,self.con).place(x=1,y=1)
        del self
  
if __name__=='__main__':
    tk=Tk()
    tk.geometry('702x502')
    b=ColorShoot(tk,'DEV-BUILD',_sql.Connection())
    b.place(x=1,y=1)
    tk.mainloop()

























