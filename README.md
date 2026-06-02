def check_termination(scores):
    if len(scores) >= 3 and sum(scores)/len(scores) < 3:
        return "Terminate"
    return "Continue"

# Example
scores = [2, 1, 2]
print(check_termination(scores))# Early-Termination-logic-
"Added early termination functionality that exits the program/task as soon as the required result is achieved, optimizing performance and execution time."
