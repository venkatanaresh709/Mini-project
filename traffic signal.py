import tkinter as tk
import time
from threading import Thread

class TrafficSignalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Signal Management with Car")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="gray")
        self.canvas.pack()

        # Draw the road
        self.canvas.create_rectangle(200, 0, 300, 400, fill="black")  # Vertical road

        # Traffic light box
        self.canvas.create_rectangle(50, 50, 100, 200, fill="white", outline="black")

        # Traffic lights (circles)
        self.red_light = self.canvas.create_oval(60, 60, 90, 90, fill="gray")
        self.yellow_light = self.canvas.create_oval(60, 100, 90, 130, fill="gray")
        self.green_light = self.canvas.create_oval(60, 140, 90, 170, fill="gray")

        # Car (initially at top of road)
        self.car = self.canvas.create_rectangle(210, 10, 290, 50, fill="blue")

        # Start signal management in separate thread
        self.running = True
        Thread(target=self.manage_traffic).start()

    def set_signal(self, red, yellow, green):
        self.canvas.itemconfig(self.red_light, fill="red" if red else "gray")
        self.canvas.itemconfig(self.yellow_light, fill="yellow" if yellow else "gray")
        self.canvas.itemconfig(self.green_light, fill="green" if green else "gray")

    def move_car(self):
        # Move car down while signal is green
        for _ in range(80):  # Move 50 steps
            self.canvas.move(self.car, 0, 5)
            time.sleep(0.05)
            self.root.update()

    def manage_traffic(self):
        while self.running:
            # Red light
            self.set_signal(red=1, yellow=0, green=0)
            time.sleep(3)

            # Yellow light
            self.set_signal(red=0, yellow=1, green=0)
            time.sleep(2)

            # Green light
            self.set_signal(red=0, yellow=0, green=1)
            self.move_car()  # Car moves only during green
            time.sleep(3)

            # Reset car position after green
            self.canvas.coords(self.car, 210, 10, 290, 50)

    def stop(self):
        self.running = False

# Create main window
root = tk.Tk()
app = TrafficSignalApp(root)

# Handle close
def on_closing():
    app.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
