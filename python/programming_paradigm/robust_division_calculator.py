def safe_divide(numerator, denominator):
    try:
        # Attempt to convert the arguments to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt to perform the division
        result = num / denom

        # Return the result if successful
        return f"The result of the division is {result:.1f}"

    except ZeroDivisionError:
        # Handle division by zero error
        return "Error: Cannot divide by zero."

    except ValueError:
        # Handle non-numeric input error
        return "Error: Please enter numeric values only."
