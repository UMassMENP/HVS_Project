#GUI for the HVS
#Please update the date and time here so we can keep track of the newest copy:
#Version: Feb 25, 2020 12:52
#TODO:
#3)Continue implementing voltage ramp function
#3a)All the print functions should be formatted to a text box
#3b)Implement functions and prep for hardware test
#5)Format py file to executable - last step
#6)NOT URGENT - ENTER/RETURN key functionality
#7)Scroll bar to text box for ease
from tkinter import *
import tkinter as tk
#from voltage_ramp import * #do not uncomment until hardware test

mainWindow = Tk()
#master window class
class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)

        self.master = master

        self.init_window()#main window and menu bar

        self.main_widgets()#objects that inhabit the main page
# use this function for menu bar and page title
    def init_window(self):
        self.master.title("HVS")

        #cascade menus
        #this only works if you keep the variable name as "menu"
        menu = Menu(mainWindow)
        mainWindow.config(menu = menu)
#all menu functions require the command passed from a seperate function
        #file cascade menu 
        file_C = Menu(menu)
        file_C.add_command(label='Exit', command=self.close_window)
        menu.add_cascade(label='File', menu=file_C)

#this function defines the main page controls
    def main_widgets(self):
        #ramp voltage entry
        Label(mainWindow, text='Enter Desired Voltage: ').grid(row = 0)
        #Voltage Entry user input
        self.v_Entry = Entry(mainWindow)
        self.v_Entry.grid(row = 0, column = 1)
        #Button to pass entry to ramp voltage function, as to not cause lag
        v_Activate = Button(mainWindow, text="Enter", command=self.ramp_Entry_Check)
        v_Activate.grid(row = 0, column = 2)
        #Text box that will read out what used to be printed to console
        self.text_box = Text(mainWindow,height=15,width=45)
        self.text_box.grid(row=3,column=1)
        self.text_box.insert(tk.INSERT,'-----\n\n')
        self.text_box.configure(state='disabled')


#voltage ramp function
    def r_Entry(self, goalVoltage):
        print(goalVoltage)
        #voltage_ramp(goalVoltage)
        self.text_box.configure(state = "normal")
        self.text_box.insert(tk.END,'Voltage start at 0 V...\n')
        self.text_box.insert(tk.END,'-----------\n')
        self.text_box.insert(tk.END,'Max Current Set to 3.3 mA\n')
        self.text_box.insert(tk.END,'-----------\n')
        self.text_box.configure(state='disabled')
        

#this function will check if the entered value is an int, float, etc. then pass
#to voltage ramp function
    def ramp_Entry_Check(self):
        rampV = self.v_Entry.get()
        check = None
        try:#check if int
            rampV = int(rampV)
            check = True
        except:
            try:#check if float
                rampV = float(rampV)
                check = True
            except:#if the input is not a float or int, it fails
                self.text_box.configure(state='normal')#to add config must be turned on
                self.text_box.insert(tk.END,'Error: Entry must be an Integer or Float\n')
                self.text_box.insert(tk.END, '----------------\n')
                self.text_box.configure(state='disabled')#turned off to prevent user input in text box
                check = False
        if check == True:#check if voltage is in the desired range
            if rampV < 0 or rampV > 3000:
                self.text_box.configure(state='normal')
                self.text_box.insert(tk.END, "Error: Entry must be between 0V and 3000V\n")
                self.text_box.insert(tk.END, '----------------\n')
                self.text_box.configure(state='disabled')
            else:
                self.r_Entry(rampV)#print entry voltage to text box
                self.text_box.configure(state='normal')
                self.text_box.insert(tk.END,'Voltage increasing to : ' + str(rampV) + '\n')
                self.text_box.insert(tk.END, '----------------\n')
                self.text_box.configure(state='disabled')        
#menu functions
    def close_window(self):
        exit()
#When ramp_Entry() is called with a valid voltage, print out info to text box
    def ramp_print_entry(self,voltage):
        self.text_box.configure(state='normal')
        self.text_box.insert(tk.END,'----------------\n')
        self.text_box.insert(tk.END,'Voltage (0 to 3000 V): ' + str(voltage) + '\n')
        self.text_box.insert(tk.END,'----------------\n')
        self.text_box.configure(state='disabled')

#initial size of window:
mainWindow.geometry("600x300")

app = Window(mainWindow)


#mainloop stays at the end
mainWindow.mainloop()
