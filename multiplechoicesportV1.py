"""
Filename: multiplechoicesport.py
Author: Asher Turipa-Tapp
Date: 06/07/2022
Description: A multiple choice quiz about any sport that you choose whether it
is basketball, football or something else. You will also have the option to do
a mix of everything
"""

VALID_ANSWER = ["1","2","3","4","5"]
Score = 0
choice = 0

print("""Welcome to my quiz about sports, when you enter an answer remember that it should be in CAPS
or simply just type the number which correlates with the answer you believe is correct,
please choose what sport you'd like to be quizzed on (enter the number, not the sport!!!)
1. Basketball
2. Football
3. Rugby
4. American Football
5. Exit""")

while not choice in VALID_ANSWER:
    choice = input("Please select a valid option")

if choice == "1":
    print("Question 1.")

    question_one = input ("""Who has scored the most career NBA points?
    1. LEBRON JAMES
    2. KAREEM ABDUL-JABBAR
    3. KARL MALONE
    4. MICHAEL JORDAN
    """)
    if question_one == "KAREEM ABDUL-JABBAR" or question_one == "2" :
        print("""Correct Kareem has a total of 38,387, Lebron is a close second
        """)
        Score = Score+1
        print("Your Score is", Score)
        

    else:
        print("""Good guess but unfortunately it is incorrect, the answer is actually Kareem Abdul-Jabbar
        """)
        Score = Score
        print("Your score is", Score)

    question_two = input ("""Who has the most all time 3 pointers made?
    1. RAY ALLEN
    2. JAMES HARDEN
    3. DAMIAN LILLARD
    4. STEPHEN CURRY
    """)
    if question_two == "STEPHEN CURRY" or question_two == "4" :
        print("""That is correct, Stephen Curry has a total of 3117 3 pointers made while Ray Allen is in second with 2973 made
        """)
        Score = Score+1
        print("Your score is", Score)
        

    else:
        print("""Unfortunately that was incorrect, the correct answer would be Stephen Curry
        """)
        Score = Score
        print("Your score is", Score)

    question_three = input ("""Which NBA player is the tallest to ever play at 7 feet and 7 inches?
    1. MANUTE BOL
    2. YAO MING
    3. SHAQUILLE O'NEAL
    4. GEORGE MURESAN
    """)
    if question_three == "MANUTE BOL" or question_three == "GEORGE MURESAN" or question_three == "1" or question_three == "4" :
        print("""Correct, both Manute Bol and George Muresan would be valid answers as they are both 7'7
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""That is incorrect, both Manute and George stand at 7'7
        """)
        Score = Score
        print("Your score is", Score)

    question_four = input ("""Which NBA player has the most NBA finals rings?
    1. LEBRON JAMES
    2. BILL RUSSELL
    3. MICHAEL JORDAN
    4. KOBE BRYANT
    """)
    if question_four == "BILL RUSSELL" or question_four == "2" :
        print("""Correct, all of these players are iconic NBA finals players
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""Incorrect, Bill Russell has 11 rings, more then any other player
        """)
        Score = Score
        print("Your score is", Score)

    question_five = input ("""Which NBA team won the 2022 NBA Finals?
    1. LOS ANGELES LAKERS
    2. MILWAUKEE BUCKS
    3. BOSTON CELTICS
    4. GOLDEN STATE WARRIORS
    """)
    if question_five == "GOLDEN STATE WARRIORS" or question_five == "4" :
        print("""Correct, The Golden State Warriors beat the Boston Celtics in the finals
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""That answer is incorrect, the Golden State Warriors were the winners
        """)
        Score = Score
        print("Your score is", Score)

    question_six = input ("""Which NBA player has the nickname "Magic"?
    1. KEVIN JOHNSON
    2. JOHN STOCKTON
    3. EARVIN JOHNSON
    4. LEBRON JAMES
    """)
    if question_six == "EARVIN JOHNSON" or question_six == "3" :
        print("""That is correct, this was a trick as Earvin Johnson is more commonly referred to as Magic Johnson
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""That answer was incorrect, the correct answer is Earvin "Magic" Johnson
        """)
        Score = Score
        print("Your score is", Score)
        

    question_seven = input ("""What two national basketball teams have won the most basketball World Cups?
    1. UNITED STATES AND YUGOSLAVIA
    2. UNITED STATES AND AUSTRALIA
    3. UNITED STATES AND SPAIN
    4. SPAIN AND AUSTRALIA
    """)
    if question_seven == "UNITED STATES AND YUGOSLAVIA" or question_seven == "1" :
        print("""Both of these teams have the most with 5 World Cups won
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""Both the United States and Yugoslavia both have 5 titles
        """)
        Score = Score
        print("Your score is", Score)

    question_eight = input ("""Who has scored the most points in one NBA game ever?
    1. LEBRON JAMES
    2. STEPHEN CURRY
    3. QUINNDARY WEATHERSPOON
    4. WILT CHAMBERLAIN
    """)
    if question_eight == "WILT CHAMBERLAIN" or question_eight == "4" :
        print("""Wilt Chamberlain is the correct answer
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""All valid guesses however Wilt is the correct answer
        """)
        Score = Score
        print("Your score is", Score)

    question_nine = input ("""Which two teams have both won the most NBA championships with 17 each?
    1. BOSTON CELTICS AND THE GOLDEN STATE WARRIORS
    2. LOS ANGELES LAKERS AND THE BOSTON CELTICS
    3. CHICAGO BULLS AND THE LOS ANGELES LAKERS
    4. LOS ANGELES CLIPPERS AND BOSTON CELTICS
    """)
    if question_nine == "LOS ANGELES LAKERS AND THE BOSTON CELTICS" or question_nine == "2" :
        print("""Correct, the team with the 3rd amount of championships is the Warriors with 7
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""Unfortunately that is incorrect, the answer is the Los Angeles Lakers and the Boston Celtics
        """)
        Score = Score
        print("Your score is", Score)

    question_ten = input ("""How many teams are there in the NBA?
    1. 36
    2. 20
    3. 40
    4. 30
    """)
    if question_ten == "30" or question_ten == "4" :
        print("""Correct, when the NBA first was created there were only 11 teams
        """)
        Score = Score+1
        print("Your score is", Score)

    else:
        print("""Unfortunately that is incorrect, the answer is 30
        """)
        Score = Score
        print("Your score is", Score)
        
        
        



        

        

    

    




