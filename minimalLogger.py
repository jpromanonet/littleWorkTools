#! python3

# minimalLogger.py creates a tagged log with a nice format in .html files to simple read and publish

# --------------------------------------------------------------------------------------------------------------

# Calling libraries and frameworks

import random
import os
import datetime
# Install this one from this git repo: git clone https://github.com/jmcnamara/XlsxWriter.git
import xlsxwriter

# Defining global variables

# User parameters and doc construction variables

userInputLog = None  # Gonna be the user input to concatenate with the htmlStr
fullInputLog = None  # It takes the userInputLog and adds bootstrap style
htmlStr = None  # Gonna be the HTML body without end tags
htmlStrEndTags = None  # Gonna be the HTML end tags
logFileName = None  # It's the name with the date
logDateTime = None  # Datetime of every log
randomCode = 0  # It's the unique ID number of every file.
fullFileName = None  # It's the sum of logFileName and randomCode
workingDir = None  # It's the dir where the user is gonna save the log file.
keepLogging = True  # Value = False stop logging
dirName = None  # Directory with the date as name
fullWorkingPath = None  # It's the sum of workingDir and dirName
titleLog = None  # Title for the log file.

# User folders

# Option variable when the logger ask if to create a folder.
folderOption = None
folderCodePath = None  # Code folder path
folderQueryPath = None  # Query folder path
folderDocsPath = None  # Documents folder path
folderRandomStuff = None  # Random stuff folder path
importantMailsFolder = None  # Important mail of the day folder

# Stats Variables

stats = None  # Contains the string with the HTML tags
startLogTime = None  # It's the time the user start loggin
finishLogTime = None  # It's the time the user finish loggin
beginLog = 0  # The same as startLogTime but as datetime
endLog = 0  # The same as startLogTime but as datetime
totalLogTime = None  # It's the time the user spend writing
totalLogs = 0  # How many logs in this file

# User parameters and setting working environment

workingDir = input('Please introduce the working directory: ')
print(' ')
titleLog = input('Please write a title for the file: ')
print(' ')

# Setting the stats values before start the writing
startLogTime = datetime.datetime.now().strftime("%H:%M:%S")
beginLog = datetime.datetime.now()

# Create dir if not exist or use it to save files for the day
dirName = datetime.datetime.now().strftime("%Y-%m-%d")
fullWorkingPath = workingDir + '\\' + dirName

if not os.path.exists(str(fullWorkingPath)):
    os.makedirs(fullWorkingPath)

os.chdir(str(fullWorkingPath))

# Ask the user to create a spreadsheet week plan.
weekplanOption = input('Create a week plan template for the week? Y/y/n ')
print(' ')
if weekplanOption == 'Y':
    # Datetime for filename
    weekPlanFileName = datetime.datetime.now().strftime("%Y-%m-%d")
    # Creates the workbook and the spreadsheet
    workbook = xlsxwriter.Workbook('Week_Plan_'+weekPlanFileName+'.xlsx')
    worksheet = workbook.add_worksheet()

    # Set the starting point for the file.
    row = 0
    col = 0

    # Styles for the cols and set days
    headerColor = workbook.add_format({'bg_color': 'green', 'bold': True})

    worksheet.write('A1', 'Lunes', headerColor)
    worksheet.write('B1', 'Martes', headerColor)
    worksheet.write('C1', 'Miercoles', headerColor)
    worksheet.write('D1', 'Jueves', headerColor)
    worksheet.write('E1', 'Viernes', headerColor)

    workbook.close()

elif weekplanOption == 'y':
    # Datetime for filename
    weekPlanFileName = datetime.datetime.now().strftime("%Y-%m-%d")
    # Creates the workbook and the spreadsheet
    workbook = xlsxwriter.Workbook('Week_Plan_'+weekPlanFileName+'.xlsx')
    worksheet = workbook.add_worksheet()

    # Set the starting point for the file.
    row = 0
    col = 0

    # Styles for the cols and set days
    headerColor = workbook.add_format({'bg_color': 'green', 'bold': True})

    worksheet.write('A1', 'Lunes', headerColor)
    worksheet.write('B1', 'Martes', headerColor)
    worksheet.write('C1', 'Miercoles', headerColor)
    worksheet.write('D1', 'Jueves', headerColor)
    worksheet.write('E1', 'Viernes', headerColor)

    workbook.close()

    # Ask if the user wants to create one folder to save code snippets made that day or queries.
folderOption = input(
    'Create dailyCodeSnippets/dailyQuerys/dailyDocs/randomStuff/importantMail folders? (y/n) ')
if folderOption == 'y':

        # Creates the code snippets folder, if exists don't
    folderCodePath = fullWorkingPath + '/dailyCodeSnippets'
    if not os.path.exists(str(folderCodePath)):
        os.makedirs(folderCodePath)

        # Creates the daily queries folder, if exists don't
    folderQueryPath = fullWorkingPath + '/dailyQueries'
    if not os.path.exists(str(folderQueryPath)):
        os.makedirs(folderQueryPath)

        # Creates the daily documents folder, if exists don't
    folderDocsPath = fullWorkingPath + '/dailyDocs'
    if not os.path.exists(str(folderDocsPath)):
        os.makedirs(folderDocsPath)

        # Creates the random stuff folder, if exists don't
    folderRandomStuff = fullWorkingPath + '/randomStuff'
    if not os.path.exists(str(folderRandomStuff)):
        os.makedirs(folderRandomStuff)

        # Creates the random stuff folder, if exists don't
    importantMailsFolder = fullWorkingPath + '/importantMailOfTheDay'
    if not os.path.exists(str(importantMailsFolder)):
        os.makedirs(importantMailsFolder)

