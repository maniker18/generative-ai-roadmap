"""
String Practice: Essential for GenAI Text Processing
Learning Objectives:
  - String methods: strip, upper, lower, replace, split, join
  - String formatting: f-strings, format(), %
  - String slicing and indexing
  - String immutability
  - Method chaining
  - Text processing patterns for NLP
"""


def string_methods_demo():
    """Demonstrate common string methods."""
    print("=== STRING METHODS ===")
    
    sentence = "  Hello, Generative AI World!  "
    print(f"Original: '{sentence}'")
    
    # Individual methods
    print(f"strip(): '{sentence.strip()}'")
    print(f"upper(): '{sentence.upper()}'")
    print(f"lower(): '{sentence.lower()}'")
    print(f"replace('World', 'Universe'): '{sentence.replace('World', 'Universe')}'")
    
    # Method chaining
    print("\nMethod Chaining:")
    chained = sentence.strip().upper().replace("WORLD", "UNIVERSE").lower()
    print(f"Chained result: '{chained}'")


def string_formatting_demo():
    """Demonstrate string formatting methods."""
    print("\n=== STRING FORMATTING ===")
    
    name = "Manik"
    age = 25
    city = "New York"
    
    # Method 1: f-strings (modern, recommended)
    print("f-string:")
    print(f"  My name is {name}, I'm {age} years old, from {city}")
    
    # Method 2: format()
    print("format():")
    print("  My name is {}, I'm {} years old, from {}".format(name, age, city))
    
    # Method 3: % formatting (older)
    print("% formatting:")
    print("  My name is %s, I'm %d years old, from %s" % (name, age, city))
    
    # Formatting numbers
    print("\nNumber formatting:")
    pi = 3.14159
    print(f"  Pi (2 decimals): {pi:.2f}")
    print(f"  Pi (4 decimals): {pi:.4f}")


def string_slicing_demo():
    """Demonstrate string slicing and indexing."""
    print("\n=== STRING SLICING & INDEXING ===")
    
    text = "Generative"
    print(f"String: '{text}'")
    print(f"Length: {len(text)}")
    
    # Indexing
    print(f"First char [0]: '{text[0]}'")
    print(f"Last char [-1]: '{text[-1]}'")
    print(f"Char at index 3: '{text[3]}'")
    
    # Slicing
    print(f"Slice [0:5]: '{text[0:5]}'")
    print(f"Slice [5:]: '{text[5:]}'")
    print(f"Slice [:-4]: '{text[:-4]}'")
    print(f"Slice [::2] (every 2nd): '{text[::2]}'")
    print(f"Slice [::-1] (reversed): '{text[::-1]}'")


def split_join_demo():
    """Demonstrate split and join operations."""
    print("\n=== SPLIT & JOIN ===")
    
    # Split
    sentence = "Python is awesome for AI development"
    print(f"Original: '{sentence}'")
    
    words = sentence.split()
    print(f"Split by space: {words}")
    
    csv = "apple,banana,orange,grape"
    fruits = csv.split(",")
    print(f"Split by comma: {fruits}")
    
    # Join
    print("\nJoin operations:")
    joined = " - ".join(words)
    print(f"Join with ' - ': '{joined}'")
    
    joined_csv = ",".join(fruits)
    print(f"Join with ',': '{joined_csv}'")


def string_search_demo():
    """Demonstrate string search operations."""
    print("\n=== STRING SEARCH ===")
    
    text = "Generative AI is transforming the world"
    
    # Find substring
    print(f"String: '{text}'")
    print(f"'AI' in text: {'AI' in text}")
    print(f"'ML' in text: {'ML' in text}")
    
    # Index and count
    print(f"Index of 'AI': {text.find('AI')}")
    print(f"Count of 'i': {text.count('i')}")
    print(f"Starts with 'Generative': {text.startswith('Generative')}")
    print(f"Ends with 'world': {text.endswith('world')}")


def text_processing_pipeline():
    """Demonstrate a text processing pipeline (useful for NLP)."""
    print("\n=== TEXT PROCESSING PIPELINE ===")
    
    raw_text = "  Hello World!!! This is Generative AI...  "
    print(f"Raw: '{raw_text}'")
    
    # Step 1: Clean whitespace
    step1 = raw_text.strip()
    print(f"Step 1 (strip): '{step1}'")
    
    # Step 2: Remove punctuation (simple version)
    step2 = step1.replace("!", "").replace(".", "").replace("?", "")
    print(f"Step 2 (remove punctuation): '{step2}'")
    
    # Step 3: Convert to lowercase
    step3 = step2.lower()
    print(f"Step 3 (lowercase): '{step3}'")
    
    # Step 4: Split into words
    step4 = step3.split()
    print(f"Step 4 (split into words): {step4}")
    
    # Step 5: Filter empty strings
    step5 = [word for word in step4 if word]
    print(f"Step 5 (filter empty): {step5}")


def advanced_string_demo():
    """Demonstrate advanced string operations."""
    print("\n=== ADVANCED STRING OPERATIONS ===")
    
    # Case operations
    text = "Generative AI"
    print(f"Original: {text}")
    print(f"Title: {text.title()}")
    print(f"Swap case: {text.swapcase()}")
    print(f"Capitalize: {text.capitalize()}")
    
    # Padding
    print("\nPadding:")
    word = "AI"
    print(f"Center (width=10): '{word.center(10)}'")
    print(f"Left-align (width=10): '{word.ljust(10)}'")
    print(f"Right-align (width=10): '{word.rjust(10)}'")
    print(f"Pad with zeros (width=10): '{word.zfill(10)}'")
    
    # Check methods
    print("\nCheck methods:")
    print(f"'123'.isdigit(): {'123'.isdigit()}")
    print(f"'abc'.isalpha(): {'abc'.isalpha()}")
    print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
    print(f"'   '.isspace(): {'   '.isspace()}")


# ============== MAIN EXECUTION ==============

if __name__ == "__main__":
    string_methods_demo()
    string_formatting_demo()
    string_slicing_demo()
    split_join_demo()
    string_search_demo()
    text_processing_pipeline()
    advanced_string_demo()
    
    print("\n✅ All string examples completed successfully!")
