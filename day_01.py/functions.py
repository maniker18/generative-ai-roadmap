# Functions Practice - Essential for organizing API calls

def get_ai_response(prompt):
    """Simulate getting a response from an AI model."""
    return f"AI says: {prompt}"

# Test the function with 3 different prompts
prompts = ["Hello", "How does AI work?", "Goodbye"]
for prompt in prompts:
    response = get_ai_response(prompt)
    print(response)