from tkinter import *
from numpy import linspace
import time
import random

def move(master,widget,x2,y2,ttime=0.5):
    x1,y1=widget.winfo_rootx(),widget.winfo_rooty()
    l1=linspace(x1,x2)
    l2=linspace(y1,y2)
    for x,y in zip(l1,l2):
        widget.place_configure(x=int(x),y=int(y))
        master.update()
        time.sleep(ttime/50)

def swap(master,widget1,widget2,ttime=0.1,crt_x=0,crt_y=0,n=25):
    master.update()
    lx1=linspace(widget1.winfo_x()-crt_x,widget2.winfo_x()-crt_x,num=n)
    lx2=linspace(widget2.winfo_x()-crt_x,widget1.winfo_x()-crt_x,num=n)
    ly1=linspace(widget1.winfo_y()-crt_y,widget2.winfo_y()-crt_y,num=n)
    ly2=linspace(widget2.winfo_y()-crt_y,widget1.winfo_y()-crt_y,num=n)
    
    for i in range(n):
        widget1.place_configure(x=int(lx1[i]),y=int(ly1[i]))
        widget2.place_configure(x=int(lx2[i]),y=int(ly2[i]))
        master.update()

        time.sleep(ttime/n)
def intel_easy(status):
    return random.choice([i for i in range(len(status)) if status[i]==None])

