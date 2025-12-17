def analyze_skills(user_skills, required_skills):

    user_skills = set(user_skills)
    required_skills = set(required_skills)

    matching = user_skills & required_skills
    missing = required_skills - user_skills

    # Skill score calculation
    if len(required_skills) == 0:
        score = 0
    else:
        score = int((len(matching) / len(required_skills)) * 100)

    return matching, missing, score


def recommend_careers(user_skills, career_skills_data):
    

    user_skills = set(user_skills)

    best_career = None
    best_score = 0

    for career, levels in career_skills_data.items():
        beginner_skills = set(levels["beginner"])
        matching = user_skills & beginner_skills

        if len(beginner_skills) == 0:
            continue

        score = int((len(matching) / len(beginner_skills)) * 100)

        if score > best_score:
            best_score = score
            best_career = career

    return best_career, best_score
from data.skill_relations import SKILL_RELATIONS

def find_related_skills(user_skills, missing_skills):
    
    related = {}
    for user_skill in user_skills:
        if user_skill in SKILL_RELATIONS:
            for mapped_skill in SKILL_RELATIONS[user_skill]:
                if mapped_skill in missing_skills:
                    related.setdefault(mapped_skill, []).append(user_skill)
    return related
