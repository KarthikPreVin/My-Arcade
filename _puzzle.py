from tkinter import *
import tkinter.messagebox as mb

import functions
import random
import _sql

class Puzzle(Frame):
    def __init__(self,master,username,con):
        self.master=master
        self.username=username
        super().__init__(master,width=700,height=500,bg='navy')
        self.game=Frame(self,
                        width=400,
                        height=402,
                        relief='solid',
                        bd=10,
                        bg='lawn green')
        self.con=con
        self.game.place(x=15,y=10)
        #self.btn_exit=Button(self,command=self.end,bg='red2',font=('Broadway',24,'bold'),text='◀')
        self.btn_exit=Button(self,command=self.end,bg='red2',font=('Arial',20,'bold'),text='BACK')
        self.btn_exit.place(x=25,y=425)
        self.btn_strt=Button(self,text='Shuffle',command=self.shuffle,font=('Arial',25,'bold'))
        self.btn_strt.place(x=250,y=415)
        self.btn_rest=Button(self,text='Reset',command=self.reset,font=('Arial',25,'bold'))
        self.btn_rest.place(x=430,y=415)
        self.side_label=Label(self,text='Order of\npuzzle',relief='solid',bd=5,font=('Arial',20,'bold'),bg='navy',fg='white')
        self.side_label.place(x=490,y=270)
        self.side_image=PhotoImage(file='puzzle_image.png')
        self.side_image2=PhotoImage(file='puzzle_image2.png')
        self.image_label=Label(self,image=self.side_image)
        self.image_label.place(x=430,y=10)

        #score
        self.moves=0
        self.lab_moves=Label(self,width=10,relief='solid',bd=5,text=f'Moves : {self.moves}',fg='black',bg='lawn green',font=('Arial',20,'bold'))
        self.lab_moves.place(x=460,y=350)
        self.order =['1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9','10','11','12','13','14', '15', '' ]
        self.lab = []
        self.lab2= []
        l_=Label(self.game,text='',width=4,height=2,font=('Times New Roman',25,'bold'),fg='white',bg='lawn green',relief='flat',bd=5,pady=4)
        l_.place(x=285,y=289)
        for i in range(1,16):
            lab = Label(self.game,text=f'{self.order[i-1]}',width=4,height=2,font=('Times New Roman',25,'bold'),fg='white',bg='sienna1',relief='solid',bd=5,pady=4)
            lab.place(x=94*((i-1)%4)+3,y=96*((i-1)//4)+1)
            self.lab.append(lab)          
        self.lab.append(l_)
        self.update()
        self.game.update()
        #self.game.bind_all('<ButtonRelease-1>',self.check)
    def end(self):
        self.destroy()


    def reset(self):
        self.btn_rest.config(state='disabled')
        self.btn_strt.config(state='disabled')
        
        self.lab2.clear()
        for i in range(1,17):
            lab=[x for x in self.lab if x['text']==['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',''][i-1]][0]
            lab.place_configure(x=94*((i-1)%4)+3,y=96*((i-1)//4)+1)
        self.order=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','']
        for i in self.order:
            lab=[x for x in self.lab if x['text'] == i][0]
            self.lab2.append(lab)

        self.lab.clear()
        self.lab.extend(self.lab2)
        self.lab_moves.config(text='Moves : 0')
        self.moves=0
        self.game.unbind_all('<ButtonRelease-1>')
        self.btn_rest.config(state='normal')
        self.btn_strt.config(state='normal')
        
    def winner(self):
        if self.order==['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','']:

            return True
        return False

    def shuffle(self):
        self.btn_rest.config(state='disabled')
        self.btn_strt.config(state='disabled')
        
        self.image_label.config(image=self.side_image)
        self.game.unbind_all('<ButtonRelease-1>')
        prev_dir=14
        self.lab_moves.config(text='Moves : 0')
        self.moves=0
        for i in range(40):
            empty = self.order.index('')
            movable=[empty+1,empty-1,empty+4,empty-4]
            if empty in [3,7,11,15]:
                movable.remove(empty+1)
            if empty in [4,8,12,0]:
                movable.remove(empty-1)
            if empty in [1,2,3,0]:
                movable.remove(empty-4)
            if empty in [12,13,14,15]:
                movable.remove(empty+4)
            move=random.choice(movable)
            while prev_dir==move:
                move=random.choice(movable)
            move1=self.lab[move]
            empty1=self.lab[empty]
            try:
                functions.swap(self.game,move1,empty1,ttime=0.05,crt_x=10,crt_y=10,n=4)
                self.lab[move],self.lab[empty]=self.lab[empty],self.lab[move]
                self.order[move],self.order[empty]=self.order[empty],self.order[move]
                prev_dir=empty
            except:pass
        
        self.game.bind_all('<ButtonRelease-1>',self.check)

        self.btn_rest.config(state='normal')
        self.btn_strt.config(state='normal')

    def new_high_score(self):
        prev_high=self.con.get('puzzle')
        if prev_high[1] == None:
            self.con.update('puzzle',self.username,self.moves)
            
            mb.showinfo('New high score!!',f'You set a new high score\nYour HighScore - {self.moves}')
        elif self.moves<prev_high[1]:
            self.con.update('puzzle',self.username,self.moves)
            
            mb.showinfo('New high score!!',f'You beat the previous highscore\nPrev HighScore - {prev_high[1]}\nYour HighScore - {self.moves}')
        self.master.do_task('puzzle')
            
    def check(self,event):
        if event.widget in self.lab:
            number=event.widget['text']
            if number=='':
                return 
        else:return
        
        self.game.unbind_all('<ButtonRelease-1>')
        number_index=self.order.index(number)
        move_dir=None
        try:
            if self.order[number_index+1]=='' and (number_index+1)%4!=0:
                toswap=number_index+1
                move_dir='r'
        except:pass
        try:
            if self.order[number_index-1]=='' and number_index%4 !=0:
                toswap=number_index-1
                move_dir='l'
        except:pass
        try:
            if self.order[number_index+4]=='':
                toswap=number_index+4
                move_dir='d'
        except:pass
        
        try:
            if self.order[number_index-4]=='':
                toswap=number_index-4
                move_dir='u'
        except:pass
        self.game.update()
        if move_dir in ['l','r','u','d']:
            blank=[i for i in self.game.place_slaves() if i['text']==''][0]
            functions.swap(self.game,blank,event.widget,ttime=0.03,crt_x=10,crt_y=10)
            self.order[number_index],self.order[toswap]=self.order[toswap],self.order[number_index]
            self.lab[number_index],self.lab[toswap]=self.lab[toswap],self.lab[number_index]
            self.moves+=1
            self.lab_moves.config(text=f'Moves : {self.moves}')
        if not self.winner():
            self.image_label.config(image=self.side_image)
            self.game.bind_all('<ButtonRelease-1>',self.check)
        else:
            self.image_label.config(image=self.side_image2)
            if self.username != 'DEV-BUILD':
                self.new_high_score()

if __name__=='__main__':
    tk=Tk()
    tk.geometry('702x502')
    b=Puzzle(tk,'DEV-BUILD',_sql.Connection())
    b.place(x=1,y=1)





























