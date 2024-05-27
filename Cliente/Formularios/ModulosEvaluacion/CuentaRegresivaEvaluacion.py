import tkinter as tk
import time

class CountdownApp(tk.Frame):
    def __init__(self, parent, minutes):
        tk.Frame.__init__(self, parent)
        self.minutes = minutes
        self.create_widgets()
        self.start_countdown()

    def create_widgets(self):
        self.countdown_label = tk.Label(self, font=("Arial", 24))
        self.countdown_label.pack(pady=20)

    def start_countdown(self):
        countdown_time = self.minutes * 60  # Tiempo en segundos
        self.update_countdown(countdown_time)

    def update_countdown(self, remaining_time):
        if remaining_time >= 0:
            minutes, seconds = divmod(remaining_time, 60)
            countdown_text = "{:02d}:{:02d}".format(minutes, seconds)
            self.countdown_label.config(text=countdown_text)
            self.after(1000, self.update_countdown, remaining_time - 1)  # Actualiza cada segundo
        else:
            self.countdown_label.config(text="¡Tiempo Agotado!")

if __name__ == "__main__":
    app = CountdownApp()
    app.mainloop()