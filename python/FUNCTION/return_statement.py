def analyze_number(num: int) -> str:
    """
    Analyze a number and describe whether it is positive, negative, or zero.

    This function demonstrates how the `return` statement works in Python:
    - It immediately sends back a result and stops further execution of the function.

    Args:
        num (int): The number to analyze.

    Returns:
        str: A message indicating whether the number is positive, negative, or zero.
    """

    if num == 0:
        return "Number is zero (stopped early)"

    if num > 0:
        result = f"{num} is positive"
    else:
        result = f"{num} is negative"

    return result


print(analyze_number(5))   # "5 is positive"
print(analyze_number(-3))  # "-3 is negative"
print(analyze_number(0))   # "Number is zero (stopped early)"
