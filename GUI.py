#GUI for the HVS
#Please update the date and time here so we can keep track of the newest copy:
#Version: Feb 24, 2020 13:00
#TODO:
#2)Error for voltage range
#3)Begin implementing voltage ramp function
#3a)All the print functions should be formatted to a text box
#4)NOT URGENT - More comments
from tkinter import *
import tkinter as tk

mainWindow = Tk()
#master window class
class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)

        self.master = master

        #self.pack()#this aligns the widgets

        self.init_window()#main window and menu bar

        self.main_widgets()#objects that inhabit the main page
#global variable declarations
        self.errlbl = None
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
        #Entry bar 
        self.v_Entry = Entry(mainWindow)
        self.v_Entry.grid(row = 0, column = 1)
        #Button to pass entry to ramp voltage function, as to not cause lag
        v_Activate = Button(mainWindow, text="Enter", command=self.ramp_Entry)
        v_Activate.grid(row = 0, column = 2)

#this function will check if the entered value is an int, float, etc. then pass
#to voltage ramp function
#TODO: throw error if voltage exceeds the range of 0 - 3000 volts
    def ramp_Entry(self):
        rampV = self.v_Entry.get()
        try:#check if int
            int(rampV)
            if self.errlbl:
                self.errlbl.destroy()
        except:
            try:#check if float
                float(rampV)
                if self.errlbl:
                    self.errlbl.destroy()
            except:
                if self.errlbl:
                    self.errlbl.destroy()
                self.errlbl = Label(mainWindow, text = 'Error: Entry must be an Integer or Float')
                self.errlbl.grid(row = 1)
        #if rampV < 0 or rampV > 3000:
            #errlbl2 = Label(mainWindow, text = "Error: Entry must be between 0V and 3000V").grid(row = 2)

    def close_window(self):
        exit()


#initial size of window:
mainWindow.geometry("400x300")

app = Window(mainWindow)
#mainloop stays at the end
mainWindow.mainloop()
