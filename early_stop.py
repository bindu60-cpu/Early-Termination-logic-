def check_termination(scores):
    if len(scores) >= 3 and sum(scores)/len(scores) < 3:
        return "Terminate"
    return "Continue"

# Example
scores = [2, 1, 2]
print(check_termination(scores))