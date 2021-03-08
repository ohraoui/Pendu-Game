from tkinter import *
import  tkinter.messagebox as Mb


class pendu_fenetre():
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.config(bg="white")
        self.master.title("Pendu Game")
        # self.master.iconbitmap("images\")
        #---------------------------Frame & Images-----------------------------
        self.master.iconbitmap("images/pendu.ico")
        self.imageLabel = Label(self.master)
        self.desc_frame = LabelFrame(self.master, text="Welcome to Pendu GAME", bd=5, relief='ridge', bg='lightgray', width=300, height=200)
        self.desc_frame.place(x=50, y=50)
        #-----------------------------Button&Label----------------------------
        # self.question = Lbel(self.desc_frame, text="How much letter will you use :", bg="lightgray", font=('arial',8,'bold')).place(x=30, y=70)
        # self.answer = Label(self.desc_frame, text="How much letter will you use :", bg="lightgray", font=('arial',8,'bold')).place(x=30, y=70)
        # self.number = Entry(self.desc_frame)
        # self.number.config(width="4")
        # self.number.place(x=210, y=70)
        self.wLabel = Label(self.desc_frame, text="word :", bg="lightgray", font=('arial',8,'bold')).place(x=45, y=10)
        self.wEntry = Entry(self.desc_frame, show="*")
        self.wEntry.place(x=115, y=10)
        self.startBtn = Button(self.desc_frame, text="START", font=('arial',8,'bold'), bg="lightgreen", command=self.start)
        self.startBtn.place(x=130, y=50)
        self.response = Label(self.desc_frame, text="Response :", bg="lightgray", font=('arial',8,'bold')).place(x=45, y=100)
        self.letter = Entry(self.desc_frame, state=DISABLED)
        self.letter.place(x=115, y=100)
        self.check = Button(self.desc_frame, text="CHECK", font=('arial',8,'bold'), bg="lightgreen", state=DISABLED, command=self.check)
        self.check.place(x=130, y=150)
        self.check_response = Label(self.master, text="ANSWER", bg="white", font=('arial',14,'bold'))
        self.check_response.place(x=165, y=290)
    def start(self):
        # self.number.config(state=DISABLED)
        self.word = self.wEntry.get()
        if len(self.word) < 2:
            self.wEntry.delete(0,END)
            Mb.showerror('Pendu Game','You should insert a word !')
        else:
            self.letter.config(state=NORMAL)
            self.check.config(state=NORMAL)
            self.wEntry.config(state=DISABLED)
            self.answer = ['*' for i in range(len(self.word))]
            self.counter = 4
            self.startBtn.config(text="RESTART", command=self.restart)
            self.startBtn.place(x=125, y=50)
    def restart(self):
        self.wEntry.config(state=NORMAL)
        self.wEntry.delete(0,END)
        self.letter.config(state=NORMAL)
        self.letter.delete(0,END)
        self.letter.config(state=DISABLED)
        self.clear()
        self.check_response.config(text="ANSWER")
        self.check_response.place(x=165, y=290)
        self.startBtn.config(text="START", command=self.start)
        self.startBtn.place(x=130, y=50)
    def find_response(self,c):
        word = [l_word for l_word in self.word]
        i=0
        while i < len(self.answer):
            if c == word[i]:
                self.answer[i] = c
            i+=1
        return self.answer
    def check(self):
        letter = self.letter.get()
        temp = self.answer.count('*')
        if len(letter) == 1:
            if self.counter >= 0:
                found = len(self.answer) - self.answer.count('*')
                check_result = self.find_response(letter)
                result = check_result.count('*')
                if check_result.count('*') == 0:
                    self.clear()
                    self.letter.config(state=DISABLED)
                    message = 'Congratulations. You found it.\n\n' 
                    xCoord = 65
                else:
                    if temp <= result: 
                        self.counter -= 1
                    s = 's'
                    if self.counter == 1:
                        s = ''
                    message = 'You still have '+str(self.counter+1)+' attempt'+s+'.\n\n'
                    if result == len(check_result) - found:
                        self.master.geometry("400x550")
                        img = PhotoImage(file="images/attempt"+str(self.counter)+".png")
                        self.imageLabel.config(bg="white", image=img)
                        self.imageLabel.image = img
                        self.imageLabel.place(x=110, y=380)
                        message += 'You haven\'t found anything.\n\n'
                        xCoord = 70
                    else:
                        self.clear()
                        num = len(check_result) - result - found
                        s = ''
                        if num != 1:
                            s = 's'
                        message += 'You found '+str(num)+' letter'+s+'.\n\n'
                        xCoord = 90
                message += "  ".join(check_result)
                self.check_response.config(text=message)
                self.check_response.place(x=xCoord, y=270)
                self.letter.delete(0,END)
            else:
                self.restart()
                Mb.showerror('Pendu Game','You failed. The word was " '+self.word+' ".')
        else:
            self.letter.delete(0,END)
            Mb.showwarning("Pendu Game","You must insert one single letter !")     
    def clear(self):
        self.imageLabel.config(image="")
        self.master.geometry("400x400")   


if __name__ == '__main__':
    pf = Tk()
    app = pendu_fenetre(pf)
    pf.mainloop()