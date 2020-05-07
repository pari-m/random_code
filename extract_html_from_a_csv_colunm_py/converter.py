# Simple Program that takes a CSV file and extracts only the HTML from the value in the eight column
# and puts it back into a new file  

#Row 8 in working.csv has html content as a substring in it.

# this program extracts that and puts in back in a new csv's row8

import csv

actualrows = []

with open('working.csv') as csvfile:   # reads from working.csv
	readcsv = csv.reader(csvfile, delimiter=',')
	for index,row in enumerate(readcsv):
	#	print(row[8])
		if index == 0:
			actualrows.append(row)
		full_body_of_email = row[8]
		if index > 0:
			html_text= full_body_of_email[full_body_of_email.find('<html>'):full_body_of_email.find('</html>')]
			html_text=html_text+ '</html>'
			row[8] = html_text
			print(index)
			actualrows.append(row)
csvfile.close()

with open('output.csv', 'wt') as csvfile2: #writes to output.csv
	writecsv = csv.writer(csvfile2)
	for row in actualrows:
		writecsv.writerow(row)

csvfile2.close()
