# career-skill-gap-analyzer
A rule-based Python chatbot that analyzes students' current skills and identifies gaps for a chosen career path using deterministic logic.
Absolutely! Let’s turn all of your notes into a **professional, neat, interview-ready README.md** with clear explanations, usage instructions, and file-by-file descriptions. I’ve structured it so anyone reviewing your project (including interviewers) can immediately understand what’s going on.

## 📂 Project Structure
career_skill_gap_analyzer/
│
├── conversation/
│   └── flow.py                # Console-based guided conversation
│
├── data/
│   ├── career_roles.py        # Lists all career roles by domain
│   ├── career_skills.py       # Maps career roles to required skills (beginner/intermediate)
│   └── skill_relations.py     # Defines related skills for partial credit in skill matching
│
├── examples/
│   └── sample_run.txt         # Example input/output runs
│
├── logic/
│   └── skill_gap_logic.py     # Core business logic: skill gap analysis & related skills
│
├── ui/
│   └── gui.py                 # Tkinter-based desktop GUI interface
│
├── utils/
│   └── helpers.py             # Helper functions for input cleaning & preprocessing
│
└── main.py                    # Entry point for console or GUI mode

## ⚙️ Features

* Step-by-step guided conversation for students
* Skill gap analysis:

  * ✅ Matching skills
  * ❌ Missing skills
  * 🔁 Related skills (partial credit based on pre-mapped skills)
* Skill match score (0–100%)
* Beginner → Intermediate learning roadmap
* Desktop GUI interface (Tkinter)
* Fully deterministic and rule-based (no AI required)

## 🛠 How It Works

1. **User Inputs:**

   * Current degree
   * Current skills (comma-separated)
   * Target career role
   * Experience level (beginner/intermediate)

2. **System Logic:**

   * Compares user skills with predefined career skill requirements
   * Calculates matching skills, missing skills, and skill match score
   * Suggests related skills the user already has (partial credit)

3. **Output:**

   * Skill gap report (matching, missing, related skills)
   * Skill match score
   * Suggested learning roadmap

---

## 🖥 Example Run

🎓 Enter your degree: BTech
🛠 Enter your skills: python, sql, power bi
🎯 Target career role: Machine Learning Engineer
📊 Experience level: beginner

📘 Skill Gap Report
------------------------------
✅ Matching Skills:
 - python

❌ Missing Skills:
 - statistics
 - linear algebra

🔁 Related Skills You Already Have:
 - statistics (supported by: power bi)
Skill Match Score: 33%
```

### GUI Example:

* Enter all inputs in the Tkinter form
* Click **Analyze Skills**
* Skill gap report shown in output box with:

  * Matching skills
  * Missing skills
  * Related skills
  * Skill match score


## 📌 File Descriptions

### 1️⃣ `conversation/flow.py`

* Handles **console-based user interaction**
* Guides the user through entering degree, skills, career, and experience level
* Calls `analyze_skills` and `find_related_skills` from the logic module
* Displays skill gap report

### 2️⃣ `data/career_roles.py`

* Stores all career roles categorized by domain
* Used for both console and GUI dropdowns
* Easily expandable

### 3️⃣ `data/career_skills.py`

* Maps career roles to required skills at **beginner** and **intermediate** levels
* Example:

```python
"data analyst": {
    "beginner": ["excel", "sql", "statistics"],
    "intermediate": ["python", "power bi", "data visualization"]
}
```

### 4️⃣ `data/skill_relations.py`

* Maps related skills for partial credit
* Example:

```python
SKILL_RELATIONS = {
    "power bi": ["statistics", "data analysis"]
}
```

### 5️⃣ `examples/sample_run.txt`

* Contains **sample input/output** runs for demonstration
* Useful for **project submission or interviews**

### 6️⃣ `logic/skill_gap_logic.py`

* Core business logic of the project
* Functions:

  * `analyze_skills(user_skills, required_skills)` → returns matching, missing skills, and score
  * `find_related_skills(user_skills, missing_skills)` → finds partial credit from related skills
* Keeps computation separate from UI

### 7️⃣ `ui/gui.py`

* Tkinter-based **desktop GUI**
* Allows user to enter degree, skills, career, and experience level
* Shows skill gap report in structured GUI output box
* Easily upgradeable to web-based interface

### 8️⃣ `utils/helpers.py`

* Helper functions for **cleaning and preprocessing inputs**
* Example:

  * `clean_skill_input()` → strips spaces, converts to lowercase, splits comma-separated skills

### 9️⃣ `main.py`

* Entry point for the project
* Can run **console version**:

```python
from conversation.flow import start_conversation
start_conversation()
```

* Or **GUI version**:

```python
from ui.gui import launch_gui
launch_gui()
```

## 💡 Technical Highlights

* Modular design: separates UI, logic, and data layers
* Deterministic, rule-based outputs (no ML/AI)
* Easily extensible: add new careers, skills, or relations
* Interview-ready: demonstrates clean software design and Python best practices

## ⚡ How to Run

### Console Version:

```bash
python main.py
```

### GUI Version:

```bash
python main.py
```

* Tkinter GUI opens automatically
* Enter inputs and click **Analyze Skills**

---

If you want, I can also **create a ready-to-run zip folder with all the files pre-configured**, so you just unzip and run `python main.py` with **no errors**, fully working with GUI and console.

Do you want me to do that next?
