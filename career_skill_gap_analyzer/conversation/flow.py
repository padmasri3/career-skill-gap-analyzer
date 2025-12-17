from data.career_roles import CAREER_ROLES
from data.career_skills import CAREER_SKILLS
from logic.skill_gap_logic import analyze_skills, recommend_careers
from utils.helpers import clean_skill_input


def start_conversation():
    print("👋 Welcome to Career & Skill Gap Analyzer\n")

    degree = input("🎓 Enter your degree: ").strip()
    skills_input = input("🛠️ Enter your skills (comma separated): ")
    user_skills = clean_skill_input(skills_input)

    print("\n🎯 Available Career Roles by Domain:")
    for domain, roles in CAREER_ROLES.items():
        print(f"\n{domain.title()}:")
        for role in roles:
            print(f" - {role.title()}")

    career = input("\nEnter your target career role: ").lower()
    level = input("📊 Experience level (beginner/intermediate): ").lower()

    # Validate support
    if career not in CAREER_SKILLS:
        print(
            "\n⚠️ Skill analysis not available for this role yet.\n"
            "📌 This role is listed but not supported in current rule base."
        )
        return

    if level not in CAREER_SKILLS[career]:
        print("\n❌ Invalid experience level.")
        return

    required_skills = CAREER_SKILLS[career][level]
    matching, missing, score = analyze_skills(user_skills, required_skills)

    print("\n📘 Skill Gap Report")
    print("-" * 30)

    print("\n✅ Matching Skills:")
    for skill in matching:
        print(f" - {skill}")
    else:
        print(" ❌ None")

    print("\n❌ Missing Skills:")
    for skill in missing:
        print(f" - {skill}")
    print("\nThank you for using the Career & Skill Gap Analyzer! 🚀")
