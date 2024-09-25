def divide_num(d, e):
    try:
        result = d / e
    except ZeroDivisionError:
        return "Error: Division by Zero not allowed."
    else:
        return result
    finally:
        print("Execution Complete.")


# Call the function
print(divide_num(10, 2))
