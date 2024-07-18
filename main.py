import customtkinter as ctk
from tkinter import Tk
from tkinter import font
# from PIL import ImageFont


class App(ctk.CTk):
    
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("To-Do")
        self.root.minsize(400, 600)
        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        self.main_frame = ctk.CTkFrame(self.root, fg_color='#A68866')
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        #Initializing the loop
        self.root.mainloop()
        
    
    
    
#Starting the app    
if __name__ == "__main__":
    app = App()