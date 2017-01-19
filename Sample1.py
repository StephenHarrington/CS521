'''
Name:        Stephen Harrington
Course:      CS521
Date:        January 18, 2017
Assignment:  Code Sample
Description: This code contains a series of interactive python statements highlighting 
             python's input/output operations and has the bonus of teaching slices into a string
             by asking the user to answer some questions about slicing into a string.
             
             The code does use the handy python function eval() which is not necessary for any
             homework, but provides a way to take a string and have the python interpreter evaluate 
             the string.
'''

endBothLoops = False
correctAnswers = 0
maxTries = 3

allTests = [ "[2]", "[1:3]", "[:3]", "[-1]", "[:-1]", "[1:]",
             "[1:9]", "[1:9:2]", "[::-1]" ]

string = input( "Type an input string with at least 10 characters or hit enter for default: " )

if string == "" or len( string ) < 10:
    string = "Hello World!"
    print( "Selected default string " + string )
else:
    print( "Selected string " + string )

print( "Hit enter with no answer to end" )
    
for test in allTests:

    currentTry = 0

    while currentTry < maxTries:

        var = input( "\nWhat is " + string + test + " ? " )
        if var == "":
            endBothLoops = True
            break

        answer = eval( "\"" + string + "\"" + test )
        if var == answer:
            print( "Correct " + string + test + " == " + "\"" + answer + "\"" )
            correctAnswers +=1
            break
        else:
            print( "Incorrect.  Try again?" )
            currentTry += 1

    if endBothLoops:
        break
        
print( "\n\nDone!  Your score is " + str(round( 100 * correctAnswers / len( allTests ), 0)) + '%' )
