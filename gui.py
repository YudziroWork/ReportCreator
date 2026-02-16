import tkinter as tk
from tkinter import filedialog, messagebox
from processor import process


def browse_file(entry_widget, save=False):
    if save:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
        )
    else:
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )

    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)


def run_process():
    etalon_path = etalon_entry.get()
    recognized_path = recognized_entry.get()
    output_path = output_entry.get()

    if not etalon_path or not recognized_path or not output_path:
        messagebox.showerror("Ошибка", "Заполните все пути к файлам.")
        return

    try:
        process(
            etalon_path=etalon_path,
            recognized_path=recognized_path,
            output_path=output_path,
            show_threshold_matches=show_threshold_var.get(),
            make_stat1=stat1_var.get(),
            make_stat2=stat2_var.get(),
            make_not_used=not_used_var.get(),
        )

        messagebox.showinfo("Готово", "Отчёт успешно сформирован!")

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


# =========================
# Создание окна
# =========================
root = tk.Tk()
root.title("Сравнение номеров")
root.geometry("900x250")
root.resizable(False, False)

# =========================
# Левая часть (пути)
# =========================

tk.Label(root, text="Файл эталона:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
etalon_entry = tk.Entry(root, width=50)
etalon_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Обзор", command=lambda: browse_file(etalon_entry)).grid(
    row=0, column=2
)

tk.Label(root, text="Файл распознавания:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
recognized_entry = tk.Entry(root, width=50)
recognized_entry.grid(row=1, column=1, padx=5)
tk.Button(root, text="Обзор", command=lambda: browse_file(recognized_entry)).grid(
    row=1, column=2
)

tk.Label(root, text="Файл отчёта:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=2, column=1, padx=5)
tk.Button(root, text="Обзор", command=lambda: browse_file(output_entry, save=True)).grid(
    row=2, column=2
)

# =========================
# Правая часть (настройки)
# =========================

settings_frame = tk.LabelFrame(root, text="Настройки", padx=10, pady=10)
settings_frame.grid(row=0, column=3, rowspan=4, padx=20, pady=10, sticky="n")

show_threshold_var = tk.BooleanVar(value=False)
stat1_var = tk.BooleanVar(value=True)
stat2_var = tk.BooleanVar(value=True)
not_used_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    settings_frame,
    text="Показывать частичные (0.55 от длины)",
    variable=show_threshold_var,
).pack(anchor="w")

tk.Checkbutton(
    settings_frame,
    text="Формировать статистику 1",
    variable=stat1_var,
).pack(anchor="w")

tk.Checkbutton(
    settings_frame,
    text="Формировать статистику 2",
    variable=stat2_var,
).pack(anchor="w")

tk.Checkbutton(
    settings_frame,
    text="Формировать список пропущенных",
    variable=not_used_var,
).pack(anchor="w")

# =========================
# Кнопка запуска
# =========================

tk.Button(
    root,
    text="Сформировать отчёт",
    width=25,
    height=2,
    command=run_process,
).grid(row=3, column=1, pady=20)

root.mainloop()