import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from collections import Counter

# Load API key
load_dotenv()
client = OpenAI()

# Define the problem
question = "If a hen and a half lays an egg and a half in a day and a half, how many eggs do three hens lay in three days?"

# Chain-of-thought prompting template
cot_prompt = f"""
Let's solve this step by step.

Question: {question}
"""

# Store results
final_answers = []

# Run multiple generations with diversity
for _ in range(10):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1.2,  # High temperature for diverse reasoning paths
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant that explains your reasoning step by step before giving an answer."},
            {"role": "user", "content": cot_prompt}
        ]
    )
    
    # Extract the assistant's reply
    reply = response.choices[0].message.content.strip()
    
    # Try to extract the final number from the answer (you could improve this with regex)
    for line in reply.split("\n")[::-1]:
        if any(char.isdigit() for char in line):
            try:
                num = int([s for s in line.split() if s.isdigit()][-1])
                final_answers.append(num)
                break
            except:
                continue

# Analyze most frequent answer
counts = Counter(final_answers)
most_common = counts.most_common(1)[0]

print(f"\n🧠 Self-Consistency Summary:\n")
print("All Results:", final_answers)
print(f"✅ Most Consistent Answer: {most_common[0]} (appeared {most_common[1]} times)")
