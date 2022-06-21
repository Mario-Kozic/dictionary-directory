# dictionary-directory
 A dictionary type of program that will return a description of the word we gave it.

 We downloaded json file with our test data.

# Create python script 
    - use command 'touch app.py' in terminal

# In app.py we are gonna:
    - import json
then:
    - we are gonna import  get_close_matches from difflib module
then:
   - we are gonna declare variable data and give it a value json.load(open("data.json")) which is gonna  accepts file object, parses the JSON data, populates a Python dictionary with the data and returns it back to you.

# Now lets make 2 variables
    - one that is gonna prompt user for an input 
    - one that is gonna pass users word thru our funcion that will define the given word

# Time to program our function 
    - we are gonna use conditional statements to check if the word is in our data.json file
    - we are also condition  our functiion in case of user error to look for the closest possibuility in our data set and offer it to the user
    

# Print the output 


# module we are gonna work with  
  difflib ---> module provides classes and functions for comparing sequences. It can be used for example, for comparing files, and can produce information about file differences in various formats, including HTML and context and unified diffs. For comparing directories and files, see also, the filecmp module.

  get_close_matches  ---> which will return a list of the best “good enough” matches. word is a sequence for which close matches are desired (typically a string), and possibilities is a list of sequences against which to match word (typically a list of strings) 
