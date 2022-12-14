import tkinter as tk
from tkinter import*
import tkinter.filedialog
import os
import shutil
import datetime as dt
import time



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #title of GUI window
        self.master.title("File Transfer")
        #Creates button to select files from the source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in the GUI using tkinter grid()padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column = 1, columnspan = 2, padx=(20,10), pady=(30, 0))

        
        #Creates button to select destination of file from the destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions source button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in the GUI using tkinter grid()padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column = 1, columnspan = 2, padx=(20,10), pady=(15, 10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #postions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))



    #Creates function to slect source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0,END) will clear that is inserted in the entry widget
        #this allows the path to be inserted in the entry widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

       


    #Creates function to select destination directory.
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

            
        
    #Creates function to transfer files from one directory to the other
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #Gets destintaion directory
        destination =  self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #getting current timestamp
        current_timestamp = dt.datetime.now()
        #created timedelta of 24 hours in seconds
        delta = dt.timedelta(seconds=86400)
        #created variable of that subtracts 24 hours from current timestamp
        x = current_timestamp - delta
    
        
        #Runs through each file in source directory
        for i in source_files:
            #joining path of files to i
            path = os.path.join(source, i)
            #created if statement to compare modifcation timestamp to timestamp from 24 hours before current time 
            if dt.datetime.fromtimestamp(os.path.getmtime(path)) > x:
                #moves each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

            

    #Creates function to exit the program
    def exit_program(self):
        #root is the ain GUI window the tkinter destroy method
        #tells prython to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


