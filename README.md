[![Python 3.9](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/)
# tedquizconsole
A simple command line function for ted's quizzes

## How to compile
run quizconsole.py

## Txt files
questions are deffined within .txt files as such
```
question = {
    id = INTEGER
    text = STRING
    answer = STRING
    incorrect = LIST OF STRINGS
    category = LIST OF STRINGS
}
```
each question must have a unique id
text is the question itself
answer is the correct answer to the question
incorrect is a list of all the incorrect options
category is a list of all the categories this question belongs to

look at the example.txt file for example questions

## savedata.csv file
stores all the save data across all sessions the format is:
```
ID;NUMASKED;NUMCORRECT
```
you do not need to touch this file

## Make Sure to Delete the example files before use