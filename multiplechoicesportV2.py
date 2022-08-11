"""
Filename: multiplechoicesport.py
Author: Asher Turipa-Tapp
Date: 06/07/2022
Description: A multiple choice quiz about any sport that you choose whether it
is basketball, football or something else. You will also have the option to do
a mix of everything
"""

import random

BASKETBALL_QUESTIONS = ["Who has scored the most career NBA points?\
    1. Lebron James\
    2. Kareem Abdul-Jabbar\
    3. Karl Malone\
    4. Michael Jordan\
    ", "Who has the most all time 3 pointers made?\
    1. Ray Allen\
    2. James Harden\
    3. Damian Lillard\
    4. Stephen Curry\
    ", "Who is the tallest NBA player ever?\
    1. Manute Bol\
    2. Yao Ming\
    3. Lebron James\
    4. George Muresan\
    ", "Who has won the most NBA Finals?\
    1. Michael Jordan\
    2. Bill Russell\
    3. Wilt Chamberlain\
    4. Kareem Abdul-Jabbar\
    ", "Who won the 2022 NBA Finals?\
    1. Boston Celtics\
    2. Los Angeles Lakers\
    3. Brooklyn Nets\
    4. Golden State Warriors\
    ", "Which NBA player has the nickname Magic?\
    1. Lebron James\
    2. Kevin Johnson\
    3. Earvin Johnson\
    4. Larry Johnson\
    ", "What two national basketball teams have won the most basketball World Cups?\
    1. United States and Yugoslavia\
    2. United States and Australia\
    3. United States and Spain\
    4. Spain and Australia\
    ", "Who has scored the most points in one NBA game ever?\
    1. Lebron James\
    2. Stephen Curry\
    3. Quinndary Weatherspoon\
    4. Wilt Chamberlain\
    ", "Which two teams have both won the most NBA championships with 17 each?\
    1. Boston Celtics and The Golden State Warriors\
    2. Los Angeles Lakers and The Boston Celtics\
    3. Chicago Bulls and The Los Angeles Lakers\
    4. Los Angeles Clippers and The San Antonio Spurs\
    ", "How many teams are there in the NBA?\
    1. 36\
    2. 20\
    3. 40\
    4. 30\
    "]

FOOTBALL_QUESTIONS = ["Who won the first ever World Cup back in 1930?\
    1. Brazil\
    2. Argentina\
    3. Germany\
    4. Uruguay\
    ", "Which club has won the most champions league titles of all time?\
    1. Real Madrid\
    2. Barcelona\
    3. Manchester United\
    4. Liverpool\
    ", "Who has the most all time goals scored in the English Premier League?\
    1. Alan Shearer\
    2. Harry Kane\
    3. Sergio Aguero\
    4. Wayne Rooney\
    ", "Which team won the Euro in 1992 despite not properly qualifying?\
    1. Germany\
    2. Sweden\
    3. Finland\
    4. Denmark\
    ", "In recent FIFA games which team does Piemonte Calcio represent in real life?\
    1. Arsenal\
    2. Chelsea\
    3. Juventus\
    4. Inter Milan\
    ", "With 9 goals, who scored the most goals in a signle European Championship?\
    1. Michel Platini\
    2. Antoine Griezmann\
    3. Gareth Bale\
    4. Gerd Muller\
    ", "Which player scored the fastest hat-trick in the Premier League ever?\
    1. Mo Salah\
    2. Thierry Henry\
    3. Sadio Mane\
    4. Shane Long\
    ", "Which player has won the most ballon d'Or awards with 7 total?\
    1. Cristiano Ronaldo\
    2. Pele\
    3. Johan Cruyff\
    4. Lionel Messi\
    ", "Which international football team has won the most World Cup trophies?\
    1. Brazil\
    2. Argentina\
    3. Spain\
    4. Germany\
    ", "Which player performed a controversial move in the World Cup called the Hand of God\
    1. Luis Suarez\
    2. Mario Zagallo\
    3. Zinedine Zidane\
    4. Diego Maradona\
    "]

