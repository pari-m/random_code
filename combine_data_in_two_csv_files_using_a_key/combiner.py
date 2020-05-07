#Random program I wrote to solve a specific problem with combining data from two csv files.
#Could have been done using excel's vlookup but what is the fun in that?
#Pari
#2020-05-08

import csv

debug = 1

name_dict = {}
email_dict = {}

csvfile_list = []


def get_info(info_list,id):
	name_and_email_list = []
	for index,item in enumerate(info_list):
		

		if item[0] == str(id):

			return item

# customers.csv has the following columns 
# "id","email","First name","Last name"
# row[0] = id
# row[1] = email
# row[2] = First Name
# row[3] = Last Name

#The below code was used to open the customers csv and combine the first name and last name.

#Now it reads from a csv and appends the content to a list


with open('customers.csv') as csvfile:
	userfile = csv.reader(csvfile,delimiter =',')
	for index,row in enumerate(userfile):
		if debug == 1:
			print(row[0])
		if index < 0:							# condition is always false 
			full_name = row[2] +' '+ row[3]
			row[2] = full_name
			name_dict.update({row[0]:full_name})
			email_dict.update({row[0]:row[1]})
			if debug == 1:
				print(row)
		csvfile_list.append(row)

csvfile.close()

#converted_file.csv has the following colunms.
#"id","customerid","Name","Email"
#where customerid is the same as customer.csv(id)
#This below snipped reads from converted_file.csv and creates a new list that has the new values for
# Name and email column that are picked up from the customer.csv file

# update_ticket_list is then used to create a new csv in the next block


updated_tickets_list = []

with open('Converted_file.csv') as csvfile:
	ticketsfile = csv.reader(csvfile,delimiter =',')
	for index,row in enumerate(ticketsfile):
		if index == 0: 							#to copy the header
			updated_tickets_list.append(row)
		if index > 0: 							 #Copy rest of rows
			customerid = row[1] 				#Pull out the customerid
			if debug == 1:
				print(row[1])
			name_and_email = get_info(csvfile_list,customerid)  #get a list containing name_and_email from the customerid
			if debug == 1:
				print(name_and_email)
			if name_and_email != None:    #Sanity check for when name and email are not present in the customer.csv
				row[2] = name_and_email[2] #replace the contents of the name cell
				row[3] = name_and_email[1] #replace the contents of the email cell
			updated_tickets_list.append(row)

csvfile.close()

if debug == 1:
	print(updated_tickets_list)

# Very simple operation, it opens a writable csv file and dumps the content of the updated_ticket_list

with open('output.csv', 'w') as csvfile:
	wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	for index,row in enumerate(updated_tickets_list):
		wr.writerow(row)

csvfile.close()