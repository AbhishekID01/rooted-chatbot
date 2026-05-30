def build_slang_response(row):

    response = f"""
Yeah, this one's everywhere right now.

{row['parent_translation']}

One thing to keep an eye on: {row['parent_tip']}
"""

    return response.strip()