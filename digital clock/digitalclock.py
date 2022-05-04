
# program made by ABDULLAAH ALQAASIM 
# DONT FORGET TO GIVE CREDIT  
"""
digital clock implementation by ABDULLAAH ALQAASIM
 
Linked in  @abdullaah alqaasim :  https://www.linkedin.com/in/abdullaah-alqaasim-30b960209/
Instagram @abdullaah_alqaasim: https://www.instagram.com/abdullaah_alqaasim/ 
Github: https://github.com/AbdullaahAlqaasim 
"""




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



