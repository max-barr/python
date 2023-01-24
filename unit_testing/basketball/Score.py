def field_goal(score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    score += 2
    return score

def free_throw(score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    score += 1
    return score

def three_pointer(score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    score += 3
    return score

