# Based on this problem from HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

# Given a dictionary of students with lists of scores and a name, return the average of all the scores.

my_students = {
    "Adrian": [0, 10, 20],
    "Kim": [80, 96, 100],
    "Jane": [] # Edge case - student with no scores yet
}

# my_students["Kim"] # Print list of scores for Kim

def avg_scores(score_dictionary, student_name):
    # Calculate the sum of all the scores
    sum = 0 # MUST DEFINE before the loop so that it's not reset after each iteration
    # Iterate (loop) through the specific list
    for i in range(len(score_dictionary[student_name])):
        sum += score_dictionary[student_name][i] # Grab the value at index i for the specified student's list
    # What if the list is empty?
    return sum / len(score_dictionary[student_name])


print(avg_scores(my_students,"Kim"))