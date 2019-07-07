"""
Usage 
./manage.py shell
>>> from sampledata import import_questions
>>> import_questions.sync('LD_Clerk','01-01-98')
"""

from classroom.models import Quiz, Question, Answer, Subject
import os

def sync(subject, exam_date):
    item, _ = Subject.objects.get_or_create(name = subject.replace('_',' '))
    quiz, created = Quiz.objects.get_or_create(owner_id = 2, name=exam_date, subject=item)
    if not created:
        return 'quiz already exist'

    filename = os.path.join('sampledata', subject, '{0}.txt'.format(exam_date))
    fp = open(filename,'r')
    for line in fp.readlines():
        items = line.split(',')

        question = Question.objects.create(quiz = quiz, text = items[0])    
        for i,ans in enumerate(items[1:-1]):
            correct = int(items[-1]) == (i+1)
            answer = Answer.objects.create(question = question, text = ans.strip(), is_correct=correct)
            print (answer)
