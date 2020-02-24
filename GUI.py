#GUI for the HVS
#Please update the date and time here so we can keep track of the newest copy:
#Version: Feb 24, 2020 15:27
#Changelog: packs reformatted to grid, Entry now throws an error if the value exceeds range 0 to 3000
#TODO:
#3)Begin implementing voltage ramp function
#3a)All the print functions should be formatted to a text box
#4)NOT URGENT - More comments
#5)Format py file to executable
from tkinter import *
import tkinter as tk
#from voltage_ramp import *

mainWindow = Tk()
#master window class
class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)

        self.master = master

        self.init_window()#main window and menu bar

        self.main_widgets()#objects that inhabit the main page
#global variable declarationshow to import functions from another python file
        self.errlbl = None
        self.errlbl2 = None
# use this function for menu bar and page title
    def init_window(self):
        self.master.title("HVS")

        #cascade menus
        #this only works if you keep the variable name as "menu"
        menu = Menu(mainWindow)
        mainWindow.config(menu = menu)

        #file cascade menu
        file_C = Menu(menu)
        file_C.add_command(label='Exit', command=self.close_window)
        menu.add_cascade(label='File', menu=file_C)
#this function defines the main page controls
    def main_widgets(self):
        #ramp voltage entry
        Label(mainWindow, text='Enter Desired Voltage: ').grid(row = 0)
        #Voltage Entry bar 
        self.v_Entry = Entry(mainWindow)
        self.v_Entry.grid(row = 0, column = 1)
        #Button to pass entry to ramp voltage function, as to not cause lag
        v_Activate = Button(mainWindow, text="Enter", command=self.ramp_Entry_Check)
        v_Activate.grid(row = 0, column = 2)
        #Text box that will read out what used to be printed to console
        self.text_box = Text(mainWindow,height=15,width=45)
        self.text_box.grid(row=3,column=1)
        self.text_box.insert(tk.END,'-----\nVoltage set to 0V...\n')
        self.text_box.insert(tk.END,'-----\nMax Current Set to 3.3 mA\n')
        self.text_box.insert(tk.END,'-----\n\n')
        self.text_box.configure(state='disabled')


#voltage ramp function 
    def r_Entry(self, goalVoltage):
        print(goalVoltage)

#this function will check if the entered value is an int, float, etc. then pass
#to voltage ramp function
#TODO: throw error if voltage exceeds the range of 0 - 3000 volts
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

                self.text_box.configure(state='normal')
                self.text_box.insert(tk.INSERT,'Error: Entry must be an Integer or Float\n')
                self.text_box.insert(tk.INSERT, '----------------\n')
                self.text_box.configure(state='disabled')
                check = False
        
        if check == True:
            if rampV < 0 or rampV > 3000:
                self.text_box.configure(state='normal')
                self.text_box.insert(tk.INSERT, "Error: Entry must be between 0V and 3000V\n")
                self.text_box.insert(tk.INSERT, '----------------\n')
                self.text_box.configure(state='disabled')
            else:
                self.r_Entry(rampV)
                self.text_box.configure(state='normal')
                self.text_box.insert(tk.INSERT,'Voltage entry: ' + str(rampV) + '\n')
                self.text_box.insert(tk.INSERT, '----------------\n')
                self.text_box.configure(state='disabled')
        
        
        
    def close_window(self):
        exit()

    # When ramp_Entry() is called with a valid voltage, print out info to text box
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
