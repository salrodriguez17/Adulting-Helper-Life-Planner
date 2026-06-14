"""
Adulting Helper: A Beginner Python Life Planner
Salvador Rodriguez


Project Description
Adulting Helper is a beginner-friendly Python life planning program designed to
help people make better everyday decisions about money, time, goals, wellness, and weekend
planning.

The user answers simple questions about income, expenses, work or study hours, sleep,
 phone use, stress, energy, and personal goals. The program then gives helpful feedback
 and creates a simple life plan with practical advice.

This project uses beginner Python concepts such as print(), input(), variables, lists,
 dictionaries, loops, if-statements, functions, and the random library. The goal of the
  project is to show how basic programming can be used to build a useful and compassionate
   tool that helps people improve their daily lives one small step at a time.
   
Purpose:
Help people make better everyday decisions about
money, time, goals, and wellness.

Beginner concepts used:
- print()
- input()
- variables
- lists
- dictionaries
- loops
- if-statements
- functions
- random choice
"""

import random


# -----------------------------
# Motivational messages
# -----------------------------

motivational_quotes = [
    "Small steps still move you forward.",
    "You do not need to fix your whole life today. Start with one choice.",
    "Discipline is choosing what you want most over what you want now.",
    "Progress is better than perfection.",
    "Your future self is built by your daily habits."
]


# -----------------------------
# Function: show welcome message
# -----------------------------

def welcome():
    print("====================================")
    print("     Adulting Helper Life Planner")
    print("====================================")
    print("This program helps you think about:")
    print("- Money")
    print("- Time")
    print("- Goals")
    print("- Wellness")
    print()
    print("Answer a few questions and get a simple life plan.")
    print()


# -----------------------------
# Function: money helper
# -----------------------------

def money_helper():
    print("\n--- Money Check-In ---")

    income = float(input("Enter your monthly income after taxes: $"))
    rent = float(input("Enter your monthly rent or housing cost: $"))
    food = float(input("Enter your monthly food cost: $"))
    transportation = float(input("Enter your monthly transportation cost: $"))
    fun = float(input("Enter your monthly fun/entertainment spending: $"))

    total_expenses = rent + food + transportation + fun
    money_left = income - total_expenses

    print("\nMoney Summary:")
    print("Total expenses: $", round(total_expenses, 2))
    print("Money left after expenses: $", round(money_left, 2))

    if money_left > 500:
        print("Great job! You have room to save or invest.")
    elif money_left > 0:
        print("You are staying positive, but your budget may be tight.")
    else:
        print("Warning: You are spending more than you earn.")

    if rent > income * 0.35:
        print("Housing warning: Your rent is more than 35% of your income.")
        print("Consider roommates, cheaper housing, or reducing other expenses.")

    return money_left


# -----------------------------
# Function: time helper
# -----------------------------

def time_helper():
    print("\n--- Time Check-In ---")

    work_hours = float(input("How many hours do you work or study each day? "))
    sleep_hours = float(input("How many hours do you sleep each night? "))
    phone_hours = float(input("How many hours do you spend on your phone/social media each day? "))

    total_used = work_hours + sleep_hours + phone_hours
    free_time = 24 - total_used

    print("\nTime Summary:")
    print("Hours already used:", total_used)
    print("Estimated free hours:", free_time)

    if free_time >= 4:
        print("You have good free time available. Use some of it for your goals.")
    elif free_time >= 2:
        print("You have some free time, but you need to use it carefully.")
    else:
        print("Your schedule is very full. Try to protect your rest and focus.")

    if phone_hours > 3:
        print("Phone warning: You may be spending too much time on your phone.")

    return free_time


# -----------------------------
# Function: goals helper
# -----------------------------

def goals_helper():
    print("\n--- Goal Planner ---")

    goals = []

    number_of_goals = int(input("How many goals do you want to enter? "))

    for i in range(number_of_goals):
        goal = input("Enter goal #" + str(i + 1) + ": ")
        goals.append(goal)

    print("\nYour Goals:")
    for goal in goals:
        print("- " + goal)

    print("\nChoose your top priority goal.")
    priority_goal = input("Type your most important goal: ")

    print("\nSimple Action Plan:")
    print("Goal:", priority_goal)
    print("Step 1: Spend 15 minutes this week working on it.")
    print("Step 2: Write down one obstacle.")
    print("Step 3: Ask one person for advice or support.")

    return goals


