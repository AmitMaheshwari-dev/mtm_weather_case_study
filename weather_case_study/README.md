Weather GenAI Assistant (Local, CPU)

Overview
This project implements a Weather GenAI Assistant that answers natural language questions about historical precipitation data.
The solution demonstrates how a language model can be combined with deterministic data processing to build a reliable analytical assistant.

The system runs fully offline on CPU, uses an open-source language model, and does not require any API keys.
All numerical calculations are performed using Python and pandas to ensure accuracy and reproducibility.

Core Design Principle
GenAI is used only for reasoning and intent extraction.
All precipitation calculations are deterministic and auditable.

This separation ensures that the system does not hallucinate numerical values and behaves predictably even when questions vary in structure.

High-Level Flow
1. A user asks a question in natural language.
2. The language model interprets the question and produces a structured query plan.
3. The query plan is normalized and validated to handle incomplete or inconsistent model output.
4. The normalized plan is executed using pandas on the precipitation datasets.
5. Results are returned as a tabular answer.

If data for the requested time range does not exist, the system safely returns an empty result instead of fabricating values.

Project Structure
weather_case_study/
data/
  daily_precipitation.xlsx
  monthly_precipitation.xlsx
models/
  phi-3-mini-instruct-q4.gguf
weather_ai/
  llm_planner.py
  plan_normalizer.py
  query_executor.py
  data_loader.py
  answer_formatter.py
run_weather_ai.py
requirements.txt
README.md

Setup Instructions
1. Install dependencies using pip install -r requirements.txt
2. Download the open-source model file phi-3-mini-instruct-q4.gguf from Hugging Face.
3. Place the model file inside the models directory.
4. Run the application using python run_weather_ai.py

Example Questions and Expected Behavior

Example 1
Question:
What is the total precipitation of Lucknow in August and September from 2001 to 2005?

Expected behavior:
The assistant interprets this as a district-level monthly aggregation and computes the total precipitation for the specified months and years using the monthly dataset.

Example output:
Year  Month  Monthly Precipitation
2001   8      296.55
2001   9      265.83

Example 2
Question:
Compare precipitation of Maharashtra and Uttar Pradesh between August 1 and August 15, 2001.

Expected behavior:
The assistant treats this as a state-level comparison using daily data and returns the aggregated precipitation for each state over the specified period.

Example 3
Question:
Compare precipitation of Maharashtra and Uttar Pradesh in November 2001.

Expected behavior:
Since the dataset does not contain data for this period, the system returns an empty result or a clear message indicating that data is not available.
No values are hallucinated.

GenAI Usage Disclosure
The system uses an open-source language model (Phi-3 Mini via llama.cpp) exclusively for:
- Understanding natural language questions
- Generating structured query plans

The model is not used for:
- Numerical calculations
- Data aggregation
- Forecasting

All numerical results are computed deterministically using pandas.

Limitations
The assistant can only answer questions for which data exists in the provided datasets.
It does not perform weather forecasting or prediction.
Performance depends on local CPU resources.

Conclusion
This project demonstrates a practical GenAI-assisted analytics system where language models handle reasoning and interpretation, while traditional code ensures correctness and reliability.
