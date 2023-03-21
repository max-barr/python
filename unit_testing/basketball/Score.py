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

def technical_foul(score):
    print("You have earned a technical foul with that behavior")
    score = free_throw(score)
    return score

jump_ball("Portland Trail Blazers", "Los Angeles Lakers")
jump_ball("Milwaukee Bucks", "Phoenix Suns")

print(technical_foul(22))