from tkinter import *    # gui
from tkinter import messagebox # gui уведомление
from PIL import ImageTk,Image  # поддержка изображений
from subprocess import * # взаимодействие с ОС
import requests # запрос для проверки интернет соединения

class tkinter:
    def __init__(self,main,name_title):
        main.title(name_title) 
        main.geometry("600x591") 
        main.resizable(False, False)

    def button(self,main,button_text,path):   
        self.btn = Button(main, text = button_text,command = lambda: self.clicked(main,path))
        self.btn.pack(side=TOP)
        
    def canvas(self,main,path):
        self.canvas = Canvas(main, width = 500, height = 500)  
        self.canvas.pack()  
        self.img = ImageTk.PhotoImage(Image.open(path).resize((300,300)))
        self.canvas.create_image(250, 250, anchor = CENTER, image = self.img)

    def clicked(self,main,path):
        try:
            requests.get("https://www.google.com", timeout = 5)
            
            if self.terminal("[ -f /var/lib/pacman/db.lck ] && echo 'True' || echo 'False'") is True:
                self.terminal("rm /var/lib/pacman/db.lck")
        
            if bool(self.terminal("pacman -Qu")) is True:
                self.btn.destroy()
                self.canvas.destroy()
                self.play_mp3(path)
                self.xterm = Frame(main)
                self.xterm.pack(fill = BOTH, expand = YES) 
                self.terminal(f"xterm -into {self.xterm.winfo_id()} -geometry 99x45 -e 'sudo pacman --noconfirm -Syu && reboot;bash'",True)
            else:
                messagebox.showwarning(None, "Нет доступных обновлений!")
        
        except (requests.ConnectionError, requests.Timeout):
            messagebox.showerror(None, "Нет подключения к интернету!")
            
    def terminal(self,cmd,wid = None):
        if wid is None:
            return Popen(f"sudo {cmd}", stdout = PIPE,shell = True).stdout.read().strip().decode('ascii')
        return Popen(cmd, stdout = PIPE,shell = True)
    
    def play_mp3(self,path):
        Popen(f"mpg123 -q {path}", shell = True).wait()

main = Tk()  
app = tkinter(main,"Обновление системы")
app.button(main,"Поехали!","/home/user/Downloads/Gagarin.mp3")
app.canvas(main,"/home/user/Downloads/MIREA.png")
main.mainloop()
