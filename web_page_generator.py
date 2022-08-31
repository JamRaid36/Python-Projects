import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column = 4, padx=(0,250) , pady=(15,10), sticky=SE)
        # This creates and places the submit custom text button in our GUI
        # it also add the command which activates our customHTML function
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=3, column = 4, padx=(0,10) , pady=(15,10), sticky=SE)
        # This creates an entry box for custom text that will be used on
        # on the custom text basic web page.
        self.customText = Entry(width=125)
        self.customText.grid(row=1, column = 1, columnspan = 4, padx=(10,10), pady=(10, 0))

        self.lblCustomText = Label(self.master, text='Enter custom text or click the Default HTML page button', font= ("Helvetica", 9), fg='black')
        self.lblCustomText.grid(row=0,column=1, columnspan = 4, padx=(6,0),pady=(20, 0), sticky=NW)

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        #this function opens a new basic web page and utilizes
        #the .get() function add custom the custom text provided in the entry box 
        htmlText = self.customText.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
        
        
        






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
