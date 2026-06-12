"""
Day 1: Functions and Scope
Learning Objectives:
  - Function definition and calling
  - Parameters and return values
  - Scope (local vs global variables)
  - Docstrings and best practices
  - Practical example: AI response simulation
"""


def get_ai_response(prompt):
    """
    Simulate getting a response from an AI model.
    
    Args:
        prompt (str): The input prompt for the AI model
        
    Returns:
        str: A formatted response string
        
    Example:
        >>> get_ai_response("Hello")
        'AI says: Hello'
    """
    return f"AI says: {prompt}"


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def greet_user(name, age=None):
    """
    Greet a user with optional age information.
    
    Args:
        name (str): User's name
        age (int, optional): User's age. Defaults to None.
        
    Returns:
        str: Personalized greeting
    """
    if age:
        return f"Hello {name}, you are {age} years old!"
    return f"Hello {name}!"


# ============== TESTING ============== 

# Test 1: Basic function call
print("=== Test 1: AI Response ===")
prompts = ["Hello", "How does AI work?", "Goodbye"]
for prompt in prompts:
    response = get_ai_response(prompt)
    print(response)

# Test 2: Mathematical functions
print("\n=== Test 2: Math Operations ===")
print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"5 * 3 = {multiply_numbers(5, 3)}")

# Test 3: Function with optional parameters
print("\n=== Test 3: Greeting Function ===")
print(greet_user("Alice"))
print(greet_user("Bob", 25))

# Test 4: Function scope example
print("\n=== Test 4: Variable Scope ===")
global_var = "I am global"

def function_with_scope():
    local_var = "I am local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

function_with_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error (NameError)