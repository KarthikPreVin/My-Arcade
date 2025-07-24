from tkinter import *# type: ignore
import tkinter.messagebox as mb

import random
from keyboard import is_pressed
import _sql

class Snake(Frame):
    def __init__(self,master,username,con):
        self.master=master
        self.username=username
        self.con=con
        super().__init__(self.master,bg='navy',width=700,height=500)
        self.game=Frame(self,bd=10,relief='solid',height=400,width=600)
        self.game.place(x=50,y=10)
        self.components=[]
        self.snake_body=[]
        self.score=-1
        self.score_lab=Label(self,width=13,bg='white',fg='green',font=('Courier New',21,'bold'))
        for i in range(12):
            l=[]
            for j in range(17):
                b=Label(self.game,text='  ',bd=1,relief='flat',font=('Courier New',19,'bold'),bg='white')
                b.grid(row=i,column=j)
                l.append(b)#17x12
            self.components.append(l)
        self.components[5][8].config(bg='green')
        self.snake_body.append([5,8])
        self.food_create()
        self.direction=None
        self.task=self.after(15,self.do_tasks)
        self.flag=True
        self.flag2=False
        self.task_2=self.after(15,self.keyscheck)
        #self.btn_exit=Button(self,command=self.end,bg='red2',font=('Broadway',24,'bold'),text='◀')
        self.btn_exit=Button(self,command=self.end,bg='red2',font=('Arial',20,'bold'),text='BACK')
        self.btn_exit.place(x=25,y=430)
        self.score_lab.place(x=180,y=440)
        self.game_overframe=Frame(self,bg='green',bd=5,relief='solid',width=400,height=200)
        self.speed=150
        # self.time=12000000000
        # self.time_label=Label(self,width=14,text=f'Time left : {self.time//1000}',bg='white',fg='green',font=('Courier New',21,'bold'))
        # self.time_label.place(x=450,y=440)
    def food_create(self):
        self.score+=1
        self.score_lab.config(text=f'Score : {self.score}')
        self.r=random.randint(0,11)
        self.c=random.randint(0,16)
        while [self.r,self.c] in self.snake_body:
            self.r=random.randint(0,11)
            self.c=random.randint(0,16)
        self.components[self.r][self.c].config(bg='red')
        self.update()

    def do_tasks(self):
        self.after_cancel(self.task)

        
        if self.direction=='u':
            self.flag=True
            if self.snake_body[0][0]==0:
                self.game_over()
                return
            for i in self.snake_body[1:]:
                if i==[self.snake_body[0][0]-1,self.snake_body[0][1]]:
                    self.game_over(message='You hit yourself')
                    return
            r,c=self.snake_body[0]
            self.components[r-1][c].config(bg='green')
            self.snake_body.insert(0,[r-1,c])
            if self.snake_body[0]==[self.r,self.c]:
                self.food_create()
            else:
                r,c=self.snake_body[-1]
                self.components[r][c].config(bg='white')
                self.snake_body.pop(-1)

            
        elif self.direction=='d':
            self.flag=True
            if self.snake_body[0][0]==11:
                self.game_over()
                return
            for i in self.snake_body[1:]:
                if i==[self.snake_body[0][0]+1,self.snake_body[0][1]]:
                    self.game_over(message='You hit yourself')
                    return
            r,c=self.snake_body[0]
            self.components[r+1][c].config(bg='green')
            self.snake_body.insert(0,[r+1,c])
            if self.snake_body[0]==[self.r,self.c]:
                self.food_create()
            else:
                r,c=self.snake_body[-1]
                self.components[r][c].config(bg='white')
                self.snake_body.pop(-1)


        elif self.direction=='l':
            self.flag=True
            if self.snake_body[0][1]==0:
                self.game_over()
                return
            for i in self.snake_body[1:]:
                if i==[self.snake_body[0][0],self.snake_body[0][1]]:
                    self.game_over(message='You hit yourself')
                    return
            r,c=self.snake_body[0]
            self.components[r][c-1].config(bg='green')
            self.snake_body.insert(0,[r,c-1])
            if self.snake_body[0]==[self.r,self.c]:
                self.food_create()
            else:
                r,c=self.snake_body[-1]
                self.components[r][c].config(bg='white')
                self.snake_body.pop(-1)


        elif self.direction=='r':
            self.flag=True
            if self.snake_body[0][1]==16:
                self.game_over()
                return
            for i in self.snake_body[1:]:
                if i==[self.snake_body[0][0],self.snake_body[0][1]+1]:
                    self.game_over(message='You hit yourself')
                    return
            r,c=self.snake_body[0]
            self.components[r][c+1].config(bg='green')
            self.snake_body.insert(0,[r,c+1])
            if self.snake_body[0]==[self.r,self.c]:
                self.food_create()
            else:
                r,c=self.snake_body[-1]
                self.components[r][c].config(bg='white')
                self.snake_body.pop(-1)

        # if self.time<=self.speed:
        #     self.game_over(message='Times Up!!')
        #     return
        # else:
        #     if self.flag2:
        #         self.time-=self.speed*6/5
            
        
        
        # self.time_label.config(text=f'Time left : {int(self.time//1000)}')
        
        self.task=self.after(self.speed,self.do_tasks)
        
        
        
    def keyscheck(self):
        self.after_cancel(self.task_2)
        if self.flag:
            if is_pressed('up') or is_pressed('w') or is_pressed('W'):
                if self.direction in ['l','r',None]:
                    self.direction='u'
                    self.flag=False
                    self.flag2=True
            elif is_pressed('down') or is_pressed('s') or is_pressed('S'):
                if self.direction in ['l','r',None]:
                    self.direction='d'
                    self.flag=False
                    self.flag2=True
            elif is_pressed('right') or is_pressed('d') or is_pressed('D'):
                if self.direction in ['u','d',None]:
                    self.direction='r'
                    self.flag=False
                    self.flag2=True
            elif is_pressed('left') or is_pressed('a') or is_pressed('A'):
                if self.direction in ['u','d',None]:
                    self.direction='l'
                    self.flag=False
                    self.flag2=True
            

        self.task_2=self.after(15,self.keyscheck)

        
    def new_high_score(self):
        prev_high=self.con.get('snake')
        if prev_high[1] == None:
            self.con.update('snake',self.username,self.score)
            
            mb.showinfo('New high score!!',f'You set a new high score\nYour HighScore - {self.score}')
        elif self.score>prev_high[1]:
            self.con.update('snake',self.username,self.score)
            
            mb.showinfo('New high score!!',f'You beat the previous highscore\nPrev HighScore - {prev_high[1]}\nYour HighScore - {self.score}')
        self.master.do_task('snake')# type: ignore
            
            
           

    def game_over(self,message='You hit a wall'):
        self.after_cancel(self.task)
        Label(self.game_overframe,
              text=f'{message}\nScore : {self.score}',
              font=('Times New Roman',25,'bold italic'),
              bg='white',fg='green').pack()
        Button(self.game_overframe,text='RESTART',
               font=('Courier New',24,'bold '),
               bg='white',fg='green',command=self.restart).pack()
        self.game_overframe.place(x=245,y=30)
        if self.username != 'DEV-BUILD':
            self.new_high_score()

    def end(self):
        self.destroy()

    def restart(self):
        self.destroy()
        Snake(self.master,self.username,self.con).place(x=1,y=1)
        
    
        
        
            
            

        


if __name__=='__main__':
    tk=Tk()
    tk.geometry('702x502')
    s=Snake(tk,'DEV-BUILD',_sql.Connection())
    s.place(x=1,y=1)