# -----------------------------
# Function: wellness helper
# -----------------------------

def wellness_helper():
    print("\n--- Wellness Check-In ---")

    stress = int(input("Rate your stress from 1 to 10: "))
    energy = int(input("Rate your energy from 1 to 10: "))
    sleep_quality = int(input("Rate your sleep quality from 1 to 10: "))

    wellness_score = stress + (10 - energy) + (10 - sleep_quality)

    print("\nWellness Summary:")

    if wellness_score <= 8:
        print("You seem to be doing okay today.")
        suggestion = "Keep your routine steady and protect your sleep."
    elif wellness_score <= 16:
        print("You may need a reset today.")
        suggestion = "Take a walk, drink water, and write down your top 3 tasks."
    else:
        print("You may be overwhelmed today.")
        suggestion = "Slow down. Pick only one important task and take a break."

    print("Suggestion:", suggestion)

    return wellness_score


# -----------------------------
# Function: weekend idea generator
# -----------------------------

def weekend_plan_generator():
    print("\n--- Weekend Plan Generator ---")

    budget = input("Choose your budget: free, low, or medium: ").lower()
    mood = input("Choose your mood: chill, social, productive, or adventurous: ").lower()

    plans = {
        "free": [
            "Go for a walk, clean your room, and call a friend.",
            "Visit a park, journal, and watch a movie at home.",
            "Do a home workout, organize your week, and relax."
        ],
        "low": [
            "Get coffee, visit a bookstore, and meal prep.",
            "Go to a local museum, try a new recipe, and plan your week.",
            "Have a picnic, take photos, and work on one personal goal."
        ],
        "medium": [
            "Go out to eat, see a movie, and plan your next goal.",
            "Take a day trip, try a new activity, and reflect on your week.",
            "Go to brunch, buy one useful item, and prep for Monday."
        ]
    }

    if budget in plans:
        selected_plan = random.choice(plans[budget])
    else:
        selected_plan = "Try a simple reset weekend: walk, clean, rest, and plan."

    print("\nYour Weekend Plan:")
    print(selected_plan)

    if mood == "productive":
        print("Extra tip: Complete one task before relaxing.")
    elif mood == "social":
        print("Extra tip: Text one friend and make a simple plan.")
    elif mood == "chill":
        print("Extra tip: Protect your rest and avoid overbooking yourself.")
    elif mood == "adventurous":
        print("Extra tip: Try one new place or activity.")


# -----------------------------
# Function: create final life plan
# -----------------------------

def final_life_plan(money_left, free_time, wellness_score):
    print("\n====================================")
    print("          Your Life Plan")
    print("====================================")

    print("\nMoney:")
    if money_left > 500:
        print("- Save some money this month.")
    elif money_left > 0:
        print("- Track your spending carefully.")
    else:
        print("- Reduce one expense this week.")

    print("\nTime:")
    if free_time >= 4:
        print("- Use one hour for a personal goal.")
    elif free_time >= 2:
        print("- Use 30 minutes for your most important task.")
    else:
        print("- Focus on rest and one small task.")

    print("\nWellness:")
    if wellness_score <= 8:
        print("- Keep your habits steady.")
    elif wellness_score <= 16:
        print("- Take a short reset break today.")
    else:
        print("- Be kind to yourself and simplify your day.")

    print("\nMotivation:")
    print(random.choice(motivational_quotes))


# -----------------------------
# Main program
# -----------------------------

def main():
    welcome()

    money_left = money_helper()
    free_time = time_helper()
    goals_helper()
    wellness_score = wellness_helper()
    weekend_plan_generator()
    final_life_plan(money_left, free_time, wellness_score)

    print("\nThank you for using Adulting Helper!")
    print("Remember: one small improvement each day adds up.")


# This starts the program
main()