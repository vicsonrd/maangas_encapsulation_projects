import tkinter as tk
from car import Car

class ModernCarGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("OOP Hardware Diagnostic Monitor")
        self.root.geometry("450x450")
        self.root.configure(bg="#0a0a12")
        
        self.my_car = Car("2026", "Mustang Dark Horse")
        self.max_speed = 100
        
        self.autopilot_active = False
        self.driving_forward = True
        
        self._setup_ui()
        self.update_dashboard()

    def _setup_ui(self) -> None:
        tk.Label(self.root, text="SYS.VELOCITY_MONITOR", font=("Courier", 14, "bold"), 
                 bg="#0a0a12", fg="#5a5a75").pack(pady=15)

        self.canvas = tk.Canvas(self.root, width=300, height=250, bg="#0a0a12", highlightthickness=0)
        self.canvas.pack()

        self.speed_text = self.canvas.create_text(150, 130, text="0", font=("Helvetica", 68, "bold"), fill="#00ffcc")
        self.mph_text = self.canvas.create_text(150, 185, text="MPH", font=("Courier", 12), fill="#5a5a75")

        ctrl_frame = tk.Frame(self.root, bg="#0a0a12")
        ctrl_frame.pack(pady=20)

        self.btn_brake = tk.Button(ctrl_frame, text="[ BRAKE ]", font=("Courier", 12, "bold"), 
                                   bg="#1a1a2e", fg="#ff3333", activebackground="#ff3333", activeforeground="white",
                                   relief="flat", borderwidth=0, command=self.press_brake)
        self.btn_brake.grid(row=0, column=0, padx=5, ipadx=5, ipady=5)

        self.btn_accel = tk.Button(ctrl_frame, text="[ ACCEL ]", font=("Courier", 12, "bold"), 
                                   bg="#1a1a2e", fg="#00ffcc", activebackground="#00ffcc", activeforeground="black",
                                   relief="flat", borderwidth=0, command=self.press_accelerate)
        self.btn_accel.grid(row=0, column=1, padx=5, ipadx=5, ipady=5)

        self.btn_auto = tk.Button(ctrl_frame, text="[ AUTO ]", font=("Courier", 12, "bold"), 
                                  bg="#1a1a2e", fg="#bf00ff", activebackground="#bf00ff", activeforeground="white",
                                  relief="flat", borderwidth=0, command=self.toggle_autopilot)
        self.btn_auto.grid(row=0, column=2, padx=5, ipadx=5, ipady=5)

    def press_accelerate(self) -> None:
        self.my_car.accelerate()
        self.update_dashboard()

    def press_brake(self) -> None:
        self.my_car.brake()
        self.update_dashboard()

    def toggle_autopilot(self) -> None:
        self.autopilot_active = not self.autopilot_active
        if self.autopilot_active:
            self.btn_auto.config(fg="#ffffff", bg="#bf00ff")
            self.run_autopilot()
        else:
            self.btn_auto.config(fg="#bf00ff", bg="#1a1a2e")

    def run_autopilot(self) -> None:
        if not self.autopilot_active:
            return

        current_speed = self.my_car.get_speed()

        if self.driving_forward:
            if current_speed < self.max_speed:
                self.my_car.accelerate()
            else:
                self.driving_forward = False
        else:
            if current_speed > 0:
                self.my_car.brake()
            else:
                self.driving_forward = True

        self.update_dashboard()
        self.root.after(50, self.run_autopilot) 

    def _get_color(self, speed: int) -> str:
        if speed < 35:
            return "#00ffcc"
        elif speed < 75:
            return "#ffcc00"
        else:
            return "#ff3333"

    def update_dashboard(self) -> None:
        speed = self.my_car.get_speed()
        color = self._get_color(speed)

        self.canvas.itemconfig(self.speed_text, text=str(speed), fill=color)

        self.canvas.delete("meter_arc")
        
        self.canvas.create_arc(20, 20, 280, 280, start=225, extent=-270, 
                               style="arc", outline="#1a1a2e", width=12, tags="meter_arc")

        capped_speed = min(speed, self.max_speed)
        extent = -(capped_speed / self.max_speed) * 270
        
        if extent < 0:
            self.canvas.create_arc(20, 20, 280, 280, start=225, extent=extent, 
                                   style="arc", outline=color, width=12, tags="meter_arc")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCarGUI(root)
    root.mainloop()