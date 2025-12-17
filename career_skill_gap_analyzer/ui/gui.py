import tkinter as tk
from tkinter import ttk, messagebox

from data.career_skills import CAREER_SKILLS
from logic.skill_gap_logic import analyze_skills, find_related_skills
from utils.helpers import clean_skill_input



class CareerSkillGapGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Career & Skill Gap Analyzer")
        self.root.geometry("650x550")

        self.create_widgets()

    def create_widgets(self):

        tk.Label(self.root, text="Career & Skill Gap Analyzer", font=("Arial", 16, "bold")).pack(pady=10)

        # Degree
        tk.Label(self.root, text="Degree").pack()
        self.degree_entry = tk.Entry(self.root, width=40)
        self.degree_entry.pack()

        # Skills
        tk.Label(self.root, text="Your Skills (comma separated)").pack(pady=5)
        self.skills_entry = tk.Entry(self.root, width=40)
        self.skills_entry.pack()

        # Career Dropdown
        tk.Label(self.root, text="Target Career Role").pack(pady=5)
        self.career_var = tk.StringVar()
        careers = sorted(CAREER_SKILLS.keys())
        self.career_menu = ttk.Combobox(self.root, textvariable=self.career_var, values=careers)
        self.career_menu.pack()

        # Level Dropdown
        tk.Label(self.root, text="Experience Level").pack(pady=5)
        self.level_var = tk.StringVar()
        self.level_menu = ttk.Combobox(self.root, textvariable=self.level_var, values=["beginner", "intermediate"])
        self.level_menu.pack()

        # Button
        tk.Button(self.root, text="Analyze Skills", command=self.analyze).pack(pady=10)

        # Output Box
        self.output = tk.Text(self.root, height=15, width=75)
        self.output.pack(pady=10)

    def analyze(self):
        self.output.delete("1.0", tk.END)

        skills = clean_skill_input(self.skills_entry.get())
        career = self.career_var.get()
        level = self.level_var.get()

        if career not in CAREER_SKILLS or level not in CAREER_SKILLS[career]:
            messagebox.showerror("Error", "Invalid career or experience level")
            return

        required = CAREER_SKILLS[career][level]
        matching, missing, score = analyze_skills(skills, required)
        related = find_related_skills(skills, missing)

        self.output.insert(tk.END, f"Skill Match Score: {score}%\n\n")

        self.output.insert(tk.END, "Matching Skills:\n")
        for s in matching:
            self.output.insert(tk.END, f" - {s}\n")

        self.output.insert(tk.END, "\nMissing Skills:\n")
        for s in missing:
            self.output.insert(tk.END, f" - {s}\n")

        if related:
            self.output.insert(tk.END, "\nRelated Skills:\n")
            for k, v in related.items():
                self.output.insert(tk.END, f" - {k} (from {', '.join(v)})\n")


def launch_gui():
    root = tk.Tk()
    CareerSkillGapGUI(root)
    root.mainloop()
