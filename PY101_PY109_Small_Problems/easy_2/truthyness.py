# Implement a program to evaluate the truthiness of a list of inputs (e.g., 0, None, [], etc.)

# Function that evaluates the value as truthy or falsy
def truthy_eval(value):
    return bool(value)

def evaluate_list_truthiness(input_list):
    return [truthy_eval(item) for item in input_list]

# Example usage
inputs = [0, None, [], {}, "", 1, "text", [1], True, False]
results = evaluate_list_truthiness(inputs)
print(results)