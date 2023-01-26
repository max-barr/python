import random

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

def jump_ball(team_1, team_2):
    if random.randint(1,2) == 1:
        print("The {} won the ball".format(team_1))
    else:
        print("The {} won the ball".format(team_2))

jump_ball("Portland Trail Blazers", "Los Angeles Lakers")