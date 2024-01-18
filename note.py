import tkinter as tk 
from tkinter import messagebox ,filedialog

window=tk.Tk()
window.title("Write your notes")
window.geometry('500x500')
window.configure(bg='#a2d2ff')

def login():
    username="salmaakhssasi"
    password="12345"
    if username_entry.get()=="salmaakhssasi" and password_entry.get()=="12345":
        open_new_window()
    else:
        messagebox.showerror(title="error",message="Invalid login")
  

username_label=tk.Label(window,text="Username",fg="#FFFFFF",bg="#a2d2ff",font=('Arial',16))
username_entry=tk.Entry(window,font=('Arial',16))
password_label=tk.Label(window,text="Password",fg="#FFFFFF",bg="#a2d2ff",font=('Arial',16))
password_entry=tk.Entry(window,show="*",font=('Arial',16))


username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=30)

loginn=tk.Button(window,text="login",command =login ,width="20",height='2')
loginn.grid(row =3, column=1,pady=20) 



def open_new_window(): 
    class NotesApp:
        def __init__(self, root):
          self.root = root
          self.root.title("Notes App")

          self.notes = []

        # Create text input areas
          self.create_text_inputs()
        
        def create_text_inputs(self):
          self.text_inputs = []

          for i in range(2):
            text_input = tk.Text(self.root, height=5, width=30)
            text_input.grid(row=i, column=0, padx=10, pady=10)
            self.text_inputs.append(text_input)

        # Create Save button
          self.create_save_button()
          
          
        def create_save_button(self):
          save_button = tk.Button(self.root, text="Save Notes", command=self.save_notes)
          save_button.grid(row=4, column=0, pady=10)

        def save_notes(self):
          for i, text_input in enumerate(self.text_inputs):
            note = text_input.get("1.0", tk.END).strip()
            self.notes.append(f"Note {i + 1}: {note}")

        # Open a file dialog to choose the save location
          file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

          if file_path:
            with open(file_path, "w") as file:
                file.write("\n".join(self.notes))
            print("Notes saved successfully!")
    if __name__ == "__main__":
       root = tk.Tk()
       app = NotesApp(root)
       root.mainloop()






window.mainloop()