import random
options = ["rock", "paper", "scissors"]
playwish = 0

playwish_str = input("Type PLAY to start: ").upper()
if playwish_str == "PLAY":
    playwish = 1

while playwish == 1:
    user_score = 0
    comp_score = 0

    for roundnum in range(1,4):
        print(f"\n---Round{roundnum}---")

        user = input("Choose rock, paper, or scissors: ").lower()
        
        computer = random.choice(options)
        
        #denoting by number
        try:
            usernum = options.index(user)
        except:
            print("Invalid Input, Please try again")
            continue
        compnum = options.index(computer)
        
        print(f"Computer chose: {computer}")
        
        #checking who won
        determinant = (usernum - compnum)%3
        if determinant == 0:
            print("It's a Tie")
        elif determinant == 1:
            print("You Win")
            user_score += 1
        else:
            print("Computer Wins")
            comp_score += 1

    print("---Final Results---")
    print(f"\nYour Score = {user_score} \nComputerScore = {comp_score}\n")

    if user_score > comp_score:
        print("You win")
    elif user_score == comp_score:
        print("It's a Tie")
    else:
        print("Computer wins")
    
    playwish = 0
    replaywish_str = input("Type PLAY to play again").upper()

    if replaywish_str == "PLAY":
        playwish = 1


