import random

questions = []

while True:
    question = input('vous > ')
    questions.append(question)
    print('moi > ', random.choice(questions))
