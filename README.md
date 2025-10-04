# Langgraph Workflows Collection

This repository contains a series of workflow examples using [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain) with Google's Gemini LLM. Each file demonstrates a unique use case, from simple LLM Q&A to advanced tool integration and fault tolerance.

## Prerequisites

- Python 3.8+
- Install dependencies:
  ```sh
  pip install langchain langchain-google-genai langgraph python-dotenv pydantic requests


  File-by-File Explanation
1. 1_bmi_workflow.py
Purpose:
Calculates Body Mass Index (BMI) and categorizes it.

Workflow:

Defines a state with weight, height, BMI, and category.
Calculates BMI from weight and height.
Labels BMI as Underweight, Normal, Overweight, or Obesity.
Uses a simple graph: START → calculate_bmi → label_bmi → END.
2. 2_simple_llm_workflow.py
Purpose:
Single-step LLM Q&A workflow.

Workflow:

Loads API key from .env.
Initializes Gemini model.
Defines state with question and answer.
Node function sends question to Gemini and stores answer.
Graph: START → llm_qa → END.
3. 3_prompt_chaining.py
Purpose:
Chained prompt workflow for blog generation.

Workflow:

State includes blog title, outline, and content.
First node generates an outline from the title.
Second node writes a blog using the outline.
Graph: START → create_outline → create_blog → END.

4. 4_batsman_workflow.py
Purpose:
Cricket batsman statistics calculator.

Workflow:

State includes runs, balls, boundaries, strike rate, balls per boundary, boundary percent, and summary.
Parallel nodes calculate strike rate, balls per boundary, and boundary percent.
All results are summarized in a final node.
Graph:

START → calculate_sr → summary → END
       → calculate_bpb → summary
       → calculate_boundary_percent → summary
       
5. 5_UPSC_essay_workflow.py
Purpose:
Automated evaluation of UPSC-style essays.

Workflow:

Uses Gemini with structured output (Pydantic schema).
State tracks essay, feedbacks, scores, and averages.
Three parallel nodes evaluate language, analysis, and clarity.
Final node summarizes feedback and computes average score.
Graph:
START → evaluate_language → final_evaluation → END
       → evaluate_analysis → final_evaluation
       → evaluate_thought → final_evaluation
       
6. 6_quadratic_equation_workflow.py
Purpose:
Solves quadratic equations and determines root types.

Workflow:

State includes coefficients, equation string, discriminant, and result.
Nodes show equation, calculate discriminant, and branch to root calculation based on discriminant.
Graph:
START → show_equation → calculate_discriminant
                           → real_roots → END
                           → repeated_roots → END
                           → no_real_roots → END
                           
7. 7_review_reply_workflow.py
Purpose:
Automated review sentiment analysis and reply generation.

Workflow:

Uses Gemini with structured output for sentiment and diagnosis.
State tracks review, sentiment, diagnosis, and response.
Nodes:
find_sentiment: Detects sentiment.
Conditional: If positive, generates thank-you reply; if negative, diagnoses issue and generates empathetic response.
Graph:START → find_sentiment → [positive_response → END | run_diagnosis → negative_response → END]

8. 8_X_post_generator.py
Purpose:
Generates and iteratively improves X (Twitter) posts.

Workflow:

State tracks topic, tweet, evaluation, feedback, iteration, and histories.
Nodes:
generate: Creates initial tweet.
evaluate: Critiques tweet using structured output.
Conditional: If approved or max iterations reached, finish; else, optimize and repeat.
Graph:START → generate → evaluate → [approved → END | needs_improvement → optimize → evaluate]

9. 9_basic_chatbot.py
Purpose:
Basic chatbot using Gemini.

Workflow:

State tracks message history.
Node sends messages to Gemini and returns response.
Loop for interactive chat in terminal.
Graph: START → chat_node → END.

10. 10_persistence.py
Purpose:
Demonstrates workflow persistence and checkpointing.

Workflow:

State tracks joke topic, joke, and explanation.
Nodes generate joke and explanation.
Uses InMemorySaver for checkpointing.
Supports time travel (state update and resume).
Graph: START → generate_joke → generate_explaination → END.

11. 10.1_Fault_Tolerance.py
Purpose:
Demonstrates fault tolerance and recovery in workflows.

Workflow:

State tracks input and step completions.
Simulates a long-running/hanging step.
Uses checkpointing to resume after interruption.
Graph: step_1 → step_2 → step_3 → END.

12. 11_tools.py
Purpose:
Tool-augmented chatbot with search, calculator, and stock price tools.

Workflow:

State tracks message history.
Tools: DuckDuckGo search, calculator, stock price fetch.
LLM can invoke tools as needed.
Conditional edge routes to tool node if tool call is required.
Graph:START → chat_node → [tools → chat_node | END]

Environment File
.env: Stores your Gemini API key.
Usage
Run any workflow file directly:

For interactive chat, run:

 by GitHub Copilot.

GPT-4.1 • 1x
