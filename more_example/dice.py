import random
score = 0
rolls = []
print("welcome player")
print("to win this, you need to reach minimum of 50")

while score < 50:
    input("press enter to roll")
    die = random.randint(1, 6)
    score += die
    rolls.append(die)
    
    print(f"you rolled the number {die}")
    print(f"your total score is {score}")

print("congratulations you won the game")
print(f"your total score is {score}")
print(f"this is your roll history {rolls}")
