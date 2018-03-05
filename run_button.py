#! /usr/bin/python
# run_button.py

""" this is to run the undo_button function, and show that undo_button works. """
from undo_button import Counter

""" run the functions from undo_button """
tally = Counter()
tally.reset()

tally.click()
tally.click()

tally.undo_button()

result = tally.getValue()
print "Result: " + str(result)


