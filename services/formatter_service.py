def format_creator(row):

    return f"""
🎬 {row['name']}

{row['name']} is a {row['creator_type']} known for {row['why_kids_like_it']}.

⚠️ Risk Level:
{row['risk_level'].title()}

💡 Parent Tip:
{row['parent_tip']}
""".strip()


def format_slang(row):

    return f"""
💬 {row['slang'].title()}

{row['meaning']}

📍 Used For:
{row['used_for']}

⚠️ Risk Level:
{row['risk_level'].title()}

💡 Parent Tip:
{row['parent_tip']}
""".strip()


def format_danger(row):

    return f"""
🚨 {row['title']}

Danger Type:
{row['danger_type']}

⚠️ Severity:
{row['severity'].title()}

👀 Signs To Watch:
{row['signs_to_watch']}

💡 Prevention:
{row['prevention_tips']}

🛡️ Parent Action:
{row['parent_actions']}
""".strip()


def format_media(row):

    return f"""
📱 {row['name']}

Official Age:
{row['official_age']}

👨‍👩‍👧 Parent Recommended Age:
{row['parent_recommended_age']}

⚠️ Risk Level:
{row['risk_level'].title()}

🚨 Main Concerns:
{row['main_concerns']}

💡 What Parents Should Know:
{row['what_parents_should_know']}

🔒 Safety Tip:
{row['safety_tips']}
""".strip()


def format_symptom(row):

    return f"""
🩺 {row['symptom']}

⚠️ Urgency:
{row['urgency_level'].title()}

🤔 Possible Causes:
{row['possible_causes']}

👀 Warning Signs:
{row['warning_signs']}

💡 What Parents Should Do:
{row['what_parents_should_do']}
""".strip()


def format_trend(row):

    return f"""
📈 {row['title']}

Platform:
{row['platform']}

⚠️ Risk Level:
{row['risk_level'].title()}

📊 Trend Status:
{row['trend_status']}

📝 What It Is:
{row['what_is_it']}

💡 Parent Advice:
{row['parents_should']}
""".strip()


def format_tough_topic(row):

    return f"""
❤️ {row['title']}

👨 Parent Emotion:
{row['parent_emotion']}

🧒 Child Emotion:
{row['child_emotion']}

💡 What To Do:
{row['what_to_do']}

🎯 Goal:
{row['emotional_goal']}
""".strip()


def format_faq(row):

    return f"""
❓ {row['question']}

✅ Answer:

{row['answer']}
""".strip()