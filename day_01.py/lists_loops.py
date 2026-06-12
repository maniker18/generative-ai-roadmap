"""
Lists and Loops Practice: Foundation for Batch Processing
Learning Objectives:
  - List creation and manipulation
  - For loops and enumerate()
  - List comprehensions
  - Loop control: break and continue
  - Filtering and transforming lists
  - Batch processing patterns
"""


def basic_list_operations():
    """Demonstrate basic list operations."""
    print("=== BASIC LIST OPERATIONS ===")
    
    # Create lists
    ai_terms = ["AI", "ML", "DL", "NLP", "CV"]
    numbers = [1, 2, 3, 4, 5]
    
    print(f"AI Terms: {ai_terms}")
    print(f"Numbers: {numbers}")
    
    # Basic operations
    print(f"First item: {ai_terms[0]}")
    print(f"Last item: {ai_terms[-1]}")
    print(f"Length: {len(ai_terms)}")
    print(f"Slice [1:3]: {ai_terms[1:3]}")


def enumerate_example():
    """Demonstrate enumerate for index tracking."""
    print("\n=== ENUMERATE EXAMPLE ===")
    
    ai_terms = ["AI", "ML", "DL", "NLP", "CV"]
    
    # Loop with enumerate to show index and value
    print("With enumerate:")
    for i, term in enumerate(ai_terms):
        print(f"  {i}: {term} (length: {len(term)})")
    
    # Starting from index 1
    print("\nWith enumerate (start=1):")
    for i, term in enumerate(ai_terms, start=1):
        print(f"  {i}: {term}")


def list_comprehension_example():
    """Demonstrate list comprehensions."""
    print("\n=== LIST COMPREHENSION ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Traditional approach
    squares_traditional = []
    for num in numbers:
        squares_traditional.append(num ** 2)
    print(f"Squares (traditional): {squares_traditional}")
    
    # List comprehension
    squares_comp = [num ** 2 for num in numbers]
    print(f"Squares (comprehension): {squares_comp}")
    
    # With condition
    even_squares = [num ** 2 for num in numbers if num % 2 == 0]
    print(f"Even squares: {even_squares}")


def break_continue_example():
    """Demonstrate break and continue statements."""
    print("\n=== BREAK AND CONTINUE ===")
    
    # Break example
    print("Break (stop at 5):")
    for i in range(1, 11):
        if i == 5:
            print(f"  Breaking at {i}")
            break
        print(f"  {i}", end=" ")
    print()
    
    # Continue example
    print("Continue (skip even numbers):")
    for i in range(1, 11):
        if i % 2 == 0:
            continue  # Skip this iteration
        print(f"  {i}", end=" ")
    print()


def batch_processing_example():
    """Demonstrate batch processing pattern useful for APIs."""
    print("\n=== BATCH PROCESSING ===")
    
    # Simulate batch processing of prompts
    prompts = [
        "What is AI?",
        "Explain ML",
        "What is NLP?",
        "Tell me about computer vision",
        "What is deep learning?"
    ]
    
    batch_size = 2
    print(f"Processing {len(prompts)} prompts in batches of {batch_size}:")
    
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i+batch_size]
        print(f"\n  Batch {i//batch_size + 1}: {batch}")
        # In real code, you would send this batch to an API
        for prompt in batch:
            print(f"    - Processing: {prompt}")


def filter_and_transform():
    """Filter and transform lists."""
    print("\n=== FILTER AND TRANSFORM ===")
    
    words = ["python", "java", "javascript", "go", "rust"]
    
    # Filter words with length > 4
    long_words = [word for word in words if len(word) > 4]
    print(f"Long words: {long_words}")
    
    # Transform to uppercase
    uppercase = [word.upper() for word in words]
    print(f"Uppercase: {uppercase}")
    
    # Transform to title case with length
    transformed = [f"{word.title()} ({len(word)})" for word in words]
    print(f"Transformed: {transformed}")


def nested_loops_example():
    """Demonstrate nested loops."""
    print("\n=== NESTED LOOPS ===")
    
    print("Multiplication table:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i}×{j}={i*j}", end="  ")
        print()  # New line after inner loop


# ============== MAIN EXECUTION ==============

if __name__ == "__main__":
    basic_list_operations()
    enumerate_example()
    list_comprehension_example()
    break_continue_example()
    batch_processing_example()
    filter_and_transform()
    nested_loops_example()
    
    print("\n✅ All examples completed successfully!")
