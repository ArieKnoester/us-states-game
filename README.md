# us-states-game

This was written as part of a Python course as an exercise
in using Pandas. The .csv and image files were provided by the 
course. A map of the United States will display. The user tries
to fill in all 50 State's names. If the player quits before 
guessing all 50 (clicks the 'Cancel' button), write the missing 
state names to a .csv file.

### Updated user feedback
Writing the missing state names to a .csv file was a requirement
for this exercise. While I understand this was intended as 
practice, I think this is poor UX. So I added a method to the
TextDisplay class to show the missing state names on the map in
red.