def intel_medium(status):
    if status.count(None)%2==0:
        if status[0]=='O' and status[1]=='O':
            if status[2] == None:return 2
        if status[2]=='O' and status[1]=='O':
            if status[0] == None:return 0
        if status[0]=='O' and status[2]=='O':
            if status[1] == None:return 1
        
        if status[6]=='O' and status[8]=='O':
            if status[7] == None:return 7
        if status[7]=='O' and status[8]=='O':
            if status[6] == None:return 6
        if status[6]=='O' and status[7]=='O':
            if status[8] == None:return 8
        
        if status[0]=='O' and status[3]=='O':
            if status[6] == None:return 6
        if status[0]=='O' and status[6]=='O':
            if status[3] == None:return 3
        if status[3]=='O' and status[6]=='O':
            if status[0] == None:return 0
        
        if status[2]=='O' and status[5]=='O':
            if status[8] == None:return 8
        if status[5]=='O' and status[8]=='O':
            if status[2] == None:return 2
        if status[2]=='O' and status[8]=='O':
            if status[5] == None:return 5

        if status[1]=='O' and status[4]=='O':
            if status[7] == None:return 7
        if status[7]=='O' and status[4]=='O':
            if status[1] == None:return 1
        if status[1]=='O' and status[7]=='O':
            if status[4] == None:return 4

        if status[3]=='O' and status[4]=='O':
            if status[5] == None:return 5
        if status[5]=='O' and status[4]=='O':
            if status[3] == None:return 3
        if status[3]=='O' and status[5]=='O':
            if status[4] == None:return 4

        if status[0]=='O' and status[4]=='O':
            if status[8] == None:return 8
        if status[8]=='O' and status[4]=='O':
            if status[0] == None:return 0
        if status[0]=='O' and status[8]=='O':
            if status[4] == None:return 4

        if status[6]=='O' and status[2]=='O':
            if status[4] == None:return 4
        if status[2]=='O' and status[4]=='O':
            if status[6] == None:return 6
        if status[6]=='O' and status[4]=='O':
            if status[2] == None:return 2


        if status[0]=='X' and status[1]=='X':
            if status[2] == None:return 2
        if status[2]=='X' and status[1]=='X':
            if status[0] == None:return 0
        if status[0]=='X' and status[2]=='X':
            if status[1] == None:return 1
        
        if status[6]=='X' and status[8]=='X':
            if status[7] == None:return 7
        if status[7]=='X' and status[8]=='X':
            if status[6] == None:return 6
        if status[6]=='X' and status[7]=='X':
            if status[8] == None:return 8
        
        if status[0]=='X' and status[3]=='X':
            if status[6] == None:return 6
        if status[0]=='X' and status[6]=='X':
            if status[3] == None:return 3
        if status[3]=='X' and status[6]=='X':
            if status[0] == None:return 0
        
        if status[2]=='X' and status[5]=='X':
            if status[8] == None:return 8
        if status[5]=='X' and status[8]=='X':
            if status[2] == None:return 2
        if status[2]=='X' and status[8]=='X':
            if status[5] == None:return 5

        if status[1]=='X' and status[4]=='X':
            if status[7] == None:return 7
        if status[7]=='X' and status[4]=='X':
            if status[1] == None:return 1
        if status[1]=='X' and status[7]=='X':
            if status[4] == None:return 4

        if status[3]=='X' and status[4]=='X':
            if status[5] == None:return 5
        if status[5]=='X' and status[4]=='X':
            if status[3] == None:return 3
        if status[3]=='X' and status[5]=='X':
            if status[4] == None:return 4

        if status[0]=='X' and status[4]=='X':
            if status[8] == None:return 8
        if status[8]=='X' and status[4]=='X':
            if status[0] == None:return 0
        if status[0]=='X' and status[8]=='X':
            if status[4] == None:return 4

        if status[6]=='X' and status[2]=='X':
            if status[4] == None:return 4
        if status[2]=='X' and status[4]=='X':
            if status[6] == None:return 6
        if status[6]=='X' and status[4]=='X':
            if status[2] == None:return 2
        


    else:
        if status[0]=='X' and status[1]=='X':
            if status[2] == None:return 2
        if status[2]=='X' and status[1]=='X':
            if status[0] == None:return 0
        if status[0]=='X' and status[2]=='X':
            if status[1] == None:return 1
        
        if status[6]=='X' and status[8]=='X':
            if status[7] == None:return 7
        if status[7]=='X' and status[8]=='X':
            if status[6] == None:return 6
        if status[6]=='X' and status[7]=='X':
            if status[8] == None:return 8
        
        if status[0]=='X' and status[3]=='X':
            if status[6] == None:return 6
        if status[0]=='X' and status[6]=='X':
            if status[3] == None:return 3
        if status[3]=='X' and status[6]=='X':
            if status[0] == None:return 0
        
        if status[2]=='X' and status[5]=='X':
            if status[8] == None:return 8
        if status[5]=='X' and status[8]=='X':
            if status[2] == None:return 2
        if status[2]=='X' and status[8]=='X':
            if status[5] == None:return 5

        if status[1]=='X' and status[4]=='X':
            if status[7] == None:return 7
        if status[7]=='X' and status[4]=='X':
            if status[1] == None:return 1
        if status[1]=='X' and status[7]=='X':
            if status[4] == None:return 4

        if status[3]=='X' and status[4]=='X':
            if status[5] == None:return 5
        if status[5]=='X' and status[4]=='X':
            if status[3] == None:return 3
        if status[3]=='X' and status[5]=='X':
            if status[4] == None:return 4

        if status[0]=='X' and status[4]=='X':
            if status[8] == None:return 8
        if status[8]=='X' and status[4]=='X':
            if status[0] == None:return 0
        if status[0]=='X' and status[8]=='X':
            if status[4] == None:return 4

        if status[6]=='X' and status[2]=='X':
            if status[4] == None:return 4
        if status[2]=='X' and status[4]=='X':
            if status[6] == None:return 6
        if status[6]=='X' and status[4]=='X':
            if status[2] == None:return 2
        

        
        if status[0]=='O' and status[1]=='O':
            if status[2] == None:return 2
        if status[2]=='O' and status[1]=='O':
            if status[0] == None:return 0
        if status[0]=='O' and status[2]=='O':
            if status[1] == None:return 1
        
        if status[6]=='O' and status[8]=='O':
            if status[7] == None:return 7
        if status[7]=='O' and status[8]=='O':
            if status[6] == None:return 6
        if status[6]=='O' and status[7]=='O':
            if status[8] == None:return 8
        
        if status[0]=='O' and status[3]=='O':
            if status[6] == None:return 6
        if status[0]=='O' and status[6]=='O':
            if status[3] == None:return 3
        if status[3]=='O' and status[6]=='O':
            if status[0] == None:return 0
        
        if status[2]=='O' and status[5]=='O':
            if status[8] == None:return 8
        if status[5]=='O' and status[8]=='O':
            if status[2] == None:return 2
        if status[2]=='O' and status[8]=='O':
            if status[5] == None:return 5

        if status[1]=='O' and status[4]=='O':
            if status[7] == None:return 7
        if status[7]=='O' and status[4]=='O':
            if status[1] == None:return 1
        if status[1]=='O' and status[7]=='O':
            if status[4] == None:return 4

        if status[3]=='O' and status[4]=='O':
            if status[5] == None:return 5
        if status[5]=='O' and status[4]=='O':
            if status[3] == None:return 3
        if status[3]=='O' and status[5]=='O':
            if status[4] == None:return 4

        if status[0]=='O' and status[4]=='O':
            if status[8] == None:return 8
        if status[8]=='O' and status[4]=='O':
            if status[0] == None:return 0
        if status[0]=='O' and status[8]=='O':
            if status[4] == None:return 4

        if status[6]=='O' and status[2]=='O':
            if status[4] == None:return 4
        if status[2]=='O' and status[4]=='O':
            if status[6] == None:return 6
        if status[6]=='O' and status[4]=='O':
            if status[2] == None:return 2

    return random.choice([i for i in range(len(status)) if status[i]==None])

