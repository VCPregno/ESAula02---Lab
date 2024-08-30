import tkinter as tk
from tkinter import messagebox

class Tela1:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela 1 - Inserir Números")

        self.numbers = []
        self.original_numbers = []

        self.labels = []
        self.entries = []
        for i in range(8):
            label = tk.Label(root, text=f"Número {i+1}:")
            label.grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.labels.append(label)
            self.entries.append(entry)

        self.submit_btn = tk.Button(root, text="Entra", command=self.process_numbers)
        self.submit_btn.grid(row=8, column=0, columnspan=2, pady=10)

    def process_numbers(self):
        self.original_numbers.clear()
        self.numbers.clear()
        try:
            self.original_numbers = [int(entry.get()) for entry in self.entries]
            if len(self.original_numbers) != 8:
                raise ValueError("Você deve inserir exatamente 8 números.")
            self.numbers = sorted(self.original_numbers)
            self.show_tela2()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def show_tela2(self):
        self.root.withdraw()
        tela2 = tk.Toplevel(self.root)
        Tela2(tela2, self.original_numbers, self.numbers, self)

class Tela2:
    def __init__(self, root, original_numbers, sorted_numbers, tela1):
        self.root = root
        self.root.title("Tela 2 - Buscar Número")

        self.original_numbers = original_numbers
        self.sorted_numbers = sorted_numbers
        self.tela1 = tela1

        self.label = tk.Label(root, text="Número para buscar:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.submit_btn = tk.Button(root, text="Entra", command=self.process_search)
        self.submit_btn.grid(row=1, column=0, columnspan=2, pady=10)

        self.back_btn = tk.Button(root, text="Voltar", command=self.go_back)
        self.back_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def process_search(self):
        try:
            search_value = int(self.entry.get())
            if search_value in self.sorted_numbers:
                sorted_position = self.sorted_numbers.index(search_value) + 1
                original_position = self.original_numbers.index(search_value) + 1
                self.show_tela3(f"O número {search_value} foi encontrado na posição {sorted_position} na lista ordenada e na posição {original_position} na lista original.")
            else:
                self.show_tela3(f"O número {search_value} não foi encontrado.")
        except ValueError:
            messagebox.showerror("Erro", "Você deve inserir um número inteiro.")

    def show_tela3(self, message):
        self.root.withdraw()
        tela3 = tk.Toplevel(self.root)
        Tela3(tela3, message, self)

    def go_back(self):
        self.root.destroy()
        self.tela1.root.deiconify()

class Tela3:
    def __init__(self, root, message, tela2):
        self.root = root
        self.root.title("Tela 3 - Resultado da Busca")

        self.label = tk.Label(root, text=message)
        self.label.pack(padx=10, pady=10)

        self.quit_btn = tk.Button(root, text="Fechar", command=self.quit)
        self.quit_btn.pack(pady=10)

        self.back_btn = tk.Button(root, text="Voltar", command=self.go_back)
        self.back_btn.pack(pady=10)

        self.tela2 = tela2

    def quit(self):
        self.root.destroy()
        self.tela2.root.deiconify()

    def go_back(self):
        self.root.destroy()
        self.tela2.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = Tela1(root)
    root.mainloop()
