import time
from pynput import keyboard, mouse
import tkinter as tk

class APMCounter:
    def __init__(self):
        self.start_time = time.time()
        self.total_actions = 0

    def on_keyboard_press(self, key):
        self.total_actions += 1

    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            self.total_actions += 1

    def calculate_apm(self):
        elapsed_time = time.time() - self.start_time
        apm = int(self.total_actions / elapsed_time * 60)
        return apm

    def update_gui(self):
        apm = self.calculate_apm()
        self.apm_label.config(text=f"APM: {apm}")

        self.apm_label.after(1000, self.update_gui)

    def set_window_always_on_top(self, window):
        if window.winfo_viewable():
            window.attributes("-topmost", True)
            window.attributes("-topmost", False)
        window.after(1000, lambda: self.set_window_always_on_top(window))

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_press)
        keyboard_listener.start()

        mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        mouse_listener.start()

        root = tk.Tk()
        root.overrideredirect(True) 
        root.attributes("-topmost", True)

        self.apm_label = tk.Label(root, text="APM: 0", font=("Arial", 12), bg="white")
        self.apm_label.pack(anchor="se")
        
        self.update_gui()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        root_width = self.apm_label.winfo_reqwidth()
        root_height = self.apm_label.winfo_reqheight()
        x_pos = screen_width - root_width - 15
        y_pos = (screen_height - root_height) // 2

        root.geometry(f"+{x_pos}+{y_pos}")

        self.set_window_always_on_top(root)

        root.mainloop()

apm_counter = APMCounter()
apm_counter.start()
