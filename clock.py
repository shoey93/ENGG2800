from Tkinter import *
import tkMessageBox
import time

class ClockApp():
    
    def __init__(self, master=None):
        master.title("Set The Time")
        master.minsize(500,300)

        self._master = master
        
        self.buttonFrame = ButtonFrame(master, self)
        self.buttonFrame.pack(anchor=E, pady=15, padx=15, fill=BOTH, expand=1)

        self.canvas = Canvas(master, height=200, width=450, bg='white')
        self.canvas.pack(padx=5, pady=1, fill=BOTH, expand=1)
        self.canvas["relief"] = SUNKEN
        self.canvas["bd"] = 1
        self.canvas["bg"] = "black"

    def setTime(self):
        tkMessageBox.showinfo(title="Set The Time",
                                  message="Please Hold Clock To Screen")
        hour = self.buttonFrame.getHour()
        ten = self.buttonFrame.getTen()
        one = self.buttonFrame.getOne()
        ampm = self.buttonFrame.getampm()
        if ampm == "pm":
            tempHour = int(hour)
            tempHour += 12
            hour = str(tempHour)
        timestring = hour + ten + one
        inttime = int(timestring)
        bintime = bin(inttime)
        timelist = list(bintime)
        timelist.remove("0")
        timelist.remove("b")
        size = len(timelist)
        if size < 12:
            for i in range(0, (12-size)):
                timelist.insert(i, 0)
        print timelist
        r = self.canvas.create_rectangle(0, 0, 1000, 1000, fill="black")
        self.canvas.update
        self.canvas.itemconfig(r, fill="white")
        self.canvas.update()
        time.sleep(1)
        for i in timelist:
            if (i == "1"):
                self.canvas.itemconfig(r, fill="white")
            else:
                self.canvas.itemconfig(r, fill="black")
            time.sleep(0.1)
            self.canvas.update()
        self.canvas.itemconfig(r, fill="white")
        self.canvas.update()
        time.sleep(1)
        self.canvas.itemconfig(r, fill="black")
        self.canvas.update()
        

    def setAlarm(self):
        tkMessageBox.showinfo(title="Set The Alarm",
                                  message="Please Hold Clock To Screen")
        hour = self.buttonFrame.getHour()
        ten = self.buttonFrame.getTen()
        one = self.buttonFrame.getOne()
        ampm = self.buttonFrame.getampm()
        if ampm == "pm":
            tempHour = int(hour)
            tempHour += 12
            hour = str(tempHour)
        time = hour + ten + one

    def quit1(self):
        """Exits the application"""
        self._master.destroy()
                
class ButtonFrame(Frame):
    """The Frame containing the command buttons"""
    def __init__(self, master, parent):
        """Creates the Button Frame
        master - Toplevel Window
        parent - Application Object
        """
        self.parent = parent
        Frame.__init__(self, master)
        self.var1 = StringVar(self)
        self.var1.set("12")
        self.setHour = OptionMenu(self, self.var1, "12", "1", "2","3","4","5","6","7",
                   "8","9","10","11")
        self.setHour.pack(side=LEFT)
        self.colon = Label(self, text=":")
        self.colon.pack(side=LEFT)
        self.var2 = StringVar(self)
        self.var2.set("0")
        self.setTen = OptionMenu(self, self.var2, "0", "1", "2","3","4","5")
        self.setTen.pack(side=LEFT)
        self.var3 = StringVar(self)
        self.var3.set("0")
        self.setOne = OptionMenu(self, self.var3, "0","1", "2","3","4",
                                 "5","6","7","8","9")
        self.setOne.pack(side=LEFT)
        self.var4 = StringVar(self)
        self.var4.set("am")
        self.setampm = OptionMenu(self, self.var4, "am","pm")
        self.setampm.pack(side=LEFT)
        self.exit = Button(self, text="Exit", command = self.quit1)
        self.exit.pack(side=RIGHT, ipadx=10)
        self.setAlarm = Button(self, text="Set Alarm", command = self.setAlarm)
        self.setAlarm.pack(side=RIGHT, ipadx=10)
        self.setTime = Button(self, text="Set Time", command = self.setTime)
        self.setTime.pack(side=RIGHT, ipadx=10)

    def setTime(self):
        self.parent.setTime()

    def setAlarm(self):
        self.parent.setAlarm()

    def getHour(self):
        return self.var1.get()
    
    def getTen(self):
        return self.var2.get()

    def getOne(self):
        return self.var3.get()

    def getampm(self):
        return self.var4.get()

    def quit1(self):
        """Accesses the quit1 Function from parent"""
        self.parent.quit1()

    
        

        







def main():
    root = Tk()
    app = ClockApp(root)
    root.mainloop()

if  __name__ == '__main__':
    main()
