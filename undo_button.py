! /usr/bin/python
# undo_button.py

"""
this is problem in Python for Everyone problem 9.1.
add a button to the tally counter that allows an operator to undo an accidental button click. provide method
    def undo(self)
that simulates such a button. the button should not undo more often the user clicked it. I wrote the source for the undo button 
method,and added the method to the run_button. the rest of the code was provided by Python for Everyone.
"""
import sys

class Counter(object):
    
    def getValue(self) :
        return self._value

   def click(self) :
        """ increases the value by 1. """
        self._value = self._value + 1

    def undo_button(self) :
        """ this snippet creates a list of undo clicks, but ensure the length of undos does not exceed clicks. """"
        undo_clicks = [ ]
        self._value = self._value - 1
        undo_clicks.append(self._value)

        if len(undo_clicks) <= self._value :

             sea_monster = "Ok, you've used the undo button." 
             print sea_monster
        else :
            if len(undo_clicks) > self._value:
                tartagrade = "Sorry, you can't use the undo button again."
                print tartagrade
                sys.exit()       
 
    def reset(self) :
        """ this function resets the counters to 0. """
        self._value = 0
