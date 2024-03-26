import random

rps= ['Rock', 'Paper', 'Scissor']

userName= input("Player please enter your name: ").capitalize()


while True:
    userScore=0
    botScore=0
    startQ= int(input(f"""
    {userName} IF YOU WANNA START THE GAME PRESS : 1
    IF YOU WANT TO KNOW THE RULES PRESS : 2
    IF YOU WANT TO EXIT PRESS : 3
    """))

    if startQ == 1:

        for game in range(1,6):
            userInput= int(input(f"""
            {userName}
            for 'ROCK' press : 1
            for 'PAPER' press : 2
            for 'SCISSOR' press : 3
                    """))
        
            if userInput==1:
                userChoice= "Rock"
            elif userInput==2:
                userChoice= "Paper"
            elif userInput==3:
                userChoice= "Scissor"

            botChoice= random.choice(rps)

            if userChoice==botChoice:
                print('GAME DRAW')
                print()
                print(f'{userName} : {userChoice}')
                print(f"Bot : {botChoice}")
                userScore+=1
                botScore+=1
            elif (userChoice== "Paper" and botChoice== "Rock" or userChoice== 'Rock' and botChoice=="Scissor" or userChoice=='Scissor' and botChoice== "Paper"):
                print(f"{userName} HAS WON THE ROUND.")
                print()
                print(f'{userName} : {userChoice}')
                print(f"Bot : {botChoice}")
                userScore+=1
            else:
                print('Bot HAS WON THE ROUND.')
                print()
                print(f'{userName} : {userChoice}')
                print(f"Bot : {botChoice}")
                botScore+=1
        
        if userScore < botScore:
            print()
            print('BOT HAS WON THE MATCH.')
            print()
            print(f'{userName} : {userScore}')
            print(f"Bot : {botScore}")
        elif userScore > botScore:
            print()
            print(F'{userName} HAS WON THE MATCH.')
            print()
            print(f'{userName} : {userScore}')
            print(f"Bot : {botScore}")
        else:
            print()
            print('MATCH DRAW')
            print()
            print(f'{userName} : {userScore}')
            print(f"Bot : {botScore}")
    elif startQ==2:
        print("""
            Rock crushes scissors (win).
            Scissors cut paper (win).
            Paper covers rock (win).
            If both players throw the same sign, it's a tie.
            """)
    else:
        break
