import tkinter as tk 
from tkinter import ttk 
import os
from subprocess import PIPE,run

class FileManager():
    def CreateNested(self,lst_folder_files):
        for FolderFiles in lst_folder_files:
            if not  lst_folder_files=="fim" and lst_folder_files=="nested ":
                if not "." in FolderFiles:
                    os.mkdir(fi)
                else:
                    os/
                os.chdir(f"{os.getcwd()}\\{FolderFiles}")     
                                    

class GUI(tk.Tk):
    pass

class CLI(tk.Tk,FileManager):
    
    def __init__(self):
        super().__init__()
        self._cursr_pos=None
        self._firstcmdcrsr_pos=None
        self._width=680
        self._height=320
        self._icon=None
        self._version=0.01
        self._title=f"{os.getcwd() }  -fim CLI"
        self._firstpath_cursor=4.0
        self._lastpath_cursor=None
        self.Window()    
    
    def Window(self):
        self.geometry(f"{self._width}x{self._height}")
        self.title(self._title)
        self.minsize(self._width,self._height)
        self.maxsize(self._width,self._height)
        self.Textarea()

    def Textarea(self):
        scrlbr=ttk.Scrollbar(self)
        scrlbr.pack(side=tk.RIGHT,fill=tk.Y)
        self.txtwidget=tk.Text(self,bg="black",fg="white",font=("Lucida Console",10,"bold"),insertbackground="white",yscrollcommand=scrlbr,insertwidth=5)        
        self.txtwidget.pack(expand=True,fill=tk.BOTH)
        scrlbr.config(command=self.txtwidget.yview)
        self.txtwidget.focus_force()

        self.txtwidget.insert(1.0,f"File Manager -version [{self._version}]     - CLI\nVishwa Make It Easy\n\n{os.getcwd()}")
        self._cursr_pos=self.txtwidget.index(tk.INSERT)
        self._lastpath_cursor=self.txtwidget.index(tk.INSERT)
        self.txtwidget.insert(self._lastpath_cursor,"\n")
    def Send_command(self,command):
        print(command)
        if command.startswith("fim "):
            if command.startswith("fim nested "):
                lst_folder_files=command.split()
                self.CreateNested(lst_folder_files)
        elif command=="":
            self.txtwidget.insert(tk.INSERT,os.getcwd())
            self._cursr_pos=self.txtwidget.index(tk.INSERT)
            self._firstpath_cursor,_=self.txtwidget.index(tk.INSERT).split('.')
            self._firstpath_cursor=f"{self._firstpath_cursor}.{0}"
            self._lastpath_cursor=self.txtwidget.index(tk.INSERT)
            self.txtwidget.insert(tk.INSERT,"\n")

        elif "cd " in command:
            try:
                _,path=command.split()
                os.chdir(path)
                self.txtwidget.insert(tk.INSERT,f"\n{os.getcwd()}")
                self._cursr_pos=self.txtwidget.index(tk.INSERT)
                self._firstpath_cursor,_=self.txtwidget.index(tk.INSERT).split('.')
                self._firstpath_cursor=f"{self._firstpath_cursor}.{0}"
                self._lastpath_cursor=self.txtwidget.index(tk.INSERT)
                self.txtwidget.insert(tk.INSERT,"\n")            
                      
            except Exception as error:
                self.txtwidget.insert(tk.INSERT,f"\n{os.getcwd()}")
                self._cursr_pos=self.txtwidget.index(tk.INSERT)
                self._firstpath_cursor,_=self.txtwidget.index(tk.INSERT).split('.')
                self._firstpath_cursor=f"{self._firstpath_cursor}.{0}"
                self._lastpath_cursor=self.txtwidget.index(tk.INSERT)
        else:
            try:
                result=run(command,stdout=PIPE,stderr=PIPE, universal_newlines=True)
                if result.stdout=="":
                    self.txtwidget.insert(tk.INSERT,f"\n{result.stderr}")
                elif result.stderr=="":
                    self.txtwidget.insert(tk.INSERT,f"\n{result.stdout}")     
                self.txtwidget.insert(tk.INSERT,f"\n{os.getcwd()}")
                self._cursr_pos=self.txtwidget.index(tk.INSERT)
                self._firstpath_cursor,_=self.txtwidget.index(tk.INSERT).split('.')
                self._firstpath_cursor=f"{self._firstpath_cursor}.{0}"
                self._lastpath_cursor=self.txtwidget.index(tk.INSERT)
                self.txtwidget.insert(tk.INSERT,"\n")
            except Exception as _:
                self.txtwidget.insert(tk.INSERT,f"\n{os.getcwd()}")
                self._cursr_pos=self.txtwidget.index(tk.INSERT)
                self._firstpath_cursor,_=self.txtwidget.index(tk.INSERT).split('.')
                self._firstpath_cursor=f"{self._firstpath_cursor}.{0}"
                self._lastpath_cursor=self.txtwidget.index(tk.INSERT)
                self.txtwidget.insert(tk.INSERT,"\n")
                


    def Get_command(self,events):
        self._firstcmdcrsr_pos=str(float(self.txtwidget.index(tk.INSERT))-1.0)
        command=self.txtwidget.get(self._firstcmdcrsr_pos,tk.END).strip()
        self.Send_command(command)
        
    def BackSpaceHandler(self,events):
        if float(self.txtwidget.index(tk.INSERT))<=float(self._cursr_pos):
            content=self.txtwidget.get(1.0,tk.END)
            self.txtwidget.delete(1.0,self._cursr_pos)
            self.txtwidget.insert(1.0,content)

if __name__=="__main__":
    cli=CLI()
    cli.bind("<Return>",cli.Get_command)
    cli.bind("<BackSpace>",cli.BackSpaceHandler)
    cli.mainloop()
