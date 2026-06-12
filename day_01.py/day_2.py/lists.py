"""
Day 2: Data Structures - Lists, Sets, and Dictionaries
Learning Objectives:
  - List operations: sort, remove, search
  - Set operations: union, intersection, difference
  - Dictionary operations: create, update, delete, iterate
  - Nested loops and iteration
  - When to use each data structure
"""

# ============== LISTS ==============

def demo_lists():
    """Demonstrate list operations."""
    print("=== LISTS ===")
    sports = ["cricket", "football", "basketball", "tennis"]
    
    # Sort a list
    sorted_sports = sorted(sports)
    print(f"Sorted sports: {sorted_sports}")
    
    # Remove an item
    sports.remove("cricket")
    print(f"After removing cricket: {sports}")
    
    # Check if item exists
    print(f"'tennis' in sports: {'tennis' in sports}")
    
    # Enumerate with index
    print("Enumerated list:")
    for ind, sport in enumerate(sports, start=1):
        print(f"  {ind}: {sport}")


# ============== SETS ==============

def demo_sets():
    """Demonstrate set operations."""
    print("\n=== SETS ===")
    set1 = set(["cricket", "football", "basketball", "tennis"])
    set2 = {'boxing', 'badminton', 'volleyball', 'cricket'}
    
    # Set operations
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Intersection (common sports): {set1.intersection(set2)}")
    print(f"Union (all sports): {set1.union(set2)}")
    print(f"Difference (in set1 but not set2): {set1.difference(set2)}")
    print(f"Difference (in set2 but not set1): {set2.difference(set1)}")


# ============== DICTIONARIES ==============

def demo_dictionaries():
    """Demonstrate dictionary operations."""
    print("\n=== DICTIONARIES ===")
    
    # Create and initialize
    person = {
        'name': 'Manik',
        'age': 25,
        'city': 'New York'
    }
    print(f"Original: {person}")
    
    # Update existing key
    person.update({'age': 26, 'course': 'CSE'})
    print(f"After update: {person}")
    
    # Delete a key
    del person['city']
    print(f"After deletion: {person}")
    
    # Add new key
    person['degree'] = 'Computer Science'
    print(f"After adding degree: {person}")
    
    # Get with default value
    result = person.get('age', 'not found')
    print(f"Age: {result}")
    
    # Iterate over items
    print("\nIterating over dictionary:")
    for key, value in person.items():
        print(f"  {key}: {value}")
    
    # Get keys and values
    print(f"\nKeys: {person.keys()}")
    print(f"Values: {person.values()}")


# ============== LOOPS AND CONTROL FLOW ==============

def demo_nested_loops():
    """Demonstrate nested loops with sets."""
    print("\n=== NESTED LOOPS ===")
    
    set_numbers = {1, 2, 3}
    chars = 'acd'
    
    # Nested loop: print each character for each number
    print("Nested loop output (single line per character):")
    for char in chars:
        for num in set_numbers:
            print(char, end="")  # Print without newline
        print()  # Print newline after inner loop


def demo_while_loops():
    """Demonstrate while loops."""
    print("\n=== WHILE LOOPS ===")
    
    # Simple while loop
    print("Counting up to 15:")
    x = 10
    while x < 15:
        print(x, end=" ")
        x += 1
    print()  # New line


def demo_break_statement():
    """Demonstrate break statement in loops."""
    print("\n=== BREAK STATEMENT ===")
    
    print("Nested loop with break condition:")
    for i in range(5):
        while True:
            print(i, end=" ")
            break  # Exit while loop immediately
    print()  # New line


# ============== CHARACTER PATTERN EXAMPLE ==============

def print_character_pattern():
    """Print a simple character pattern."""
    print("\n=== CHARACTER PATTERN ===")
    
    set_numbers = {1, 2, 3}
    for char in 'acd':
        for _ in set_numbers:
            print(char, end="")
        print()  # Newline for each character
    

# ============== MAIN EXECUTION ==============

if __name__ == "__main__":
    """Run all demonstrations."""
    demo_lists()
    demo_sets()
    demo_dictionaries()
    demo_nested_loops()
    demo_while_loops()
    demo_break_statement()
    print_character_pattern()
    
    print("\n✅ All examples completed successfully!")

      