import json
from llama_cpp import Llama

llm = Llama(
    model_path="models/Phi-3-mini-4k-instruct-q4.gguf",
    n_ctx=4096,
    n_threads=8,
    temperature=0.0,
    chat_format=None  
)

SYSTEM_PROMPT = """
You are a weather data query planner.

Return ONLY ONE valid JSON object.
No explanations. No markdown. No extra text.

JSON schema:
{
  "dataset": "daily" | "monthly",
  "aggregation": "sum" | "average",
  "time": {
    "years": [int] | null,
    "months": [int] | null,
    "start_date": "YYYY-MM-DD" | null,
    "end_date": "YYYY-MM-DD" | null
  },
  "geography": {
    "level": "state" | "district",
    "state": string | null,
    "district": string | null,
    "compare": [string] | null
  },
  "output": "table" | "text"
}
"""

def extract_json_strict(text: str) -> dict:
    """
    Parse JSON by tracking brace balance.
    This is the ONLY reliable way with local LLMs.
    """
    print("\n--- RAW MODEL OUTPUT ---")
    print(text)
    print("--- END RAW OUTPUT ---\n")

    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON start found")

    brace_count = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            brace_count += 1
        elif text[i] == "}":
            brace_count -= 1
            if brace_count == 0:
                json_text = text[start:i+1]
                return json.loads(json_text)

    raise ValueError("JSON not balanced")

def plan_query(question: str) -> dict:
    primary_prompt = f"""
    {SYSTEM_PROMPT}

    Question:
    {question}

    Return JSON only.
    """

    output = llm(
        primary_prompt,
        max_tokens=256
    )

    raw_text = output["choices"][0]["text"].strip()

    # Retry once with a simpler prompt if empty
    if not raw_text:
        print("Empty LLM output, retrying with fallback prompt")

        fallback_prompt = f"""
Convert the following question into a JSON object following the schema.

Question:
{question}

JSON:
"""

        output = llm(
            fallback_prompt,
            max_tokens=256
        )

        raw_text = output["choices"][0]["text"].strip()

    return extract_json_strict(raw_text)