#! python3

# minimalLogger.py creates a tagged log with a nice format in .html files to simple read and publish

# --------------------------------------------------------------------------------------------------------------

# Calling libraries and frameworks

import random
import os
import datetime

# Defining global variables

    ## User parameters and doc construction variables

userInputLog = None # Gonna be the user input to concatenate with the htmlStr
fullInputLog = None # It takes the userInputLog and adds bootstrap style
htmlStr = None # Gonna be the HTML body without end tags
htmlStrEndTags = None # Gonna be the HTML end tags
logFileName = None # It's the name with the date
logDateTime = None # Datetime of every log
randomCode = 0 # It's the unique ID number of every file.
fullFileName = None # It's the sum of logFileName and randomCode
workingDir = None # It's the dir where the user is gonna save the log file.
keepLogging = True # Value = False stop logging
dirName = None # Directory with the date as name
fullWorkingPath = None # It's the sum of workingDir and dirName
titleLog = None # Title for the log file.

    ## Stats Variables

stats = None # Contains the string with the HTML tags
startLogTime = None # It's the time the user start loggin
finishLogTime = None # It's the time the user finish loggin
beginLog = 0 # The same as startLogTime but as datetime
endLog = 0 # The same as startLogTime but as datetime
totalLogTime = None # It's the time the user spend writing
totalLogs = 0 # How many logs in this file

# User parameters

print('Please introduce the working directory: ')
workingDir = input()
print(' ')
print('Please write a title for the file: ')
titleLog = input()
print('----------------------------------------------------------------------')
print(' ')

# Program Logic

    ## Setting the stats values before start the writing
startLogTime = datetime.datetime.now().strftime("%H:%M:%S")
beginLog = datetime.datetime.now()

	## Create dir if not exist or use it to save files for the day
dirName = datetime.datetime.now().strftime("%Y-%m-%d")
fullWorkingPath = workingDir + '\\' + dirName

if not os.path.exists(str(fullWorkingPath)):
    os.makedirs(fullWorkingPath)

os.chdir(str(fullWorkingPath))
	
    ## Creating the filename 
logFileName = datetime.datetime.now().strftime("%Y-%m-%d") # Establish the filename to the date it's create
randomCode = random.randint(1,10000000) # It's create the serial random number to validate the file
fullFileName = str(logFileName) + '_(Sn#' + str(randomCode) + ').html' # Full file name

    ## Creating the HTML body structure | Without end tags

htmlStr = ''' 
            <DOCTYPE! html>
                <html>
                    <head>
                        <title>LOG: ''' + fullFileName + '''</title>

                            <!-- Latest compiled and minified CSS -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

                            <!-- Optional theme -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

                            <!-- Latest compiled and minified JavaScript -->
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
                    </head>
                    <body>
                        <header class="bg-primary">
                            <div class="container">
                                <div class="row">
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-sx-12">
                                        <center>
                                            <h1><b>FULL LOG | '''+str(logFileName)+''' | Sn: '''+str(randomCode)+'''</b></h1>
                                        </center> 
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-sx-12">
                                        <center>
                                            <h4 style="background: #228B22;"><b>'''+str(titleLog)+'''</b></h4>
                                        </center> 
                                    </div>
                                </div>
                            </div>
                        </header>
                        <main>
                            <div class="container">
                                <div class="row">'''

    ## Creating the HTML body structure | End Tags to close the document

htmlStrEndTags = '''    <center>
							<b>MinimalLoggerPy</b> by <a href="http://www.jpromano.net" target="_blank">Juan P. Romano</a> | GitHub Repo  
							</br>
							<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/" target="_blank">
								<img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" />
							</a>
						</center>
					</footer>
                </body>
            </html>'''

    ## Here starts the HTML document
htmlFile= open(fullFileName,"w")
htmlFile.write(str(htmlStr))

    ## Here starts the loggin module
while keepLogging == True:
        ### Creating the log header
    logDateTime = datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
        ### User input log
    print('Start writing your log: ')
    userInputLog = input()
        ### Now it creates the log input with the style and the user input
    fullInputLog = '''</br></br>
                    <div class = "col-lg-12 col-md-12 col-sm-12 col-sx-12">
                        <div class="panel panel-success">
                            <div class="panel-heading">Log time: <b>'''+logDateTime+'''</b></div>'''+userInputLog+'''</div>
                    </div>'''
    htmlFile.write(str(fullInputLog))
        ### Counting logs inputs
    totalLogs += 1
        ### Ask if the user wants to keep adding logs
    print(' ')
    print('Do you want to keep writing? y/n')
    option = input()
    if option == 'y':
        keepLogging = True
    elif option == 'Y':
        keepLogging = True
    else:
        break

    ## Setting the stats values after finish the writing
finishLogTime = datetime.datetime.now().strftime("%H:%M:%S")
endLog = datetime.datetime.now()
totalLogTime = endLog - beginLog # How much time spend writing

    ## Creating the HTML tags for the Stats line

stats = '''                 </div>
                        </div>
                    </main>
                    </br>
                    </br>
                    </br>
                    </br>
                    </br>
                    <footer class="bg-info" style="position: fixed; bottom: 0; left: 0; width: 100%;"><div class="container-fluid" style="background: #FF8C00;>
                            <div class="row">
                                <div class="col-lg-12 col-md-12 col-sm-12 col-sx-12">
                                    <div align-text="left">
                                        <b class="bg-danger">Start time:</b><b> '''+str(startLogTime)+''' Hs </b>
                                        <b class="bg-danger">Finish time:</b><b> '''+str(finishLogTime)+''' Hs </b>
                                        <b class="bg-danger">SESSION TIME:</b><b> '''+str(totalLogTime)+''' Hs </b>
                                        <b style="background: #008080;">    TOTAL ENTERS IN FILE:<font color="white">   '''+str(totalLogs)+'''  </font></b>
                                    </div> 
                                </div>
                            </div>
                        </div>'''

    ## Here ends the HTML document
htmlFile.write(str(stats))
htmlFile.write(str(htmlStrEndTags))
htmlFile.close()