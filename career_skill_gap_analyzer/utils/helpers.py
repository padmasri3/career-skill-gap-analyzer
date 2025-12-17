# Helper functions

def clean_skill_input(skills_string):
    return [skill.strip().lower() for skill in skills_string.split(",")]
