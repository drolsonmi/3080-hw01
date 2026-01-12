# Homework 1 - Basic Python Skills - MATH 3080
In this assignment, you will apply your basic python skills to solve three problems. In your GitHub Classroom repository, you will find three files called `problem_1.py`, `problem_2.py`, and `problem_3.py`. Complete the code for these problems using python.

The files `test_1.py`, `test_2.py`, and `test_3.py` will generate output from your three functions and will be used to grade your homework. When creating your programs, please do the following:
* Test your data to make sure the output comes out exactly as requested
* Use functions to allow different input
* Use formatted strings so the output values match the input given

When completed, push your repository to GitHub. GitHub Classroom will then use the test files to see if your python files solve the given problems correctly.

## Problem 1 - Tip Calculator
You are dining at the "Budget Bistro." Your program should:
1. Ask the user for the original cost of the meal.
2. Ask the user for the tip percentage they wish to leave (e.g., 15).
3. Calculate the tip amount and the total bill.
4. Print a summary of the costs.

Required Input
* Meal Cost: A float (e.g., 25.50)
* Tip Percentage: An integer (e.g., 18)

Example Output
<pre>Enter the cost of the meal: 25.50
Enter the tip percentage: 18

--- Receipt ---
Original Meal: $25.50
Tip Amount: $4.59
Total Bill: $30.09</pre>

## Problem 2 - Greenhouse Monitors
Write a program that monitors temperature readings for a greenhouse and alerts the user if any readings are "Critical."

The greenhouse sensors take 4 temperature readings (in Celsius). Your program should:
1. Ask the user to enter 4 temperature readings.
2. For each reading:
    * If the temperature is above 30°C, print: "WARNING: Critical Heat!"
    * If the temperature is below 10°C, print: "WARNING: Critical Cold!"
    * Otherwise, print: "Temperature Stable."
3. After the loop finishes, calculate and print the average temperature of all 4 readings.

Required Input
* Temperatures: Four float values (e.g., 32.5, 20.0, 8.0, 25.0).

Example Output
<pre>Reading 1: 32.5
WARNING: Critical Heat!
Reading 2: 20.0
Temperature Stable.
Reading 3: 8.0
WARNING: Critical Cold!
Reading 4: 25.0
Temperature Stable.

--- Report ---
Average Temperature: 21.375°C</pre>

## Problem 3 - The Hashtag & Keyword Tracker
Write a program that analyzes a "social media post" (a string) and counts the occurrences of specific interest tags to determine the post's category.

A marketing firm needs to categorize posts based on keywords. Your program should:
1. Define a dictionary called tracker with three keys: "tech", "health", and "travel". Initialize their values to 0.
2. Ask the user to input a sentence (the post).
3. Clean the data: Convert the entire sentence to lowercase.
4. Split the sentence into a list of individual words.
5. Use a for loop to check every word in that list:
    * If the word is "coding" or "python", increment the "tech" value in your dictionary.
    * If the word is "gym" or "fruit", increment the "health" value.
    * If the word is "ocean" or "flight", increment the "travel" value.
6. Print the final dictionary to show the interest scores.

Required Input
* The Post: A string (e.g., "I love coding in Python and eating fruit at the gym")

Example Output
<pre>Enter your post: I love coding in Python and eating fruit at the gym

--- Post Analysis ---
{'tech': 2, 'health': 2, 'travel': 0}</pre>
