import datetime
import tkinter as tk
from tkinter import ttk, messagebox

def set_alarm():
    try:
        alarm_hour = int(hour_entry.get())
        alarm_minute = int(minute_entry.get())
        alarm_second = int(second_entry.get())
        
        if 0 <= alarm_hour < 24 and 0 <= alarm_minute < 60 and 0 <= alarm_second < 60:
            alarm_time = datetime.time(alarm_hour, alarm_minute, alarm_second)
            current_time = datetime.datetime.now().time()
            if alarm_time > current_time:
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time.strftime('%H:%M:%S')}")
                root.after((alarm_time.hour - current_time.hour) * 3600000 + (alarm_time.minute - current_time.minute) * 60000 + (alarm_time.second - current_time.second) * 1000, ring_alarm)
            else:
                messagebox.showwarning("Invalid Time", "Please enter a future time.")
        else:
            messagebox.showwarning("Invalid Time", "Please enter a valid time (0-23 hours, 0-59 minutes, 0-59 seconds).")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for hours, minutes, and seconds.")

def ring_alarm():
        root.after(3000, lambda: messagebox.showinfo("Alarm", "Wake up!"))

# GUI setup
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("300x200")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

hour_label = ttk.Label(mainframe, text="Hour:")
hour_label.grid(row=0, column=0, padx=5, pady=5)
hour_entry = ttk.Entry(mainframe)
hour_entry.grid(row=0, column=1, padx=5, pady=5)

minute_label = ttk.Label(mainframe, text="Minute:")
minute_label.grid(row=1, column=0, padx=5, pady=5)
minute_entry = ttk.Entry(mainframe)
minute_entry.grid(row=1, column=1, padx=5, pady=5)

second_label = ttk.Label(mainframe, text="Second:")
second_label.grid(row=2, column=0, padx=5, pady=5)
second_entry = ttk.Entry(mainframe)
second_entry.grid(row=2, column=1, padx=5, pady=5)

set_button = ttk.Button(mainframe, text="Set Alarm", command=set_alarm)
set_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
