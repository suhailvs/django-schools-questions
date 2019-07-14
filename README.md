# django-schools-questions

## Usage 

Copy `sampledata` folder to project folder
::

    $ ./manage.py shell
    >>> from sampledata import import_questions
    >>> import_questions.sync()