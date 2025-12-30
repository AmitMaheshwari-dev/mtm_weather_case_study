def format_answer(question, df):
    return f"""
Question:
{question}

Answer:
{df.to_string(index=False)}
"""