RUGBY_QUESTIONS = ["In international rugby, who is the all time highest points scorer?\
    1. Richie Mccaw\
    2. Dan Carter\
    3. Sonny Bill Williams\
    4. Owen Farrell\
    ", "Which playing kicked the winning penalty in the 2011 Rugby World Cup Final?\
    1. Beauden Barrett\
    2. Richie Mo'unga\
    3. Ardie Savea\
    4. Stephen Donald\
    ", "Which two teams have won the most Rugby World Cup Finals?\
    1. New Zealand and South Africa\
    2. New Zealand and Australia\
    3. England and France\
    4. Samoa and New Zealand\
    ", "Which player scored the most points in the 2015 World Cup?\
    1. Julian Savea\
    2. Agustin Creevy\
    3. Quade Cooper\
    4. Jonah Lomu\
    ", "Which player has the most Super Rugby appearances with 202 appearances?\
    1. Israel Folau\
    2. Dan Carter\
    3. TJ Perenara\
    4. Wyatt Crockett\
    ", "Which franchise holds the record for the most Super Rugby titles?\
    1. Crusaders\
    2. Hurricanes\
    3. Chiefs\
    4. Blues\
    ", "Which singular player has the most matches won at the Rugby World Cup?\
    1. Jerry Collins\
    2. Aaron Smith\
    3. Richie Mccaw\
    4. Christian Cullen\
    ", "What is the actual name of the Rugby World Cup?\
    1. Naismith Cup\
    2. Webb Ellis Cup\
    3. Super Cup\
    4. Lomu Cup\
    ", "When did the first Rugby World Cup happen?\
    1. 1991\
    2. 1999\
    3. 1984\
    4. 1987\
    ", "The New Zealand All Blacks famously beat Japan in 1995, what was the score?\
    1. 9-3\
    2. 100-0\
    3. 145-17\
    4. 127-45\
    "]






VALID_ANSWER = ["1","2","3","4","5"]
Score = 0
choice = 0

print("""Welcome to my quiz about sports, when you enter an answer remember that you should enter the number which correlates with the answer you believe is correct,
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

        question_one = input ("{}" .format(BASKETBALL_QUESTIONS[0]))
        if question_one == "2" :
            ""
            print("""Correct Kareem has a total of 38,387, Lebron is a close second
            """)
            Score = Score+1
            print("Your Score is", Score)
            

        else:
            print("""Good guess but unfortunately it is incorrect, the answer is actually Kareem Abdul-Jabbar
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 2.")

        question_two = input("{}".format(BASKETBALL_QUESTIONS[1]))
        if question_two == "4" :
            print("""That is correct, Stephen Curry has a total of 3117 3 pointers made while Ray Allen is in second with 2973 made
            """)
            Score = Score+1
            print("Your score is", Score)
            

        else:
            print("""Unfortunately that was incorrect, the correct answer would be Stephen Curry
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 3.")

        question_three = input ("{}".format(BASKETBALL_QUESTIONS[2]))
        if question_three == question_three == "1" or question_three == "4" :
            print("""Correct, both Manute Bol and George Muresan would be valid answers as they are both 7'7
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""That is incorrect, both Manute and George stand at 7'7
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 4.")

        question_four = input ("{}".format(BASKETBALL_QUESTIONS[3]))
        if question_four == "2" :
            print("""Correct, all of these players are iconic NBA finals players
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""Incorrect, Bill Russell has 11 rings, more then any other player
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 5.")

        question_five = input ("{}".format(BASKETBALL_QUESTIONS[4]))
        if question_five == "4" :
            print("""Correct, The Golden State Warriors beat the Boston Celtics in the finals
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""That answer is incorrect, the Golden State Warriors were the winners
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 6.")

        question_six = input ("{}".format(BASKETBALL_QUESTIONS[5]))
        if question_six == "3" :
            print("""That is correct, this was a trick as Earvin Johnson is more commonly referred to as Magic Johnson
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""That answer was incorrect, the correct answer is Earvin "Magic" Johnson
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 7.")
            

        question_seven = input ("{}".format(BASKETBALL_QUESTIONS[6]))
        if question_seven == "1" :
            print("""Both of these teams have the most with 5 World Cups won
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""Both the United States and Yugoslavia both have 5 titles
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 8.")

        question_eight = input ("{}".format(BASKETBALL_QUESTIONS[7]))
        if question_eight == "4" :
            print("""Wilt Chamberlain is the correct answer
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""All valid guesses however Wilt is the correct answer
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 9.")

        question_nine = input ("{}".format(BASKETBALL_QUESTIONS[8]))
        if question_nine == "2" :
            print("""Correct, the team with the 3rd amount of championships is the Warriors with 7
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""Unfortunately that is incorrect, the answer is the Los Angeles Lakers and the Boston Celtics
            """)
            Score = Score
            print("Your score is", Score)

        print("Question 10.")

        question_ten = input ("{}".format(BASKETBALL_QUESTIONS[9]))
        if question_ten == "4" :
            print("""Correct, when the NBA first was created there were only 11 teams
            """)
            Score = Score+1
            print("Your score is", Score)

        else:
            print("""Unfortunately that is incorrect, the answer is 30
            """)
            Score = Score
            print("Your score is", Score)


    if choice == "2":
        print("Question 1.")

    
    

        

            
            
    if choice == "5":
        print("Goodbye")
            
            
            



            

            

        

        





