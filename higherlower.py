import random, os
from game_data import data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
    country_name = account['name']
    rank = account['Rank']
    return f"country name: {country_name}"# and Rank is {rank}"

def compare_answer(a,b):
        print(f"a: {a}")
        print(f"b: {b}")
        if a['Rank'] > b['Rank']:
            correct = 'B'
            return b,correct
        elif a['Rank'] < b['Rank']:
            correct = 'A'
            return a,correct
        else:
            print("Invalid input. ")

#Shuffle the data
random.shuffle(data)

#Length of the items
length = len(data)
print(length)

#Randomly pick two items
country_a = random.choice(data)
country_b = random.choice(data)

#If country a and country are same then execute if statement
if country_a == country_b:
    country_b = random.choice(data)

#print the countries data in a formated way

print(f"Compare the country A {format_data(country_a)}.")
print("*****V/S*****")
print(f"Compare the country B {format_data(country_b)}.")

#input 'A' or 'B'
answer = input("Enter the country which has highest rank, A or B ").upper()
#compare the values and return the data correct data and correct answer "A" or "B"
compare,compare_value = compare_answer(country_a,country_b)

#set the score value and i value to zero
score = 0
i = 0
while i < length:

    if compare_value == answer:
        score += 1
        clear_screen() # this will clear the terminal
        print(f"\033[1m ✅ Correct! {compare['name']} has the higher rank.\033[0m")
        print(f"Your current score is {score}\n")
        if answer == 'B':
            print(f"Compare the country A {format_data(country_a)}.")
            print("*****V/S*****")
            country_b = random.choice(data)
            while country_b == country_a:
                country_b = random.choice(data)
            print(f"Compare the country B {format_data(country_b)}.")
            answer = input("Enter the country which has highest rank, A or B ").upper()
            
            #score += 1
        elif answer == 'A':
            country_a = random.choice(data)
            while country_a == country_b:
                country_a = random.choice(data)
            print(f"Compare the country A {format_data(country_a)}.")
            print("*****V/S*****")
            print(f"Compare the country B {format_data(country_b)}.")
            answer = input("Enter the country which has highest rank, A or B ").upper()
            #score += 1
                
        compare,compare_value = compare_answer(country_a,country_b)
        
        i += 1
        
    else:
        print("❌ Incorrect!")
        break

print(f"Your total score is {score}")