#! python3

import random, os

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
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

#Create folder filesQuiz to store files
if not os.path.isdir('filesQuiz'):
	os.makedirs('filesQuiz')
else: 
	print('\nya existe el folder de los archivos\n')


for quizNum in range(35):
	# TODO: Create the quiz and answer key files.
	
	quizFile = open('filesQuiz\\capitalsquiz%s.txt' % (quizNum +1), 'w')
	answerKeyFile = open('filesQuiz\\capitalsquiz_answers%s.txt'% (quizNum +1) , 'w')

	# TODO: Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'state capitals quiz (Form %s)' %(quizNum+1))
	quizFile.write('\n\n')

	# TODO: Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)

	# TODO: Loop through all 50 states, making a question for each.
	for questionNum in range(50):
		# Get right and wrong answers.
		correctAnswser = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswser)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswser]
		random.shuffle(answerOptions)
		
		# TODO: Write the question and answer options to the quiz file.
		quizFile.write('%s. what is the capital of %s?\n' % (questionNum +1,states[questionNum]))
		for x in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[x], answerOptions[x]))
		quizFile.write('\n')

        # TODO: Write the answer key to a file.
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswser)]))

	quizFile.close()
	answerKeyFile.close()