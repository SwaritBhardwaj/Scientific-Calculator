#IMPORTING LIBRARIES
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
from math import sin, cos, tan, pi

#CREATING CONSTANTS
font1=('Arial', 14, 'bold')
font2=('Arial', 12)
rowNum = 0
columnNum = 0
str1 = ""
str2 = ""
i = 0

#MAKING A PARENT WINDOW
root=tk.ThemedTk()
root.title('Calculator')
root.get_themes()
root.set_theme("plastik")

#CREATING STYLES
numeralStyle = ttk.Style()
numeralStyle.configure("NS.TButton",font = font1)

sciStyle = ttk.Style()
sciStyle.configure("SS.TButton", font = font2, foreground = 'blue')

displayStyle = ttk.Style()
displayStyle.configure("DS.TButton", font = font1)

#DEFINING FUNCTIONS
def evaluate(event):
    if event.widget['text'] == "Evaluate":
        try:
            Input = calcDisplay.get()
            calcDisplay.delete(0,END)
            function = list(Input)
            print(function)
            #COMPUTING FOR SIN
            if 'i' in function:
                x = function.index('i')
                string = (str1.join(function[:x+3])+str(pi/180)+"*"+ str2.join(function[x+3:]))                
                print(string)
                Output = eval(str(string))
                calcDisplay.insert(END, str(Output))
            #COMPUTING FOR COS
            elif 'c' in function:
                i = function.index('c')
                string = (str1.join(function[:i+4])+str(pi/180)+"*"+ str2.join(function[i+4:]))                
                print(string)
                Output = eval(str(string))
                calcDisplay.insert(END, str(Output))
            #COMPUTING FOR TAN
            elif 't' in function:
                i = function.index('t')
                string = (str1.join(function[:i+4])+str(pi/180)+"*"+ str2.join(function[i+4:]))
                print(string)
                Output = eval(str(string))
                calcDisplay.insert(END, str(Output))
            #GENERAL EVALUATION    
            else:
                Output = eval(Input)
                calcDisplay.insert(END, str(Output))
        except EXCEPTION as error:
            messagebox.error("error", error)

    #FNC FOR PI
    elif event.widget['text'] == "pi ":
        try:
            calcDisplay.insert(END, str(pi))
        except Exception as error:
            messagebox.showerror("Error", error)

    #FNC. FOR CLEAR SCREEN        
    elif event.widget['text'] == "  Clear  ":
        try:
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear the screen?")
            if confirm == True:
                calcDisplay.delete(0,END)
        except EXCEPTION as error:
            messagebox.error("error", error)

    #FNC. FOR DISPLAYING SCIENTIFIC FRAME
    elif event.widget['text'] == "    V    " :
        try:
            buttonMode.grid_remove()
            
            buttonRevMode.bind("<Button-1>", evaluate)
            buttonRevMode.grid(row = 1, column = 4, columnspan = 2, padx = 20, pady = 15)
            numeralPad.forget()
            scientificPad.grid(row = 3, column = 0, columnspan = 6, padx = 10, pady = 10)
            numeralPad.grid(row = 4, column = 0, columnspan = 6, padx = 10, pady = 10)
        except Exception as error:
            messagebox.showerror("Error", error)

    #FNC. FOR HIDING SCIENTIFIC FRAME
    elif event.widget['text'] == "    ^    " :
        try:
            buttonRevMode.grid_remove()
            buttonMode.grid(row = 1, column =4, columnspan = 2, padx = 20, pady = 15)
            scientificPad.grid_remove()
            numeralPad.grid(row = 3, column = 0, columnspan = 6, padx = 10, pady = 10)        
        except Exception as error:
            messagebox.showerror("Error", error)
            
    #FNC. FOR DELETING LAST DIGIT
    elif event.widget['text'] == "DEL":
        try:
            input = calcDisplay.get()
            calcDisplay.delete(len(input)-1, END)
        except Exception as error:
            messagebox.showerror("Error", error)
            
    #FNC FOR TAKING INPUT FROM BUTTON WIDGETS
    else:
        try:
            calcDisplay.insert(END, event.widget['text'])
        except Exception as error:
            messagebox.showerror("Error", error)

            
#MAKING INPUT AREA DISPLAY
calcDisplay=Entry(root, width = 50, borderwidth=10, font=font1)
calcDisplay.grid(row=0, column=0, columnspan=6, padx=40, pady=10)

#CREATING BUTTON WIDGETS
buttonEval = Button(root,text = "Evaluate", font =font1, padx = 15, pady = 6, relief = 'ridge', activeforeground="LightSteelBlue3",  activebackground="black",fg = "white",bg = "green", border = 3)
buttonEval.bind("<Button-1>", evaluate)
buttonEval.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = 15)

buttonClr = Button(root, text = '  Clear  ',font =font1, padx = 15, pady = 6, relief = 'ridge', activeforeground="LightSteelBlue3",  activebackground="black",fg = "black",bg = "red", border = 3)
buttonClr.bind("<Button-1>", evaluate)
buttonClr.grid(row = 1, column = 2, columnspan = 2, padx = 20, pady = 15)

buttonMode = Button(root, text = "    V    ", font =font1, padx = 15, pady = 6, relief = 'ridge', activeforeground="LightSteelBlue3",  activebackground="black",fg = "black",bg = "cyan", border = 3)
buttonMode.bind("<Button-1>", evaluate)
buttonMode.grid(row = 1, column =4, columnspan = 2, padx = 20, pady = 15)

#CREATING FRAMES
numeralPad = ttk.Frame(root)
numeralPad.grid(row = 2, column = 0, columnspan = 6, padx = 10, pady = 10)
scientificPad = ttk.Frame(root)

#CREATING BUTTON WIDGETS IN FRAMES
# 1.NUMERAL FRAME
numberPad = [['7','8','9','/'],
             ['4','5','6','*'],
             ['1','2','3','-'],
             ['.','0','DEL','+']]

for row in numberPad:
    columnNum = 0
    for column in row:
        numButton = ttk.Button(numeralPad, text = column, style = "NS.TButton")
        numButton.bind("<Button-1>", evaluate)
        numButton.grid(row = rowNum, column = columnNum, padx = 8, pady = 10,ipadx=5, ipady=12)
        columnNum +=1
    rowNum+=1
    
# 2.SCIENTIFIC FRAME
sciPad = [['sin','cos','tan'],
          ['pi ','(',')']]
for row in sciPad:
    columnNum=0
    for column in row:
        sciButton = ttk.Button(scientificPad, text = column, style = "SS.TButton")
        sciButton.bind("<Button-1>", evaluate)
        sciButton.grid(row = rowNum, column = 2*columnNum, padx = 32, pady = 5, columnspan = 2, ipadx = 19, ipady = 3)
        columnNum +=1
    rowNum+=1   
buttonRevMode = Button(root, text = "    ^    ", font =font1, padx = 15, pady = 6, relief = 'ridge', activeforeground="LightSteelBlue3",  activebackground="black",fg = "black",bg = "cyan", border = 3)

root.mainloop()
