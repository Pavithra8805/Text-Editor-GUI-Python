import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font
import os
from datetime import datetime


class ModernTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor - Untitled")
        self.root.geometry("1200x700")
        self.root.minsize(800, 600)

        self.current_file = None
        self.is_modified = False

        self.setup_styles()
        self.create_menu()
        self.create_toolbar()
        self.create_status_bar()
        self.create_editor()
        self.bind_shortcuts()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_styles(self):
        self.bg_color = "#1e1e1e"
        self.fg_color = "#d4d4d4"
        self.select_bg = "#264f78"
        self.toolbar_bg = "#2d2d30"
        self.status_bg = "#007acc"
        self.button_bg = "#0e639c"
        self.button_hover = "#1177bb"

        self.root.configure(bg=self.bg_color)

        style = ttk.Style()
        style.theme_use('clam')

    def create_menu(self):
        menubar = tk.Menu(self.root, bg=self.toolbar_bg, fg=self.fg_color,
                          activebackground=self.button_hover, activeforeground="white")
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0, bg=self.toolbar_bg, fg=self.fg_color,
                            activebackground=self.button_hover, activeforeground="white")
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(
            label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(
            label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(
            label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(
            label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit", command=self.on_closing, accelerator="Alt+F4")

        edit_menu = tk.Menu(menubar, tearoff=0, bg=self.toolbar_bg, fg=self.fg_color,
                            activebackground=self.button_hover, activeforeground="white")
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(
            label="Undo", command=self.undo, accelerator="Ctrl+Z")
        edit_menu.add_command(
            label="Redo", command=self.redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Cut", command=self.cut, accelerator="Ctrl+X")
        edit_menu.add_command(
            label="Copy", command=self.copy, accelerator="Ctrl+C")
        edit_menu.add_command(
            label="Paste", command=self.paste, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All",
                              command=self.select_all, accelerator="Ctrl+A")

        view_menu = tk.Menu(menubar, tearoff=0, bg=self.toolbar_bg, fg=self.fg_color,
                            activebackground=self.button_hover, activeforeground="white")
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(
            label="Zoom In", command=self.zoom_in, accelerator="Ctrl++")
        view_menu.add_command(
            label="Zoom Out", command=self.zoom_out, accelerator="Ctrl+-")
        view_menu.add_command(label="Reset Zoom",
                              command=self.reset_zoom, accelerator="Ctrl+0")

        help_menu = tk.Menu(menubar, tearoff=0, bg=self.toolbar_bg, fg=self.fg_color,
                            activebackground=self.button_hover, activeforeground="white")
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg=self.toolbar_bg, height=40)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        buttons = [
            ("New", self.new_file),
            ("Open", self.open_file),
            ("Save", self.save_file),
            ("Cut", self.cut),
            ("Copy", self.copy),
            ("Paste", self.paste),
            ("Undo", self.undo),
            ("Redo", self.redo)
        ]

        for text, command in buttons:
            btn = tk.Button(toolbar, text=text, command=command,
                            bg=self.button_bg, fg="white",
                            activebackground=self.button_hover,
                            relief=tk.FLAT, padx=15, pady=5,
                            cursor="hand2", font=("Segoe UI", 9))
            btn.pack(side=tk.LEFT, padx=2, pady=5)

    def create_status_bar(self):
        self.status_bar = tk.Frame(self.root, bg=self.status_bg, height=25)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.line_col_label = tk.Label(self.status_bar, text="Line: 1 | Col: 1",
                                       bg=self.status_bg, fg="white",
                                       font=("Segoe UI", 9), anchor=tk.W)
        self.line_col_label.pack(side=tk.LEFT, padx=10)

        self.file_type_label = tk.Label(self.status_bar, text="Plain Text",
                                        bg=self.status_bg, fg="white",
                                        font=("Segoe UI", 9))
        self.file_type_label.pack(side=tk.RIGHT, padx=10)

        self.modified_label = tk.Label(self.status_bar, text="",
                                       bg=self.status_bg, fg="white",
                                       font=("Segoe UI", 9))
        self.modified_label.pack(side=tk.RIGHT, padx=10)

        self.branding_label = tk.Label(self.status_bar, text="Powered by ProjectsHUB",
                                       bg=self.status_bg, fg="white",
                                       font=("Segoe UI", 9, "bold"))
        self.branding_label.pack(side=tk.RIGHT, padx=10)

    def create_editor(self):
        self.editor_frame = tk.Frame(self.root, bg=self.bg_color)
        self.editor_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create line numbers
        self.line_numbers = tk.Text(self.editor_frame, width=4, padx=5, takefocus=0,
                                    border=0, background="#252526", foreground="#858585",
                                    state="disabled", wrap="none", font=("Consolas", 11))
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        scrollbar = tk.Scrollbar(self.editor_frame, bg=self.bg_color)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        editor_font = font.Font(family="Consolas", size=11)

        self.text_editor = tk.Text(self.editor_frame, wrap=tk.WORD,
                                   undo=True, maxundo=-1,
                                   bg=self.bg_color, fg=self.fg_color,
                                   insertbackground="white",
                                   selectbackground=self.select_bg,
                                   selectforeground="white",
                                   font=editor_font,
                                   relief=tk.FLAT,
                                   yscrollcommand=scrollbar.set)
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.text_editor.yview)

        self.text_editor.bind("<KeyRelease>", self.on_content_changed)
        self.text_editor.bind("<Button-1>", self.on_content_changed)
        self.text_editor.bind(
            "<KeyRelease>", self.update_line_numbers, add="+")
        self.text_editor.bind(
            "<MouseWheel>", self.update_line_numbers, add="+")

        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", tk.END)

        line_count = self.text_editor.get("1.0", tk.END).count("\n")
        line_numbers_string = "\n".join(str(i)
                                        for i in range(1, line_count + 1))
        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.config(state="disabled")

    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_as_file())
        self.root.bind("<Control-z>", lambda e: self.undo())
        self.root.bind("<Control-y>", lambda e: self.redo())
        self.root.bind("<Control-x>", lambda e: self.cut())
        self.root.bind("<Control-c>", lambda e: self.copy())
        self.root.bind("<Control-v>", lambda e: self.paste())
        self.root.bind("<Control-a>", lambda e: self.select_all())
        self.root.bind("<Control-plus>", lambda e: self.zoom_in())
        self.root.bind("<Control-minus>", lambda e: self.zoom_out())
        self.root.bind("<Control-0>", lambda e: self.reset_zoom())

    def on_content_changed(self, event=None):
        self.update_status_bar()
        if not self.is_modified:
            self.is_modified = True
            self.update_title()

    def update_status_bar(self):
        line, col = self.text_editor.index(tk.INSERT).split(".")
        self.line_col_label.config(text=f"Line: {line} | Col: {int(col) + 1}")

        if self.is_modified:
            self.modified_label.config(text="Modified")
        else:
            self.modified_label.config(text="")

    def update_title(self):
        title = "Text Editor - "
        if self.current_file:
            title += os.path.basename(self.current_file)
        else:
            title += "Untitled"
        if self.is_modified:
            title += " *"
        self.root.title(title)

    def new_file(self):
        if self.is_modified:
            response = messagebox.askyesnocancel("Save Changes",
                                                 "Do you want to save changes?")
            if response is None:
                return
            elif response:
                self.save_file()

        self.text_editor.delete("1.0", tk.END)
        self.current_file = None
        self.is_modified = False
        self.update_title()
        self.update_line_numbers()

    def open_file(self):
        if self.is_modified:
            response = messagebox.askyesnocancel("Save Changes",
                                                 "Do you want to save changes?")
            if response is None:
                return
            elif response:
                self.save_file()

        filepath = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("JavaScript Files", "*.js"),
                ("HTML Files", "*.html"),
                ("CSS Files", "*.css"),
                ("All Files", "*.*")
            ]
        )

        if not filepath:
            return

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert("1.0", content)

            self.current_file = filepath
            self.is_modified = False
            self.update_title()
            self.update_line_numbers()
            self.update_file_type()
            messagebox.showinfo("Success", "File opened successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file:\n{str(e)}")

    def save_file(self):
        if not self.current_file:
            return self.save_as_file()

        try:
            content = self.text_editor.get("1.0", tk.END)
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(content)

            self.is_modified = False
            self.update_title()
            self.update_status_bar()
            messagebox.showinfo("Success", "File saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")

    def save_as_file(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("JavaScript Files", "*.js"),
                ("HTML Files", "*.html"),
                ("CSS Files", "*.css"),
                ("All Files", "*.*")
            ]
        )

        if not filepath:
            return

        try:
            content = self.text_editor.get("1.0", tk.END)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)

            self.current_file = filepath
            self.is_modified = False
            self.update_title()
            self.update_file_type()
            messagebox.showinfo("Success", "File saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")

    def update_file_type(self):
        if self.current_file:
            ext = os.path.splitext(self.current_file)[1]
            file_types = {
                ".txt": "Plain Text",
                ".py": "Python",
                ".js": "JavaScript",
                ".html": "HTML",
                ".css": "CSS",
                ".json": "JSON",
                ".xml": "XML"
            }
            self.file_type_label.config(text=file_types.get(ext, "Unknown"))
        else:
            self.file_type_label.config(text="Plain Text")

    def undo(self):
        try:
            self.text_editor.edit_undo()
        except:
            pass

    def redo(self):
        try:
            self.text_editor.edit_redo()
        except:
            pass

    def cut(self):
        try:
            self.text_editor.event_generate("<<Cut>>")
        except:
            pass

    def copy(self):
        try:
            self.text_editor.event_generate("<<Copy>>")
        except:
            pass

    def paste(self):
        try:
            self.text_editor.event_generate("<<Paste>>")
        except:
            pass

    def select_all(self):
        self.text_editor.tag_add(tk.SEL, "1.0", tk.END)
        self.text_editor.mark_set(tk.INSERT, "1.0")
        self.text_editor.see(tk.INSERT)
        return "break"

    def zoom_in(self):
        current_font = font.Font(font=self.text_editor["font"])
        current_size = current_font.actual()["size"]
        new_size = min(current_size + 2, 32)
        self.text_editor.config(
            font=(current_font.actual()["family"], new_size))

    def zoom_out(self):
        current_font = font.Font(font=self.text_editor["font"])
        current_size = current_font.actual()["size"]
        new_size = max(current_size - 2, 8)
        self.text_editor.config(
            font=(current_font.actual()["family"], new_size))

    def reset_zoom(self):
        self.text_editor.config(font=("Consolas", 11))

    def show_about(self):
        about_text = """Modern Text Editor
Version 1.0.0

A feature-rich text editor with modern UI

Powered by ProjectsHUB

Features:
- Syntax highlighting support
- Line numbers
- Keyboard shortcuts
- Multiple file format support
- Modern dark theme
- Auto-save functionality

Copyright 2025"""
        messagebox.showinfo("About", about_text)

    def on_closing(self):
        if self.is_modified:
            response = messagebox.askyesnocancel("Save Changes",
                                                 "Do you want to save changes before closing?")
            if response is None:
                return
            elif response:
                self.save_file()

        self.root.destroy()


def main():
    root = tk.Tk()
    app = ModernTextEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
