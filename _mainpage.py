import _puzzle
import _tictactoe
import _memorygame
import _bounce
import _colour_shoot
import _snake
import _sql

import functions
import special_widgets

from tkinter import *
##ttt_choice fix



class MainPage(Frame):
    def __init__(self,master,user,con):
        self.ttt_choice='player'
        self.master=master
        self.user=user
        self.labels=[]
        
        self.con=con
        super().__init__(self.master,width=700,height=500,bg='navy')
        Label(self,text='     My Games     ',font=('Arial',30,'bold'),height=2,
              bg='lawn green',fg='black',bd=10,relief='solid').place(x=179,y=20)
        Label(self,text=f'user : {self.user}',font=('Arial',15,'bold'),
              bg='lawn green',fg='black',bd=5,relief='solid').place(x=260,y=132)
        

        puzzle=self.btn('══Puzzle══',self.g1,'puzzle')
        tctcto=self.btn('Tic═Tac═Toe',self.g2,'tictactoe')
        memory=self.btn('Memory═Game',self.g3,'memorygame')
        bounce=self.btn('══Bounce══',self.g4,'bounce')
        colour=self.btn('Color═Shoot',self.g5,'colour')
        snake_=self.btn('═══Snake═══',self.g6,'snake')
        back  =Button(self,bd=6,text='LOG OUT',command=self.logout,width=9,
                      bg='red',font=('Times New Roman',13,'bold'))
        puzzle.place(x=50,y=170)
        tctcto.place(x=250,y=170)
        memory.place(x=450,y=170)
        bounce.place(x=50,y=320)
        colour.place(x=250,y=320)
        snake_.place(x=450,y=320)
        back.place(x=30,y=450)
        
        

    def btn(self,text,command,g):
        F=Frame(self,bd=5,relief='solid')
        text=f'╔{len(text)*"═"}╗\n╠{text}╣\n╚{len(text)*"═"}╝'
        Button(F,text=text,command=command,width=15,height=3,bd=5,
               bg='khaki1',fg='DeepPink2',font=('Courier New',14,'bold')).pack()
        d=self.con.get(g)
        if g=='tictactoe':
            Label(F,text='No highscore',bg='DeepPink2',fg='khaki1',
              font=('Courier New',15,'bold'),width=15).pack()
            return F
        if d[0]!=None:
            x=d[0]
        else:
            x='Nil'
        if d[1]!=None:
            y=d[1]
        else:
            y='Nil'
        l=Label(F,text=f'{x}-{y}',bg='DeepPink2',fg='khaki1',
              font=('Courier New',15,'bold'),width=15)
        l.pack()
        self.labels.append([l,g])
        return F

    def g1(self):
        _puzzle.Puzzle(self,self.user,self.con).place(x=1,y=1)

    def g2(self):        
        _tictactoe.TicTacToe(self,functions.intel_medium).place(x=1,y=1)

    def g3(self):
        _memorygame.MemoryGame(self,self.user,self.con).place(x=1,y=1)

    def g4(self):
        _bounce.Bounce(self,self.user,self.con).place(x=1,y=1)

    def g5(self):
        _colour_shoot.ColorShoot(self,self.user,self.con).place(x=1,y=1)

    def g6(self):
        _snake.Snake(self,self.user,self.con).place(x=1,y=1)

    def do_task(self,game):
        for i in self.labels:
            if i[1]==game.lower():
                d=self.con.get(game)
                if d[0]!=None:
                    x=d[0]
                else:
                    x='Nil'
                if d[1]!=None:
                    y=d[1]
                else:
                    y='Nil'
                i[0].config(text=f'{x}-{y}')
                self.master.update()
                
            
    def logout(self):
        self.destroy()
        self.master.FRAME.place(x=1,y=1)
        del self
        
if __name__=='__main__':
    app=Tk()
    app.config(bg='white')
    app.geometry('702x502')
    MainPage(app,'DEV-BUILD',_sql.Connection()).place(x=1,y=1)
    app.mainloop()