def intel_impossible(status):
    possible=[i for i in range(len(status)) if status[i]==None]
    
    
    
    if not any(status):
        return 4
    else:
        if status[4]==None:
            return 4
        else:
            if status.count(None)%2==0:
                if status[0]=='O' and status[1]=='O':
                    if status[2] == None:return 2
                if status[2]=='O' and status[1]=='O':
                    if status[0] == None:return 0
                if status[0]=='O' and status[2]=='O':
                    if status[1] == None:return 1
                
                if status[6]=='O' and status[8]=='O':
                    if status[7] == None:return 7
                if status[7]=='O' and status[8]=='O':
                    if status[6] == None:return 6
                if status[6]=='O' and status[7]=='O':
                    if status[8] == None:return 8
                
                if status[0]=='O' and status[3]=='O':
                    if status[6] == None:return 6
                if status[0]=='O' and status[6]=='O':
                    if status[3] == None:return 3
                if status[3]=='O' and status[6]=='O':
                    if status[0] == None:return 0
                
                if status[2]=='O' and status[5]=='O':
                    if status[8] == None:return 8
                if status[5]=='O' and status[8]=='O':
                    if status[2] == None:return 2
                if status[2]=='O' and status[8]=='O':
                    if status[5] == None:return 5

                if status[1]=='O' and status[4]=='O':
                    if status[7] == None:return 7
                if status[7]=='O' and status[4]=='O':
                    if status[1] == None:return 1
                if status[1]=='O' and status[7]=='O':
                    if status[4] == None:return 4

                if status[3]=='O' and status[4]=='O':
                    if status[5] == None:return 5
                if status[5]=='O' and status[4]=='O':
                    if status[3] == None:return 3
                if status[3]=='O' and status[5]=='O':
                    if status[4] == None:return 4

                if status[0]=='O' and status[4]=='O':
                    if status[8] == None:return 8
                if status[8]=='O' and status[4]=='O':
                    if status[0] == None:return 0
                if status[0]=='O' and status[8]=='O':
                    if status[4] == None:return 4

                if status[6]=='O' and status[2]=='O':
                    if status[4] == None:return 4
                if status[2]=='O' and status[4]=='O':
                    if status[6] == None:return 6
                if status[6]=='O' and status[4]=='O':
                    if status[2] == None:return 2


        
                if status[0]=='X' and status[1]=='X':
                    if status[2] == None:return 2
                if status[2]=='X' and status[1]=='X':
                    if status[0] == None:return 0
                if status[0]=='X' and status[2]=='X':
                    if status[1] == None:return 1
                
                if status[6]=='X' and status[8]=='X':
                    if status[7] == None:return 7
                if status[7]=='X' and status[8]=='X':
                    if status[6] == None:return 6
                if status[6]=='X' and status[7]=='X':
                    if status[8] == None:return 8
                
                if status[0]=='X' and status[3]=='X':
                    if status[6] == None:return 6
                if status[0]=='X' and status[6]=='X':
                    if status[3] == None:return 3
                if status[3]=='X' and status[6]=='X':
                    if status[0] == None:return 0
                
                if status[2]=='X' and status[5]=='X':
                    if status[8] == None:return 8
                if status[5]=='X' and status[8]=='X':
                    if status[2] == None:return 2
                if status[2]=='X' and status[8]=='X':
                    if status[5] == None:return 5

                if status[1]=='X' and status[4]=='X':
                    if status[7] == None:return 7
                if status[7]=='X' and status[4]=='X':
                    if status[1] == None:return 1
                if status[1]=='X' and status[7]=='X':
                    if status[4] == None:return 4

                if status[3]=='X' and status[4]=='X':
                    if status[5] == None:return 5
                if status[5]=='X' and status[4]=='X':
                    if status[3] == None:return 3
                if status[3]=='X' and status[5]=='X':
                    if status[4] == None:return 4

                if status[0]=='X' and status[4]=='X':
                    if status[8] == None:return 8
                if status[8]=='X' and status[4]=='X':
                    if status[0] == None:return 0
                if status[0]=='X' and status[8]=='X':
                    if status[4] == None:return 4

                if status[6]=='X' and status[2]=='X':
                    if status[4] == None:return 4
                if status[2]=='X' and status[4]=='X':
                    if status[6] == None:return 6
                if status[6]=='X' and status[4]=='X':
                    if status[2] == None:return 2

                if status.count('X')==1:
                    if status[4]==None:return 4
                    else:return random.choice([0,2,6,8])
                elif status.count('X')==2:
                    if status[4]=='O':
                        if 'X' not in [status[1],status[3],status[5],status[7]]:
                            #both 'x' in corners diagonal
                            return random.choice([1,3,5,7])
                        elif [status[1],status[3],status[5],status[7]].count('X')==2:
                            #- X -
                            #X O -
                            #- - - any except 8
                            if status[1]=='X' and status[3]=='X':return random.choice([0,2,6])
                            elif status[1]=='X' and status[5]=='X':return random.choice([0,2,8])
                            elif status[7]=='X' and status[3]=='X':return random.choice([0,8,6])
                            elif status[5]=='X' and status[7]=='X':return random.choice([8,2,6])
                            else:return random.choice([0,2,6,8])#win
                        elif [status[1],status[3],status[5],status[7]].count('X')==1:
                            if status[0]=='X':return 8
                            elif status[8]=='X':return 0
                            elif status[2]=='X':return 6
                            elif status[6]=='X':return 2
                    else:
                        if status[0]=='O' and status[8]=='X':return random.choice([2,6])
                        elif status[8]=='O' and status[0]=='X':return random.choice([2,6])
                        elif status[2]=='O' and status[6]=='X':return random.choice([0,8])
                        elif status[6]=='O' and status[2]=='X':return random.choice([0,8])
    
                        
                            
            else:
                if status[0]=='X' and status[1]=='X':
                    if status[2] == None:return 2
                if status[2]=='X' and status[1]=='X':
                    if status[0] == None:return 0
                if status[0]=='X' and status[2]=='X':
                    if status[1] == None:return 1
                
                if status[6]=='X' and status[8]=='X':
                    if status[7] == None:return 7
                if status[7]=='X' and status[8]=='X':
                    if status[6] == None:return 6
                if status[6]=='X' and status[7]=='X':
                    if status[8] == None:return 8
                
                if status[0]=='X' and status[3]=='X':
                    if status[6] == None:return 6
                if status[0]=='X' and status[6]=='X':
                    if status[3] == None:return 3
                if status[3]=='X' and status[6]=='X':
                    if status[0] == None:return 0
                
                if status[2]=='X' and status[5]=='X':
                    if status[8] == None:return 8
                if status[5]=='X' and status[8]=='X':
                    if status[2] == None:return 2
                if status[2]=='X' and status[8]=='X':
                    if status[5] == None:return 5

                if status[1]=='X' and status[4]=='X':
                    if status[7] == None:return 7
                if status[7]=='X' and status[4]=='X':
                    if status[1] == None:return 1
                if status[1]=='X' and status[7]=='X':
                    if status[4] == None:return 4

                if status[3]=='X' and status[4]=='X':
                    if status[5] == None:return 5
                if status[5]=='X' and status[4]=='X':
                    if status[3] == None:return 3
                if status[3]=='X' and status[5]=='X':
                    if status[4] == None:return 4

                if status[0]=='X' and status[4]=='X':
                    if status[8] == None:return 8
                if status[8]=='X' and status[4]=='X':
                    if status[0] == None:return 0
                if status[0]=='X' and status[8]=='X':
                    if status[4] == None:return 4

                if status[6]=='X' and status[2]=='X':
                    if status[4] == None:return 4
                if status[2]=='X' and status[4]=='X':
                    if status[6] == None:return 6
                if status[6]=='X' and status[4]=='X':
                    if status[2] == None:return 2
                

                
                if status[0]=='O' and status[1]=='O':
                    if status[2] == None:return 2
                if status[2]=='O' and status[1]=='O':
                    if status[0] == None:return 0
                if status[0]=='O' and status[2]=='O':
                    if status[1] == None:return 1
                
                if status[6]=='O' and status[8]=='O':
                    if status[7] == None:return 7
                if status[7]=='O' and status[8]=='O':
                    if status[6] == None:return 6
                if status[6]=='O' and status[7]=='O':
                    if status[8] == None:return 8
                
                if status[0]=='O' and status[3]=='O':
                    if status[6] == None:return 6
                if status[0]=='O' and status[6]=='O':
                    if status[3] == None:return 3
                if status[3]=='O' and status[6]=='O':
                    if status[0] == None:return 0
                
                if status[2]=='O' and status[5]=='O':
                    if status[8] == None:return 8
                if status[5]=='O' and status[8]=='O':
                    if status[2] == None:return 2
                if status[2]=='O' and status[8]=='O':
                    if status[5] == None:return 5

                if status[1]=='O' and status[4]=='O':
                    if status[7] == None:return 7
                if status[7]=='O' and status[4]=='O':
                    if status[1] == None:return 1
                if status[1]=='O' and status[7]=='O':
                    if status[4] == None:return 4

                if status[3]=='O' and status[4]=='O':
                    if status[5] == None:return 5
                if status[5]=='O' and status[4]=='O':
                    if status[3] == None:return 3
                if status[3]=='O' and status[5]=='O':
                    if status[4] == None:return 4

                if status[0]=='O' and status[4]=='O':
                    if status[8] == None:return 8
                if status[8]=='O' and status[4]=='O':
                    if status[0] == None:return 0
                if status[0]=='O' and status[8]=='O':
                    if status[4] == None:return 4

                if status[6]=='O' and status[2]=='O':
                    if status[4] == None:return 4
                if status[2]=='O' and status[4]=='O':
                    if status[6] == None:return 6
                if status[6]=='O' and status[4]=='O':
                    if status[2] == None:return 2

                    
                if status.count('X') == 1:
                    if 'O' == status[1]:
                        return random.choice([6,8])#win
                    elif 'O' == status[3]:
                        return random.choice([2,8])#win
                    elif 'O' == status[5]:
                        return random.choice([0,6])#win
                    elif 'O' == status[7]:
                        return random.choice([0,2])#win
                    elif 'O' == status[0]:
                        return 8
                    elif 'O' == status[8]:
                        return 0
                    elif 'O' == status[6]:
                        return 2
                    elif 'O' == status[2]:
                        return 6
                elif status.count('X')==2:
                    if status[0]=='O':
                        if status[5]=='O':
                            return 6
                        elif status[7]=='O':
                            return 2
                    elif status[2]=='O':
                        if status[3]=='O':
                            return 8
                        elif status[7]=='O':
                            return 0
                    elif status[6]=='O':
                        if status[5]=='O':
                            return 0
                        elif status[1]=='O':
                            return 8
                    elif status[8]=='O':
                        if status[1]=='O':
                            return 6
                        elif status[3]=='O':
                            return 2
                
    return random.choice(possible)
                    
                
