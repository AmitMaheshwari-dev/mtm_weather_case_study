from weather_ai.data_loader import load_daily, load_monthly
from weather_ai.llm_planner import plan_query
from weather_ai.query_executor import execute_query
from weather_ai.answer_formatter import format_answer

DAILY_FILE = "data/daily_precipitation.xlsx"
MONTHLY_FILE = "data/monthly_precipitation.xlsx"

def main():
    daily_df = load_daily(DAILY_FILE)
    monthly_df = load_monthly(MONTHLY_FILE)

    print("Weather GenAI Assistant (Local, CPU)")
    print("Type 'exit' to quit\n")

    while True:
        question = input("Ask a question: ")
        if question.lower() == "exit":
            break

        plan = plan_query(question)

        from weather_ai.plan_normalizer import normalize_plan
        plan = normalize_plan(plan, daily_df, monthly_df)

        result = execute_query(plan, daily_df, monthly_df)

        answer = format_answer(question, result)

        print(answer)
        print("-" * 60)

if __name__ == "__main__":
    main()