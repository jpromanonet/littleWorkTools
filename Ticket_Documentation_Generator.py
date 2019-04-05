#! python3

# This scripts generates the main dir tree and plain text documents
# to document an IT Ticket
# Just for personal use.

# Importing libraries and frameworks

import os

# User parameters

print('Ingrese ID de ticket')
ticket_Number = input()
chdir = os.chdir('Enter your working directory here')
dir_Ticket = (str(ticket_Number)) 

# Script logic

	# Creating new working dir

os.makedirs(dir_Ticket)

	# Changing working dir

os.chdir('Enter your working directory here' + '\\' + str(ticket_Number))

	# Creating sub-dirs

os.makedirs('Screen_Shots')
os.makedirs('Mail')
os.makedirs('Attachments')

	# Creating Plaintext files

request_File = open(ticket_Number + '_01_Request.txt', 'w')
request_File.close()

solution_File = open(ticket_Number + '_02_Solution.txt', 'w')
request_File.close()

print('Done!')