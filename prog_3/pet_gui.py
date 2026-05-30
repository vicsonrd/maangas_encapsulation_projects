import tkinter as tk
from pet import Pet

class ModernPetGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("OOP Biological Asset Database")
        self.root.geometry("450x550")
        self.root.configure(bg="#0a0a12")
        
        self.my_pet = Pet()
        
        self._setup_ui()

    def _setup_ui(self) -> None:
        tk.Label(self.root, text="SYS.BIO_ASSET_REGISTRY", font=("Courier", 16, "bold"), 
                 bg="#0a0a12", fg="#00ffcc").pack(pady=20)

        entry_frame = tk.Frame(self.root, bg="#0a0a12")
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="ASSET NAME:", font=("Courier", 12), bg="#0a0a12", fg="#5a5a75").grid(row=0, column=0, sticky="e", pady=10, padx=10)
        self.ent_name = tk.Entry(entry_frame, font=("Courier", 12), bg="#1a1a2e", fg="white", insertbackground="white", relief="flat")
        self.ent_name.grid(row=0, column=1, pady=10, ipady=5)

        tk.Label(entry_frame, text="SPECIES:", font=("Courier", 12), bg="#0a0a12", fg="#5a5a75").grid(row=1, column=0, sticky="e", pady=10, padx=10)
        self.ent_type = tk.Entry(entry_frame, font=("Courier", 12), bg="#1a1a2e", fg="white", insertbackground="white", relief="flat")
        self.ent_type.grid(row=1, column=1, pady=10, ipady=5)

        tk.Label(entry_frame, text="LIFESPAN (YRS):", font=("Courier", 12), bg="#0a0a12", fg="#5a5a75").grid(row=2, column=0, sticky="e", pady=10, padx=10)
        self.ent_age = tk.Entry(entry_frame, font=("Courier", 12), bg="#1a1a2e", fg="white", insertbackground="white", relief="flat")
        self.ent_age.grid(row=2, column=1, pady=10, ipady=5)

        self.btn_submit = tk.Button(self.root, text="[ ENCAPSULATE DATA ]", font=("Courier", 14, "bold"), 
                                    bg="#1a1a2e", fg="#bf00ff", activebackground="#bf00ff", activeforeground="white",
                                    relief="flat", borderwidth=0, command=self.process_data)
        self.btn_submit.pack(pady=20, ipadx=10, ipady=5)

        self.display_frame = tk.Frame(self.root, bg="#0a0a12", highlightbackground="#00ffcc", highlightthickness=1)
        self.display_frame.pack(pady=10, fill="x", padx=40)

        tk.Label(self.display_frame, text="DATABASE OUTPUT:", font=("Courier", 10), bg="#0a0a12", fg="#5a5a75").pack(pady=(10, 0))
        
        self.lbl_output = tk.Label(self.display_frame, text="AWAITING INPUT...", font=("Courier", 12), bg="#0a0a12", fg="#ff3333", justify="left")
        self.lbl_output.pack(pady=15)

    def process_data(self) -> None:
        try:
            name_val = self.ent_name.get()
            type_val = self.ent_type.get()
            age_val = int(self.ent_age.get())

            self.my_pet.set_name(name_val)
            self.my_pet.set_animal_type(type_val)
            self.my_pet.set_age(age_val)

            self.update_display()
        except ValueError:
            self.lbl_output.config(text="ERR: LIFESPAN MUST BE NUMERIC", fg="#ff3333")

    def update_display(self) -> None:
        retrieved_name = self.my_pet.get_name()
        retrieved_type = self.my_pet.get_animal_type()
        retrieved_age = self.my_pet.get_age()

        output_text = f"> ID_NAME: {retrieved_name}\n> SPECIES: {retrieved_type}\n> CURRENT_AGE: {retrieved_age}"
        self.lbl_output.config(text=output_text, fg="#00ffcc")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernPetGUI(root)
    root.mainloop()