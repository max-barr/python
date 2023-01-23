def touchdown(score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    score += 7
    return score

def two_point_conversion(score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    score += 8
    return score

def field_goal(score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    score += 3
    return score

def safety(score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    score += 2
    return score

