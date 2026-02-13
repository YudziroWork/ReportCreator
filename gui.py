import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import os
from processor import process


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Сравнение номеров")
        self.root.geometry("500x350")

        self.etalon_path = ""
        self.recognized_path = ""
        self.output_dir = ""

        tk.Button(root, text="Выбрать эталон", command=self.select_etalon).pack(pady=5)
        tk.Button(root, text="Выбрать распознавание", command=self.select_recognized).pack(pady=5)
        tk.Button(root, text="Выбрать папку отчёта", command=self.select_output).pack(pady=5)

        tk.Button(root, text="Сформировать отчёт", command=self.run, bg="green", fg="white").pack(pady=15)

        self.status = tk.Label(root, text="Статус: Ожидание")
        self.status.pack(pady=5)

        self.stats_label = tk.Label(root, text="")
        self.stats_label.pack(pady=5)

    def select_etalon(self):
        self.etalon_path = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])

    def select_recognized(self):
        self.recognized_path = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])

    def select_output(self):
        self.output_dir = filedialog.askdirectory()

    def run(self):
        if not self.etalon_path or not self.recognized_path or not self.output_dir:
            messagebox.showerror("Ошибка", "Выберите все файлы!")
            return

        try:
            self.status.config(text="Обработка...")
            self.root.update()

            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            output_path = os.path.join(self.output_dir, filename)

            stats = process(self.etalon_path, self.recognized_path, output_path)

            self.status.config(text="Готово")

            self.stats_label.config(
                text=f"Всего: {stats['total']} | "
                     f"Точно: {stats['fully_matched']} | "
                     f"Частично: {stats['partially_matched']} | "
                     f"Точность: {stats['accuracy_percent']:.2f}%"
            )

            messagebox.showinfo("Успех", f"Отчёт создан:\n{output_path}")

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            self.status.config(text="Ошибка")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()