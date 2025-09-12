import wordle
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# loading env:
env = wordle.load_environment(num_train_examples=100, num_eval_examples=20, use_think=True)


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

client = openai.OpenAI(api_key=api_key)

results = env.evaluate(
    client=client, 
    model="gpt-4", 
    num_examples=2,  # avoid rate-limits brugh
    rollouts_per_example=1
)

print("Evaluation completed!")
print(f"Results: {results}")