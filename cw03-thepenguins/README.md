[![Build Status](https://travis-ci.com/chapman-phys220-2018f/cw03-thepenguins.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/cw03-thepenguins)

# PHYS220/MATH220/CPSC220 CW 3

**Author(s):** Jack Savage, Enea Dodi,Gwyneth Casey

## Specification

Complete the following exercises, saving your solutions in the indicated files. For Python files that include test functions, GitHub will automatically run your tests with ```nosetests3``` on every commit, indicating any failures via the Travis framework in the build status image above.

1. Have one person in your group go to [Travis-CI.com](https://travis-ci.com) and log in with a GitHub account. On the left column, click on the "+" icon to find a list of your Organizations, and click on "Sync Account". Refresh the page after it is synced properly, then click on the class organization. You should see a list of all class repositories on the right that are could be automatically tested by Travis. We are going to use Travis from now on to make sure that your code works properly. Every time you commit to GitHub, it will "trigger" a Travis "build" of your code, which will automatically run it against all specified tests to ensure that it works properly. The first change you need to make on each README file from now on will be to update the icon at the top of the README. To do this, find the repository within Travis, click on it, then click on the "build" icon next to its name. A popup should appear; change "Image URL" to "Markdown" in the pulldown menu, copy the Markdown code, and paste it in the README file above. After saving, you should see the icon change to either red or green once the build completes automatically, which will tell you whether the tests have failed or succeeded.  Remember to also add your names at the top, and sign your names at the bottom.  Later on remember to fill out your assessment properly.
1. With your group, review the [IPython/Jupyter Slides](https://slides.com/profdressel/jupyter-overview) together and discuss. Try sample code in an ipython session in a terminal with your group. Note that these slides are a crash course in basic interactive python that we will use throughout the semester, so do not fret if you do not absorb it all at once. It will complement Chapters 2--5 of your textbook nicely. The rest of the assignment this week will give you a challenge to test your python-fu, so a recommended strategy is to try the rest of the assignment while referencing the slides as needed.
1. Create a python file ```sequences.py``` with a function ```fibonacci(n)``` that returns the first ```n``` Fibonacci numbers in a list. (Recall that each successive Fibonacci number is defined by summing the previous two, starting with the numbers 1 and 1.) Commit to GitHub.
    * Hint: Use the python template file in the info repository to make sure you have the correct structure. You should have a `#!` line at the top, a module docstring, function definitions, function docstrings, and informative comments in your code.
    * Example: ```fibonacci(5)``` should return ```[1,1,2,3,5]``` 
    * Example: the last element of ```fibonacci(1000)``` should be: 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    * Verify that running ```nosetests3 test_sequences.py``` in a terminal within the repository successfully finds and runs all tests.
    * Make sure the function only returns a list. Have it raise an exception if a nonsensical argument ```n``` is given (i.e., not a positive integer).
1. Write an executable python script ```fib.py``` that loads ```sequences.py``` as a module, reads one command line argument ```n```, runs ```fibonacci(n)```, then prints the last element of the result. Commit the script to GitHub.
    * If an exception is raised, catch it and print an appropriate error message to the screen. 
    * Make sure you use the template to set up a proper ```main(argv)``` method called from inside a ```___main___``` environment. Your script should not execute any code if it is loaded as a module.
    * Remember to make your script executable with ```chmod```.
    * Verify that running ```nosetests3 test_fib.py``` in a terminal successfully runs the tests.
1. Write a bash script ```runfibs.sh``` that uses bash to run ```fib.py``` for arguments ```n``` from 1 to 10000.  For each argument, redirect the output of the script to a comma-separated-value file ```fibs.csv``` such that each fibonacci number is separated by a comma (with no newlines). Commit the shell script (but not the csv file) to GitHub.
    * If a ```fibs.csv``` file already exists, back it up: move the existing file to ```fibs.csv.bak```, then create the new file. Inform the user that this backup occurred.
    * If a backup already exists, inform the user, then exit the program with an error code (not 0) before any files are overwritten.

Note : the homework this week will be to finish all of the classwork, and include some minor modifications.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have. You can use the GitHub web interface to edit this file directly for now.

**This assignments sees us combining our existing knowledge in bash scripting and python. This assignment was helpful in illustrating a good program workflow with modular code. Because of this modular design, if we came back to this assignment in the future it would be easy and painless to edit existing modules or add new ones without cluttering the main executable function**
## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,
# Enea Dodi, Jack Savage, Gwyneth Casey
