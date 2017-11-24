import tkinter as tk
import time


class Timer():
    def __init__(self):
        self.run = False
        self.t_start = 0
        self.t_stop = 0

    def rst(self):
        self.__init__()

    def start(self):
        self.t_start = time.time() - (self.t_stop - self.t_start)
        self.run = True

    def stop(self):
        self.t_stop = time.time()
        self.run = False

    def get_time(self):
        if self.run:
            return time.time() - self.t_start
        else:
            return self.t_stop - self.t_start

    def start_stop(self):
        if self.run:
            self.stop()
            print(self.get_time())
        else:
            self.start()


class TimerApp():
    def __init__(self):
        self.timer = Timer()
        self.root = tk.Tk()
        default_text = '00 : 00 : 00'
        self.label = tk.Label(self.root, text=default_text)
        self.ss_btn = tk.Button(self.root, text='Start/Stop', command=self.ss_mod_label)
        self.rst_btn = tk.Button(self.root, text='Reset', command=self.rst_mod_label)
        self.label.pack()
        self.ss_btn.pack()
        self.rst_btn.pack()
        self.update_label()
        self.root.mainloop()

    def rst_mod_label(self):
        self.timer.rst()

    def ss_mod_label(self):
        self.timer.start_stop()

    def mod_label_start_stop(self):
        self.timer.start_stop()

    def update_label(self):
        text = self.text()
        self.label.configure(text=text)
        self.root.after(10, self.update_label)

    def text(self):
        t = self.timer.get_time()
        return '{0:02d} : {1:02d} : {2:02d}'.format(int(t)//60, int(t) % 60, int(100*t) % 100)


my_tmr = TimerApp()
