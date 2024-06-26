import tkinter as tk
from tktimepicker import SpinTimePickerModern, SpinTimePickerOld
from tktimepicker import constants


def updateTime(time,time_lbl):
    time_lbl.configure(text="{}:{}".format(*time)) # if you are using 24 hours, remove the 3rd flower bracket its for period


def get_time(root,time_lbl):

    top = tk.Toplevel(root)

    time_picker = SpinTimePickerModern(top)
    # time_picker = SpinTimePickerOld(top)
    time_picker.addAll(constants.HOURS24)  # adds hours clock, minutes and period
    time_picker.configureAll(bg="#404040", height=1, fg="#ffffff", font=("Times", 16), hoverbg="#404040",
                            hovercolor="#d73333", clickedbg="#2e2d2d", clickedcolor="#d73333")
    time_picker.configure_separator(bg="#404040", fg="#ffffff")
    # time_picker.addHours12()
    #time_picker.addHours24()
    # time_picker.addMinutes()

    time_picker.pack(expand=True, fill="both")

    ok_btn = tk.Button(top, text="ok", command=lambda: updateTime(time_picker.time(),time_lbl))
    ok_btn.pack()