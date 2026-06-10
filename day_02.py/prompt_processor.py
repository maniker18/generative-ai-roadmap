# Prompt Processor - Save chat history to file

prompts = []
responses = []

print("Enter 3 prompts (or 'done' to finish early):")

for i in range(3):
    user_input = input(f"\nPrompt {i+1}: ").strip()
    if user_input.lower() == "done":
        break
    
    # Simulate AI response
    response = f"AI response to: '{user_input}'"
    prompts.append(user_input)
    responses.append(response)
    print(f"AI: {response}")

# Save to file
with open("results.txt", "w") as f:
    for p, r in zip(prompts, responses):
        f.write(f"You: {p}\nAI: {r}\n\n")

# Count total characters
total_chars = sum(len(p) for p in prompts)
print(f"\nSaved {len(prompts)} exchanges to results.txt")
print(f"Total characters in prompts: {total_chars}")