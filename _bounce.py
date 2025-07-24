from tkinter import *
import tkinter.messagebox as mbimport
import random
from keyboard import is_pressed
import _sql

class Bounce(Frame):
    def __init__(self,master,username,con):
        self.master=master
        self.username=username
        self.con=con
        
        super().__init__(self.master,width=700,height=500,bg='navy')
        self.game=Frame(self,bg='indian red',
                        width=600,height=400)
        self.speed=20
        self.game.place(x=50,y=10)
        self.x_velocity=random.randint(5,7)
        self.y_velocity=random.randint(5,7)
        self.image=PhotoImage(file='ball.png')
        self.ball=Label(self.game,image=self.image,bd=0)
        self.pos=[random.randrange(0,99),random.randrange(0,300)]       
        self.ball.place(x=self.pos[0],y=self.pos[1])
        self.gameover=False
        #self.btn_exit=Button(self,command=self.end,bg='red2',font=('Broadway',24,'bold'),text='◀')
        self.btn_exit=Button(self,command=self.end,bg='red2',font=('Arial',20,'bold'),text='BACK')
        self.btn_exit.place(x=25,y=425)
        
        Label(self.game,bd=0,bg='black',font=('Arial',5,'bold'),height=57,width=1).place(x=0,y=0)
        Label(self.game,bd=0,bg='black',font=('Arial',2,'bold'),height=1,width=300).place(x=0,y=0)
        Label(self.game,bd=0,bg='black',font=('Arial',2,'bold'),height=1,width=300).place(x=0,y=394)
        self.scorel=Label(self,bd=5,bg='lawn green',fg='black',font=('Arial',25,'bold'),relief='solid',text='Score : 0',width=11)
        self.scorel.place(x=220,y=425)
        self.bat = Label(self.game,bg='lawn green',text='-',fg='red',bd=1,relief='solid',font=('Arial',5,'bold'),width=1,height=15)
        self.bat.place(x=592, y=100)
        self.bat_pos=100
        self.score=0
        self.countdown()
        
        self.time=60000
        self.time_label=Label(self,width=11,text=f'Time left : {self.time//1000}',font=('Arial',25,'bold'),relief='solid',bd=5,bg='lawn green')
        self.time_label.place(x=460,y=425)
    

        
        

    def _update(self):
        #corners = (0,0), (0,355), (552,0), (552,355) [ if hit on bat ] else (552->560)
        #75-195 bat at y=100 , bat length = 110 px
        self.counterf.place(x=-200,y=-200)
        self.update_idletasks()
        self.after_cancel(self.init3)
        try:
            try:
                self.after_cancel(self.after_var)
            except:
                pass
            self.time_label.config(text=f'Time left : {int(self.time//1000)}')
            self.update_idletasks()
            if self.pos[0]>560-self.x_velocity or self.time<=self.speed:
                self.gameover=True
                self.x_velocity=0;self.y_velocity=0
                self.GAMEOVER()
                return

                
            elif self.pos[0]>552-self.x_velocity and not self.gameover:
                if self.pos[1]>=self.bat_pos-35 and self.pos[1]<=self.bat_pos+105:
                    self.score+=1
                    self.x_velocity=-self.x_velocity
                    self.scorel.config(text=f'Score : {self.score}')
            
            if self.pos[1]>355-self.y_velocity:
                self.y_velocity=-self.y_velocity
            if self.pos[0]+self.x_velocity<0:
                self.x_velocity=-self.x_velocity
            if self.pos[1]+self.y_velocity<0:
                self.y_velocity=-self.y_velocity

            if (is_pressed('up') or is_pressed('W') or is_pressed('w')) and not self.gameover:self.up()
            if (is_pressed('down') or is_pressed('S') or is_pressed('s')) and not self.gameover:self.down()
            
                

            self.pos[0]=self.pos[0]+self.x_velocity
            self.pos[1]=self.pos[1]+self.y_velocity
            self.ball.place_configure(x=self.pos[0],y=self.pos[1])
            self.time-=self.speed*3/2
            
        except:
            del self
        if not self.gameover:
            try:
                self.after_var=self.after(self.speed,func=self._update)
            except:
                pass

    def new_high_score(self):
        prev_high=self.con.get('bounce')
        if prev_high[1] == None:
            self.con.update('bounce',self.username,self.score)
            
            mb.showinfo('New high score!!',f'You set a new high score\nYour HighScore - {self.score}')
        elif self.score>prev_high[1]:
            self.con.update('bounce',self.username,self.score)
            
            mb.showinfo('New high score!!',f'You beat the previous highscore\nPrev HighScore - {prev_high[1]}\nYour HighScore - {self.score}')
        self.master.do_task('bounce')
        
    def GAMEOVER(self):
        x=Frame(self.game,bg='black')
        Label(x,text=f'Your Score : {self.score}',bg='lawn green',
              font=('Comic Sans MS',19,'bold'),relief='solid',width=15).pack()
        Button(x,text='RESTART',bg='lawn green',font=('Comic Sans MS',19,'bold'),
               bd=10,width=10,command=self.restart).pack()
        x.place(x=190,y=100)
        self.after_cancel(self.after_var)
        if self.username != 'DEV-BUILD':
            self.new_high_score()
   
            
            
        #else:
        #   self.after_cancel(self.timer)
        #   self.GAMEOVER()
                                   
            
    def end(self):
        self.destroy()
        del self

    def restart(self):
        self.destroy()
        B=Bounce(self.master,self.username,self.con)
        B.place(x=1,y=1)
        del self
    def task1(self):
        self.l.config(text='2')
        self.update()
        self.after_cancel(self.taskinit)
        self.init1=self.after(1000,self.task2)
        self.update()

    def task2(self):
        self.l.config(text='1')
        self.update()
        self.init2=self.after(1000,self.task3)
        self.after_cancel(self.init1)
        self.update()
        
    def task3(self):
        self.l.config(text='0')
        self.update()
        self.after_cancel(self.init2)
        self.init3=self.after(1000,self._update)

    def countdown(self):
        self.counterf=Frame(self.game,relief=SOLID,bd=5)
        Label(self.counterf,text='GAME STARTS IN...',font=('Arial',20,'bold')).pack()
        self.l=Label(self.counterf,text='3',font=('Arial',55,'bold'),width=2,bd=5)
        self.l.pack()
        Label(self.counterf,text='use arrow keys ⬆ ⬇ and to move \nthe bat on the right',font=('Arial',15,'bold')).pack()
        self.counterf.place(x=150,y=100)
        self.update()
        self.taskinit=self.after(1000,self.task1)
       
        

    def up(self):
        if self.bat_pos-6<0:
            return
        self.bat_pos-=6
        self.bat.place_configure(x=592,y=self.bat_pos)
        self.update()


    def down(self):
        if self.bat_pos+116>400:
            return
        self.bat_pos+=6
        self.bat.place_configure(x=592,y=self.bat_pos)
        self.update()

if __name__=='__main__':
    tk=Tk()
    tk.geometry('702x502')
    b=Bounce(tk,'DEV-BUILD',_sql.Connection())
    b.speed=10
    b.place(x=1,y=1)
    tk.mainloop()



