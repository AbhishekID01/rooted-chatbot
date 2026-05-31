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

📍 Used for:
{row['used_for']}

⚠️ Risk Level:
{row['risk_level'].title()}

💡 Parent Tip:
{row['parent_tip']}
""".strip()