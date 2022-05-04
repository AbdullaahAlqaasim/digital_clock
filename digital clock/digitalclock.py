from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("abdullaah alqaasim clock ")


def time():
    string = strftime('%I:%M:%S %p \n %D \n%A')
    Label.config(text=string)
    Label.after(1000, time,)
    #add H for 24H time ,I for non 24 HRS
    # string = strftime('%I:%M:%S %p \n %D \n%A:%Y')


Label = Label(root, font=("ds-digital", 90), background="black", foreground="BLACK")
Label.pack(anchor='center')
time()

mainloop()


# program made by ABDULLAAH ALQAASIM 
# DONT FORGET TO GIVE CREDIT  

#my github 
#https://github.com/AbdullaahAlqaasim

#my instagram 
#https://www.instagram.com/abdullaah_alqaasim/

#my linked in 
#https://www.linkedin.com/in/abdullaah-alqaasim-30b960209/

