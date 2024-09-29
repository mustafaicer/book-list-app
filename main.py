import customtkinter as tk
from customtkinter import CTkScrollableFrame

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Book List App")
        self.minsize(width=450, height=420)
        self.maxsize(width=450, height=420)
        self.config(padx=20, pady=20)

        # UI
        header_label = tk.CTkLabel(self, text="Book List App", font=('Arial', 24, 'bold'))
        header_label.place(relx=0.29, rely=0.0)

        self.input_entry = tk.CTkEntry(self, width=410)
        self.input_entry.place(relx=0.0, rely=0.1)

        search_button = tk.CTkButton(self, text="Search", width=203, command=self.search_book)
        search_button.place(relx=0.0, rely=0.2)

        add_button = tk.CTkButton(self, text="Add", width=203, command=self.add_book)
        add_button.place(relx=0.504, rely=0.2)

        self.list_frame = CTkScrollableFrame(self, fg_color="#8D6F3A", width=386)
        self.list_frame.place(relx=0.0, rely=0.3)

        self.info_label = tk.CTkLabel(self, font=('Arial', 21, 'bold'), pady=10, padx=10)

        for book in books:
            self.list_label = tk.CTkLabel(master=self.list_frame, text=f"{book}", font=('Arial', 18, 'bold'))
            self.list_label.pack()

        self.display_books()

    # Functions
    def display_books(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for book in books:
            list_label = tk.CTkLabel(master=self.list_frame, text=f"{book}", font=('Arial', 18, 'bold'))
            list_label.pack()

    def search_book(self):
        searchin_book = self.input_entry.get()

        if searchin_book:
            self.input_entry.delete(0, tk.END)

            if searchin_book in books:
                self.info_label.configure(text=f"{searchin_book} in your list")

            else:
                self.info_label.configure(text=f"{searchin_book} not found")

            self.info_label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    def add_book(self):
        new_book = self.input_entry.get()

        if new_book:
            self.input_entry.delete(0, tk.END)

            books.append(new_book)

            self.info_label.configure(text=f"{new_book} successfully added")
            self.info_label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

            self.display_books()

# List
books = [
    "Kuyucaklı Yusuf",
    "Kürk mantolu Madonna",
    "Milenyaya Mektuplar",
    "Kardeşimin hikayesi",
    "Serenad",
    "Marslı",
    "Suç ve Ceza",
    "Sherlock Holmes",
    "1984",
    "Ademden önce",
    "Kamelyalı kadın",
    "Tutunamayanlar"
]

if __name__ == "__main__":
    window = App()
    window.mainloop()