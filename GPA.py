import tkinter as tk
from tkinter import messagebox


class MarkSheetCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Mark Sheet Calculator")
        self.master.geometry("300x200")

        self.subjects = ["Python", "MATH 1", "MOTO VEHICLE", "VB.NET", "STATISTICS"]  # Add your subjects here
        self.grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]  # Grades scale

        self.credit_label = tk.Label(master, text="Enter Credits:")
        self.credit_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.credit_entries = []
        for i, subject in enumerate(self.subjects):
            label = tk.Label(master, text=subject)
            label.grid(row=i + 1, column=0, padx=5, pady=5, sticky="e")

            entry = tk.Entry(master)
            entry.grid(row=i + 1, column=1, padx=5, pady=5)
            self.credit_entries.append(entry)

        self.grade_label = tk.Label(master, text="Enter Grades:")
        self.grade_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.grade_entries = []
        for i, subject in enumerate(self.subjects):
            label = tk.Label(master, text=subject)
            label.grid(row=i + 1, column=2, padx=5, pady=5, sticky="e")

            grade_var = tk.StringVar(master)
            grade_var.set(self.grades[0])
            entry = tk.OptionMenu(master, grade_var, *self.grades)
            entry.grid(row=i + 1, column=3, padx=5, pady=5)
            self.grade_entries.append(grade_var)

        self.submit_button = tk.Button(master, text="Submit", command=self.calculate_sgpa)
        self.submit_button.grid(row=len(self.subjects) + 1, columnspan=4, pady=10)

    def calculate_sgpa(self):
        total_credits = 0
        total_points = 0

        for i, subject in enumerate(self.subjects):
            try:
                credits = int(self.credit_entries[i].get())
                grade = self.grade_entries[i].get()

                if grade == "A":
                    points = 10
                elif grade == "A":
                    points = 9
                elif grade == "A-":
                    points = 8
                elif grade == "B+":
                    points = 7
                elif grade == "B":
                    points = 6
                elif grade == "B-":
                    points = 5
                elif grade == "C+":
                    points = 4
                elif grade == "C":
                    points = 3
                elif grade == "C-":
                    points = 2
                elif grade == "D":
                    points = 1
                else:
                    points = 0

                total_credits += credits
                total_points += credits * points
            except ValueError:
                messagebox.showerror("Error", "Please enter valid credits for all subjects.")
                return

        if total_credits == 0:
            messagebox.showerror("Error", "Total credits cannot be zero.")
            return

        sgpa = total_points / total_credits
        messagebox.showinfo("Result", f"Total Credits: {total_credits}\nSGPA: {sgpa:.2f}")


def main():
    root = tk.Tk()
    app = MarkSheetCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
