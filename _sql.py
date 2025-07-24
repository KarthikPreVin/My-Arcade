
import pickle


class Connection:
    """creates a connection object for the game"""
    def __init__(self):
        self.userdata="userdata.dat"
        self.gamedata="gamedata.dat"
        self.temp=[]
        f=open(self.userdata,'a')
        f.close()
        try:
            f=open(self.gamedata)
        except FileNotFoundError:
            f=open(self.gamedata,'wb')
            for i in ['PUZZLE','TICTACTOE','MEMORYGAME','BOUNCE','COLOUR','SNAKE']:
                pickle.dump((i,None,None),f)
            
        
       
    def add(self,username,pwd):
        if self.check(username,pwd)==False:
            f=open(self.userdata,'ab')
            pickle.dump((username,pwd),f)
            f.close()
            return True
        else:
            return False
        
        

    def check(self,username,pwd):
        f=open(self.userdata,'rb')
        try:
            while True:
                d=pickle.load(f)
                if d[0].lower()==username.lower():
                    if d[1].lower()==pwd.lower():
                        return True##username pwd correct
                    else:
                        return None##username exist, incorrect pwd
        except:
            return False##username doesnt exist
        

    def update(self,game,name,score):
        f=open(self.gamedata,'rb')
        try:
            while True:
                d=pickle.load(f)
                if d[0].lower()==game.lower():
                    i=(game,name,score)
                    self.temp.append(i)
                else:
                    self.temp.append(d)
        except:
            f.close()

        f=open(self.gamedata,'wb')
        for j in self.temp:
            pickle.dump(j,f)
        f.close()
        print(self.temp)
        self.temp.clear()
        
            
                
        
        
    
    def get(self,game):
        f=open(self.gamedata,'rb')
        try:
            while True:
                d=pickle.load(f)
                if d[0].lower()==game.lower():
                    return d[1],d[2]

        except:
            f.close()
            return None,None

    def end(self):
        del self


'''

import mysql.connector as s
from tkinter import *
import tkinter.messagebox as mb


class Connection:
    """creates a connection object for the game"""
    def __init__(self):
        
        u,p='root','pkct8k6rxy'
        self.mc=s.connect(host='localhost',user=u,passwd=p)
        self.cr=self.mc.cursor()
            
        
        try:
            self.cr.execute('use arcade')
        except:
            print('creating database...')
            
            self.cr.execute('create database arcade')
            self.cr.execute('use arcade')
            self.cr.execute('create table login(username varchar(30),password varchar(30))')
            self.cr.execute('create table games(game varchar (15),name varchar(30),highscore int)')
            self.cr.execute('insert into games(game) values("PUZZLE"),("TICTACTOE"),("MEMORYGAME"),("BOUNCE"),("COLOUR"),("SNAKE")')
            self.mc.commit()
    
    def add(self,username,pwd):
        self.cr.execute(f'select * from login where username="{username}"')
        if len(self.cr.fetchall())==0:
            self.cr.execute(f'Insert into login values("{username}","{pwd}")')
            self.mc.commit()
            return True
        else:
            self.mc.rollback()
            return False
        

    def check(self,username,pwd):
        self.cr.execute(f'select password from login where username="{username}"')
        d=self.cr.fetchall()
        if len(d)==0:         ##no username
            return False
        else:
            if d[0][0]==pwd:  ##username and pwd correct
                return True
            else:             ##password wrong
                #print(d[0][0])
                return None

    def update(self,game,name,score):
        self.cr.execute(f'update games set name="{name}",highscore={score} where game="{game}"')
        self.mc.commit()
        
    
    def get(self,game):
        self.cr.execute(f'select * from games where game="{game}"')
        d=self.cr.fetchall()

        return d[0][1],d[0][2]

    def end(self):
        self.cr.close()
        self.mc.close()


'''
