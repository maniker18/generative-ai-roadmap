"""
Conditionals Practice: Decision Making in Code
Learning Objectives:
  - If, elif, else statements
  - Comparison operators: ==, !=, <, >, <=, >=
  - Logical operators: and, or, not
  - Boolean values and truthiness
  - Writing clean conditional logic
"""


def age_category(age):
    """
    Determine age category based on age value.
    
    Args:
        age (int): Person's age
        
    Returns:
        str: Age category description
    """
    if age < 13:
        return "You're a kid!"
    elif age <= 19:
        return "You're a teenager!"
    else:
        return "You're an adult!"


def check_grades(score):
    """
    Assign letter grade based on score.
    
    Args:
        score (int): Score out of 100
        
    Returns:
        str: Letter grade
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def is_eligible_to_vote(age, citizenship):
    """
    Check voting eligibility using logical operators.
    
    Args:
        age (int): Person's age
        citizenship (bool): Is citizen?
        
    Returns:
        bool: True if eligible, False otherwise
    """
    return age >= 18 and citizenship


def can_access_content(age, has_permission):
    """Check if user can access restricted content."""
    return age >= 18 or has_permission


# ============== EXAMPLES ==============

print("=== AGE CATEGORY ===")
print(age_category(10))    # You're a kid!
print(age_category(16))    # You're a teenager!
print(age_category(25))    # You're an adult!

print("\n=== GRADE ASSIGNMENT ===")
scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = check_grades(score)
    print(f"Score: {score} → Grade: {grade}")

print("\n=== VOTING ELIGIBILITY ===")
print(f"Age 18, Citizen: {is_eligible_to_vote(18, True)}")
print(f"Age 17, Citizen: {is_eligible_to_vote(17, True)}")
print(f"Age 20, Not Citizen: {is_eligible_to_vote(20, False)}")

print("\n=== BOOLEAN LOGIC ===")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# ============== INTERACTIVE EXAMPLE ==============

if __name__ == "__main__":
    print("\n=== INTERACTIVE AGE CHECKER ===")
    try:
        user_age = int(input("Enter your age: "))
        print(age_category(user_age))
    except ValueError:
        print("❌ Please enter a valid number!")
