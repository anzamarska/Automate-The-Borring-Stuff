#! python3

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}





# Creates 35 different quizzes.

for numb in range (35):
    quizFile= open ("quiz%s.txt" % (numb +1), "w")
    answerFile= open ("anser_quiz%s.txt" % (numb +1), "w")

    quizFile.write("Name: \n\nDate: \n\nPeriod:\n\n")
    quizFile.write((" " * 20) + "State Capitals Quiz (Form %s) \n\n" % (numb + 1))

    states = list(capitals.keys())
    random.shuffle(states)
    

# Creates 50 multiple-choice questions for each quiz, in random order.
for questionNum in range(50):
    correctAnswer= capitals[states[questionNum]]
    wrongAnswers=list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers=random.sample(wrongAnswers, 3 )
    answerOptions= wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

# Provides the correct answer and three random wrong answers for each question, in random order.
for questionNum in range (50):
    quizFile.write("%s. What is the capital of %s?\n " %(questionNum + 1, states[questionNum]))
    for i in range(4):
        quizFile.write("%s. %s\n" % ("ABCD"[i], answerOptions[i]))

    answerFile.write("%s. %s\n" % (questionNum +1, "ABCD"[answerOptions.index(correctAnswer)]))
                   
quizFile.close()
answerFile.close()

# Writes the quizzes to 35 text files.

# Writes the answer keys to 35 text files.
