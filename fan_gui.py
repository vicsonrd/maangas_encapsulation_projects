import tkinter as tk
from fan import Fan

class FanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OOP Fan Visualizer")
        
        
        self.my_fan = Fan()
        self.angle = 0
        self.is_animating = False

        
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack(pady=20)

       
        ctrl_frame = tk.Frame(root)
        ctrl_frame.pack(pady=10)


        self.btn_power = tk.Button(ctrl_frame, text="Turn ON", width=10, command=self.toggle_power)
        self.btn_power.grid(row=0, column=0, padx=5)

        
        self.btn_slow = tk.Button(ctrl_frame, text="Slow", command=lambda: self.change_speed(Fan.SLOW))
        self.btn_slow.grid(row=0, column=1, padx=5)
        
        self.btn_med = tk.Button(ctrl_frame, text="Medium", command=lambda: self.change_speed(Fan.MEDIUM))
        self.btn_med.grid(row=0, column=2, padx=5)
        
        self.btn_fast = tk.Button(ctrl_frame, text="Fast", command=lambda: self.change_speed(Fan.FAST))
        self.btn_fast.grid(row=0, column=3, padx=5)

    
        self.btn_blue = tk.Button(ctrl_frame, text="Blue", bg="lightblue", command=lambda: self.change_color("blue"))
        self.btn_blue.grid(row=1, column=1, pady=10)
        
        self.btn_yellow = tk.Button(ctrl_frame, text="Yellow", bg="lightyellow", command=lambda: self.change_color("yellow"))
        self.btn_yellow.grid(row=1, column=2, pady=10)

        self.draw_fan()

    def toggle_power(self):
        
        current_state = self.my_fan.get_on()
        self.my_fan.set_on(not current_state)
        
        if self.my_fan.get_on():
            self.btn_power.config(text="Turn OFF", fg="red")
            self.animate_fan()
        else:
            self.btn_power.config(text="Turn ON", fg="black")

    def change_speed(self, speed):
        self.my_fan.set_speed(speed)

    def change_color(self, color):
        self.my_fan.set_color(color)
        self.draw_fan()

    def draw_fan(self):
        self.canvas.delete("all")
        x, y, r = 150, 150, self.my_fan.get_radius() * 10 # Scale radius for visibility
        color = self.my_fan.get_color()

        
        self.canvas.create_oval(x - r - 10, y - r - 10, x + r + 10, y + r + 10, outline="gray", width=4)

    
        for i in range(4):
            start_angle = self.angle + (i * 90)
            self.canvas.create_arc(x - r, y - r, x + r, y + r, 
                                   start=start_angle, extent=30, fill=color, outline="black")

    def animate_fan(self):
        if self.my_fan.get_on():
            # Adjust angle step based on getter speed
            speed_multiplier = self.my_fan.get_speed() * 5
            self.angle = (self.angle + speed_multiplier) % 360
            self.draw_fan()
            self.root.after(20, self.animate_fan)

if __name__ == "__main__":
    root = tk.Tk()
    app = FanGUI(root)
    root.mainloop()