from tkinter import *
from PIL import ImageTk, Image

class Colourwheel(Label):#light cyan(e0ffff),red,green,blue,yellow,size=120x120
    def __init__(self,master):
        self.master=master
        self.image=Image.open(r'wheel.png')
        self.angle=45
        self.colour='blue'
        #self.rotated=self.image.rotate(25,fillcolor = (224,255,255))
        self.img=ImageTk.PhotoImage(self.image)
        super().__init__(master,bd=0,bg='light cyan',image=self.img)
        self.master.update_idletasks()

    def rotate(self):
        self.angle+=7
        self.colour=['blue','green','red','yellow'][(self.angle%360)//90]
        self.rotated=self.image.rotate(self.angle-45,fillcolor = (224,255,255))
        self.img=ImageTk.PhotoImage(self.rotated)
        self.config(image=self.img)
        self.master.update_idletasks()
 
if __name__=='__main__':

    tk=Tk()
    tk.config(bg='light cyan')
    tk.geometry('220x220')
    c=Colourwheel(tk)
    c.place(x=100,y=100)
    
    import time

    def test():
        colour=['blue','green','red','yellow'][(c.angle%360)//90]
        print(colour)
        for i in range(100):
            c.rotate()
            prev=colour
            colour=['blue','green','red','yellow'][(c.angle%360)//90]
            if prev!=colour:
                print(colour)
            time.sleep(0.02)
            
    Button(tk,command=test,bg='black',fg='white',text='Click Me!').place(x=50,y=50)
    tk.mainloop()
        
