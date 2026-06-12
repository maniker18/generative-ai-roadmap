# Lists and Loops Practice - Foundation for batch processing prompts

# Step 1: Create a list
ai_terms = ["AI", "ML", "DL", "NLP", "CV"]

# Step 2: Loop with enumerate to show index and length
for i, term in enumerate(ai_terms):
    print(f"{i}: {term} (length: {len(term)})")