elif folderOption == 'Y':

        # Creates the code snippets folder, if exists don't
    folderCodePath = fullWorkingPath + '/dailyCodeSnippets'
    if not os.path.exists(str(folderCodePath)):
        os.makedirs(folderCodePath)

        # Creates the daily queries folder, if exists don't
    folderQueryPath = fullWorkingPath + '/dailyQueries'
    if not os.path.exists(str(folderQueryPath)):
        os.makedirs(folderQueryPath)

        # Creates the daily documents folder, if exists don't
    folderDocsPath = fullWorkingPath + '/dailyDocs'
    if not os.path.exists(str(folderDocsPath)):
        os.makedirs(folderDocsPath)

        # Creates the random stuff folder, if exists don't
    folderRandomStuff = fullWorkingPath + '/randomStuff'
    if not os.path.exists(str(folderRandomStuff)):
        os.makedirs(folderRandomStuff)

        # Creates the random stuff folder, if exists don't
    importantMailsFolder = fullWorkingPath + '/importantMailOfTheDay'
    if not os.path.exists(str(importantMailsFolder)):
        os.makedirs(importantMailsFolder)

print('---------------------------------------------------------------------------------------------------------')
print(' ')
print('***********************')
print('*** EASY GUIDELINES ***')
print('***********************')
print(' ')
print('1. ALWAYS read the documentation, every doc and written word about any project helps.')
print(' ')
print('2. ASK for more documentation just in case.')
print(' ')
print('3. SEARCH on internet first.')
print(' ')
print('4. ALWAYS use the pomodoro technique')
print(' ')
print('5. ALWAYS spend 2 pomodores(50min to 1hr) trying to solve a problem if you are stuck,')
print('   if you did not solve it, ASK for help, never get over the 2 pomodores to ASK, its the limit.')
print(' ')
print('6. DOCUMENT everything, log your daily work, even just for yourself')
print(' ')
print('7. SAVE every important file in many places to be sure.')
print(' ')
print('8. PUSH to GIT all the time, make a parallel branch if you are not sure of the change but PUSH')
print(' ')
print('''9. REMEMBER: git pull && git add -A && git commit -m 'your message' && git push ''')
print(' ')
print('10. REMEMBER to always close the log file or else, it would be lost!!!')
print('')
print('11. READ THE CODE 3 times before ask for help!')
print('')
print('12. RTFM = READ THE FUCKING MANUAL!')
print('---------------------------------------------------------------------------------------------------------')

# Program Logic

# Creating the filename
# Establish the filename to the date it's create
logFileName = datetime.datetime.now().strftime("%Y-%m-%d")
# It's create the serial random number to validate the file
randomCode = random.randint(1, 10000000)
fullFileName = str(logFileName) + '_(Sn#' + \
    str(randomCode) + ').html'  # Full file name

# Creating the HTML body structure | Without end tags

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

# Creating the HTML body structure | End Tags to close the document

htmlStrEndTags = '''    <center>
							<b>MinimalLoggerPy</b> by <a href="http://www.jpromano.net" target="_blank">Juan P. Romano</a> | <a href="https://www.github.com/jpromanonet" target="_blank">GitHub Repo</a>  
							</br>
							<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/" target="_blank">
								<img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" />
							</a>
						</center>
					</footer>
                </body>
            </html>'''

# Here starts the HTML document
htmlFile = open(fullFileName, "w")
htmlFile.write(str(htmlStr))

# Here starts the loggin module
while keepLogging == True:
        # Creating the log header
    logDateTime = datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
    # User input log
    userInputLog = input("Log: ")
    # Now it creates the log input with the style and the user input
    fullInputLog = '''</br></br>
                    <div class = "col-lg-12 col-md-12 col-sm-12 col-sx-12">
                        <div class="panel panel-success">
                            <div class="panel-heading">Log time: <b>'''+logDateTime+'''</b></div>'''+userInputLog+'''</div>
                    </div>'''
    htmlFile.write(str(fullInputLog))
    # Counting logs inputs
    totalLogs += 1
    # Ask if the user wants to keep adding logs
    print(' ')
    option = input('Do you want to keep writing? y/n ')
    if option == 'y':
        keepLogging = True
    elif option == 'Y':
        keepLogging = True
    else:
        break

    # Setting the stats values after finish the writing
finishLogTime = datetime.datetime.now().strftime("%H:%M:%S")
endLog = datetime.datetime.now()
totalLogTime = endLog - beginLog  # How much time spend writing

# Creating the HTML tags for the Stats line

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

# Here ends the HTML document
htmlFile.write(str(stats))
htmlFile.write(str(htmlStrEndTags))
htmlFile.close()
