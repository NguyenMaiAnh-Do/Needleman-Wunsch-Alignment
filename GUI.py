#CREATING THE GUI BY TNINTER LIBRARY

from tkinter import *
import NW 
import re

class NotDNAseq(Exception):
    pass
class NotNumber(Exception):
    pass
class NotNegativeNum(Exception):
    pass

def Take_input():
    INPUT1 = inputtxt1.get("1.0", "end-1c").upper()
    INPUT2 = inputtxt2.get("1.0", "end-1c").upper()
    INPUT3 = inputtxt3.get("1.0", "end-1c")
    INPUT4 = inputtxt4.get("1.0", "end-1c")
    INPUT5 = inputtxt5.get("1.0", "end-1c")

    validated_inputs = True
    #sequence 1
    try:
        match = re.search(r"[^ATCG]", INPUT1)
        if match:
            raise NotDNAseq
    except NotDNAseq:
        Output.insert(END,"Sequence 1 is not a DNA sequence, please clear and insert again \n")
        validated_inputs = False
    #sequence 2
    try:
        match = re.search(r"[^ATCG]", INPUT2)
        if match:
            raise NotDNAseq
    except NotDNAseq:
        Output.insert(END,"Sequence 2 is not a DNA sequence, please clear and insert again \n")
        validated_inputs = False

    #gap penalty    
    try:
        value3 = int(INPUT3)
        if value3 >=0:
            raise NotNegativeNum
    except ValueError:
        Output.insert(END, "Gap Penalty is not a number, please clear and insert again \n" )
        validated_inputs = False
    except NotNegativeNum:
        Output.insert(END, "Gap Penalty has to be a negative number, please clear and insert again \n" )
        validated_inputs = False   

    #match  
    try:
        if not INPUT4.isnumeric():
            raise NotNumber
    except NotNumber:
        Output.insert(END, "Match score is not a number, please clear and insert again \n" )
        validated_inputs = False

    #mismatch
    
    try:
        value5 = int(INPUT5)
        if value5 > 0:
            raise NotNegativeNum
    except ValueError:
        Output.insert(END, "Mismatch score is not a number, please clear and insert again \n" )
        validated_inputs = False
    except NotNegativeNum:
        Output.insert(END, "Mismatch score has to be a non positive number, please clear and insert again \n" )
        validated_inputs = False  
        

    if validated_inputs:
        Output.insert(END, NW.get_align(INPUT1,INPUT2))
root = Tk()
root.geometry("600x600")
root.title("Needleman-Wunsch Sequencing ")
 

    
     
l1 = Label(text = "Insert DNA sequence 1 ")
l2 = Label(text = "Insert DNA sequence 2")
l3 = Label(text = "Insert Gap Penalty")
l4 = Label(text = "Insert Match Score")
l5 = Label(text = "Insert Mismatch Score")

inputtxt1 = Text(root, height = 5,
                width = 50,
                bg = "light yellow")
inputtxt2 = Text(root, height = 5,
                width = 50,
                bg = "light yellow")
inputtxt3 = Text(root, height = 1,
                width = 25,
                bg = "light yellow")
inputtxt4 = Text(root, height = 1,
                width = 25,
                bg = "light yellow")
inputtxt5 = Text(root, height = 1,
                width = 25,
                bg = "light yellow")

 
Output = Text(root, height = 10,
              width = 50,
              bg = "light cyan")
 
Display = Button(root, height =2,
                 width = 20,
                 text ="Sequencing...",
                 command = lambda:Take_input())
 
l1.pack()
inputtxt1.pack()
l2.pack()
inputtxt2.pack()
l3.pack()
inputtxt3.pack()
l4.pack()
inputtxt4.pack()
l5.pack()
inputtxt5.pack()
Display.pack()
Output.pack()
 
mainloop()
