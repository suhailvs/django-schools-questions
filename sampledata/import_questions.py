"""
Usage 
./manage.py shell
>>> from sampledata import import_questions
>>> import_questions.sync('30-1-10')
"""

from classroom.models import Quiz, Question, Answer
import os

def sync(book):
    quiz, created = Quiz.objects.get_or_create(owner_id = 2, name='PSC {0}'.format(book), subject_id=5)
    # created = True
    if not created:
        return 'quiz already exist'

    filename = os.path.join('sampledata', '{0}.txt'.format(book))
    fp = open(filename,'r')
    for line in fp.readlines():
        items = line.split(',')

        question = Question.objects.create(quiz = quiz, text = items[0])    
        for i,ans in enumerate(items[1:-1]):
            correct = int(items[-1]) == (i+1)
            answer = Answer.objects.create(question = question, text = ans.strip(), is_correct=correct)
            print (answer)
