DIAGNOSIS_PROMPT = """
You are an expert software engineer.

Analyze the following bug.

Bug Title:
{title}

Description:
{description}

Source Code:
{code}

Provide:
1. Root cause
2. Suggested fix
3. Confidence (0-100)
"""