from tkinter import *
import functions
import random
import time as ttime

######################-----WIN--Patterns-----######################            

#  X - -   - - X   X X X   - - -   - - -   X - -   - X -   - - X  #
#  - X -   - X -   - - -   X X X   - - -   X - -   - X -   - - X  #
#  - - X   X - -   - - -   - - -   X X X   X - -   - X -   - - X  #

#0 1 2
#3 4 5
#6 7 8


class TicTacToe(Frame):
    def __init__(self,master,diff):
        super().__init__(master,width=700,height=500,bg='navy')
        self.master=master
        self.game=Frame(self,width=425,
                        height=424,
                        relief='solid',
                        bd=10,bg='lawn green')
        self.game.place(x=270,y=15)
        self.play_buttons=[]
        self.difficulty=diff
        self.board=[None,None,None,None,None,None,None,None,None]
        self.side_label=Label(self,bg='lawn green',width=12,fg='red',font=('Arial',25,'bold'),relief='solid',bd=6)
        self.side_label.place(x=10,y=50)
        self.pattern='X'
        self.win_patterns=[[0,4,8],
                           [2,4,6],
                           [0,1,2],
                           [3,4,5],
                           [6,7,8],
                           [0,3,6],
                           [1,4,7],
                           [2,5,8]]
        b1=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b1.place(x=6,y=6)
        b2=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b2.place(x=136,y=6)
        b3=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b3.place(x=266,y=6)
        b4=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b4.place(x=6,y=136)
        b5=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b5.place(x=136,y=136)
        b6=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b6.place(x=266,y=136)
        b7=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b7.place(x=6,y=266)
        b8=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b8.place(x=136,y=266)
        b9=Label(self.game,font=('Arial',45,'bold'),padx=3,pady=23,width=3,bd=7,relief='solid')
        b9.place(x=266,y=266)
        self.play_buttons.extend([b1,b2,b3,b4,b5,b6,b7,b8,b9])
        
        self.easy = Button(self,bg='cyan',bd=7,text='Restart :  Easy ',font=('Courier New',18,'bold'),command=self.easy)
        self.medium=Button(self,bg='lawn green',bd=9,text='Restart : Medium',font=('Courier New',18,'bold'),command=self.medi)
        self.hard = Button(self,bg='cyan',bd=7,text='Restart :  Hard ',font=('Courier New',18,'bold'),command=self.hard)
        Label(self,fg='red',bg='navy',text='Select Mode',width=13,font=('Courier New',23,'bold underline')).place(x=10,y=130)
        self.easy.place(x=10,y=190)
        self.medium.place(x=8,y=248)
        self.hard.place(x=10,y=310)

        #self.btn_exit=Button(self,command=self.end,bg='red2',font=('Broadway',24,'bold'),text='◀')
        self.btn_exit=Button(self,command=self.end,bg='red2',font=('Arial',20,'bold'),text='BACK')
        self.btn_exit.place(x=25,y=425)

        self.update()
        self.game.update()

        self.starter=random.choice(['player','ai'])
        self.ender=['player','ai']
        self.ender.remove(self.starter)
        self.ender=self.ender[0]
        if self.starter == 'ai':
            ai_choice=self.difficulty(self.board)
            self.play_buttons[ai_choice].config(text=self.pattern)
            self.board[ai_choice]=self.pattern
            if self.pattern=='X':
                self.pattern='O'
            else:
                self.pattern='X'
            self.side_label.config(text='Your Turn')
        else:
            self.side_label.config(text='Your Turn')

        
        self.game.bind_all('<Enter>',self.hover_in)
        self.game.bind_all('<Leave>',self.hover_out)
        self.game.bind_all('<ButtonRelease-1>',self.on_click)
    def on_click(self,event):
        if event.widget not in self.play_buttons:
            return
        if event.widget['text']=='' or event.widget['fg']=='gray' and event.widget['text'] in ['O','X']:
            self.game.unbind_all('<ButtonRelease-1>')
            self.game.unbind_all('<Enter>')
            self.game.unbind_all('<Leave>')
            
            event.widget.config(text=self.pattern,fg='black')
            self.board[self.play_buttons.index(event.widget)]=self.pattern
            if self.pattern=='X':
                self.pattern='O'
            else:
                self.pattern='X'
            winning=self.win_check()
            if winning:
                if winning=='X':
                    self.side_label.config(text=self.starter.upper()+' WINS!')
                    return
                else:
                    self.side_label.config(text=self.ender.upper()+' WINS!')
                    return
            elif all(self.board):
                self.side_label.config(text='DRAW MATCH!')
                return
            self.think(random.choice([5,6,7]))
            ai_choice=self.difficulty(self.board)
            self.play_buttons[ai_choice].config(text=self.pattern)
            self.board[ai_choice]=self.pattern
            if self.pattern=='X':
                self.pattern='O'
            else:
                self.pattern='X'
            winning=self.win_check()
            if winning:
                if winning=='X':
                    self.side_label.config(text=self.starter.upper()+' WINS!')
                else:
                    self.side_label.config(text=self.ender.upper()+' WINS!')
            elif all(self.board):
                self.side_label.config(text='DRAW MATCH!')
                return
            
                
            else:
                
                self.game.bind_all('<Enter>',self.hover_in)
                self.game.bind_all('<Leave>',self.hover_out)
                self.game.bind_all('<ButtonRelease-1>',self.on_click)
                self.update()

    def hover_in(self,event):
        if event.widget not in self.play_buttons:return
        else:
            if event.widget['text']=='':
                event.widget.config(text=self.pattern,fg='gray')
    def hover_out(self,event):
        if event.widget not in self.play_buttons:return
        else:
            if event.widget['fg']=='gray':
                event.widget.config(text='',fg='black')
                
    def win_check(self):
        for i in self.win_patterns:
            if self.board[i[0]]==self.board[i[1]]:
                if self.board[i[1]]==self.board[i[2]]:
                    if self.board[i[1]]!=None:
                        self.play_buttons[i[0]].config(bg='red')
                        self.play_buttons[i[1]].config(bg='red')
                        self.play_buttons[i[2]].config(bg='red')
                        
                        return self.board[i[1]]
        return False

    def think(self,time):
        try:
            self.side_label.config(text='thinking...')
            for i in range(time):
                if self.side_label['text']=='thinking...':
                    self.side_label.config(text='thinking')
                    ttime.sleep(0.1)
                else:
                    self.side_label.config(text=self.side_label['text']+'.')
                    ttime.sleep(0.25)
                self.master.update()
            self.side_label.config(text='Your Move!')
        except:return

    def end(self):
        self.destroy()
        del self

    def medi(self):
        self.destroy()
        tt=TicTacToe(self.master,functions.intel_medium)
        tt.place(x=1,y=1)
        del self

    def easy(self):
        self.destroy()
        tt=TicTacToe(self.master,functions.intel_easy)
        tt.place(x=1,y=1)
        tt.easy.config(bg='lawn green',bd=9)
        tt.easy.place_configure(x=8,y=188)
        tt.medium.config(bg='cyan',bd=7)
        tt.medium.place_configure(x=10,y=250)
        del self

    def hard(self):
        self.destroy()
        tt=TicTacToe(self.master,functions.intel_impossible)
        tt.place(x=1,y=1)
        tt.hard.config(bg='lawn green',bd=9)
        tt.hard.place_configure(x=8,y=308)
        tt.medium.config(bg='cyan',bd=7)
        tt.medium.place_configure(x=10,y=250)
        del self

if __name__=='__main__':
    tk=Tk()
    tk.geometry('702x502')
    b=TicTacToe(tk,functions.intel_medium)
    b.place(x=1,y=1)
    tk.mainloop()
